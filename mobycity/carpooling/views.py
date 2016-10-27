# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core import serializers
from django.utils import timezone
from django.db import connection
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.conf import settings
from datetime import date, datetime, timedelta
from allauth.account.decorators import verified_email_required

from carpooling.forms import OfferCarpoolForm, SearchCarpoolForm
from carpooling.models import Carpool, Subscription, lat_1km, lng_1km
from cartography.models import Category, PointOfInterest


# Marges pour la recherche
search_timedelta = timedelta(minutes=15)
search_lat_delta = lat_1km
search_lng_delta = lng_1km


@verified_email_required
def offer(request):
    form = OfferCarpoolForm(request.POST or None, initial={'occ_departure_datetime': timezone.now, 'occ_arrival_datetime': timezone.now, 'reg_departure_time': timezone.now, 'reg_arrival_time': timezone.now})

    # cartography
    category_list_json = serializers.serialize('json', Category.objects.all())
    point_of_interest_list_json = serializers.serialize('json', PointOfInterest.objects.all())

    context = {
        'form': form,

        # cartography
        'category_list_json': category_list_json,
        'point_of_interest_list_json': point_of_interest_list_json,
    }

    if request.method == 'POST':
        if form.is_valid():
            carpool = form.save(commit=False)
            carpool.organizer = request.user
            carpool.save()
            
            messages.success(request, u'Votre offre de covoiturage a été publiée.')
            return HttpResponseRedirect('')
        else:
            messages.error(request, 'Une erreur est survenue.')
            
    return render(request, 'carpooling/offer.html', context)


def search(request):
    form = SearchCarpoolForm(request.GET or None, initial={'occ_arrival_datetime': timezone.now, 'reg_arrival_time': timezone.now})
    
    # cartography
    category_list_json = serializers.serialize('json', Category.objects.all())
    point_of_interest_list_json = serializers.serialize('json', PointOfInterest.objects.all())

    context = {
        'form': form,

        # cartography
        'category_list_json': category_list_json,
        'point_of_interest_list_json': point_of_interest_list_json,
    }

    return render(request, 'carpooling/search.html', context)


def search_result(request):
    carpool_list = []
    subscription_carpool_list = None

    form = SearchCarpoolForm(request.GET or None, initial={'occ_arrival_datetime': timezone.now, 'reg_arrival_time': timezone.now})

    if request.GET:
        if form.is_valid():

            # Frequence selectionnee
            # Ordre d'affichage
            carpool_list = Carpool.objects.filter(frequency=form.cleaned_data['frequency']).order_by('-creation_datetime')
            
            # Trajet occasionnel
            if form.cleaned_data['frequency'] == 'OCC':
                # Date a venir
                carpool_list = carpool_list.filter(occ_departure_datetime__gt=timezone.now)
                
                # Autour de la date/heure recherchee
                occ_arrival_datetime_min = form.cleaned_data['occ_arrival_datetime'] - search_timedelta
                occ_arrival_datetime_max = form.cleaned_data['occ_arrival_datetime'] + search_timedelta
                
                carpool_list = carpool_list.filter(occ_arrival_datetime__range=(occ_arrival_datetime_min, occ_arrival_datetime_max))
                
            # Trajet regulier
            if form.cleaned_data['frequency'] == 'REG':
                (datetime.combine(date(1, 1, 1), form.cleaned_data['reg_arrival_time']) + search_timedelta).time()
                
                # Autour de l'heure recherchee
                reg_arrival_time_min = (datetime.combine(date(2, 2, 2), form.cleaned_data['reg_arrival_time']) - search_timedelta).time()
                reg_arrival_time_max = (datetime.combine(date(2, 2, 2), form.cleaned_data['reg_arrival_time']) + search_timedelta).time()
                
                print reg_arrival_time_min
                print reg_arrival_time_max
                
                # Sur 1 jour
                if reg_arrival_time_min <= reg_arrival_time_max:
                    carpool_list = carpool_list.filter(reg_arrival_time__gte=reg_arrival_time_min)
                    carpool_list = carpool_list.filter(reg_arrival_time__lte=reg_arrival_time_max)
                # Sur 2 jours
                else:
                    carpool_list = carpool_list.filter(Q(reg_arrival_time__gte=reg_arrival_time_min) | Q(reg_arrival_time__lte=reg_arrival_time_max))
            
            # Fourchette pour le point de depart
            departure_latitude_max = form.cleaned_data['departure_latitude'] - search_lat_delta
            departure_latitude_min = form.cleaned_data['departure_latitude'] + search_lat_delta
            departure_longitude_max = form.cleaned_data['departure_longitude'] - search_lng_delta
            departure_longitude_min = form.cleaned_data['departure_longitude'] + search_lng_delta

            carpool_list = carpool_list.filter(departure_latitude__range=(str(departure_latitude_max), str(departure_latitude_min)))
            carpool_list = carpool_list.filter(departure_longitude__range=(str(departure_longitude_max), str(departure_longitude_min)))

            # Fourchette pour le point d'arrivee
            arrival_latitude_max = form.cleaned_data['arrival_latitude'] - search_lat_delta
            arrival_latitude_min = form.cleaned_data['arrival_latitude'] + search_lat_delta
            arrival_longitude_max = form.cleaned_data['arrival_longitude'] - search_lng_delta
            arrival_longitude_min = form.cleaned_data['arrival_longitude'] + search_lng_delta

            carpool_list = carpool_list.filter(arrival_latitude__range=(str(arrival_latitude_max), str(arrival_latitude_min)))
            carpool_list = carpool_list.filter(arrival_longitude__range=(str(arrival_longitude_max), str(arrival_longitude_min)))

            # Pas annule
            carpool_list = carpool_list.filter(cancelled=False)

            cursor = connection.cursor()

            # TODO Simplifier en une seule requete
            # Covoiturages dans lesquels il reste au moins une place
            cursor.execute('select distinct c.id '
                           'from carpooling_carpool c '
                           'where c.seats_number > '
                           '        (select count (*) '
                           '        from carpooling_subscription s '
                           '        where s.carpool_id = c.id'
                           '        and s.accepted <> true)'
                           'order by c.id ASC;')

            available_carpool_list = cursor.fetchall()
            available_carpool_id_list = [i[0] for i in available_carpool_list]

            carpool_list = carpool_list.filter(id__in=available_carpool_id_list)

            # Pagination
            paginator = Paginator(carpool_list, 10)
            page = request.GET.get('page')
            
            try:
                carpool_paginated_list = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                carpool_paginated_list = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                carpool_paginated_list = paginator.page(paginator.num_pages)

            # Liste des inscriptions de l'utilisateur
            if not request.user.is_anonymous():
                subscription_carpool_list = Subscription.objects.values_list('carpool').filter(subscriber=request.user)
                
        else:
            messages.error(request, u'Une erreur est survenue.')
            return HttpResponseRedirect('/carpooling/search')

    else: 
        return HttpResponseRedirect('/carpooling/search')
    
    carpool_list_json = serializers.serialize('json', carpool_list, fields=('departure_latitude', 'departure_longitude', 'arrival_latitude', 'arrival_longitude'))

    # cartography
    category_list_json = serializers.serialize('json', Category.objects.all())
    point_of_interest_list_json = serializers.serialize('json', PointOfInterest.objects.all())

    context = {
        'form': form,
        'carpool_list': carpool_paginated_list,
        'carpool_list_json': carpool_list_json,
        'subscription_carpool_list': subscription_carpool_list,

        # cartography
        'category_list_json': category_list_json,
        'point_of_interest_list_json': point_of_interest_list_json,
    }
    
    return render(request, 'carpooling/search_result.html', context)


@verified_email_required
def subscribe(request):
    if request.method == 'POST' and 'carpool_id' in request.POST:
        carpool = Carpool.objects.get(pk=request.POST['carpool_id'])
        accepted_subscription_count = Subscription.objects.filter(carpool=carpool, accepted=True).count()

        # L'inscrit ne peut etre l'organisateur du covoiturage
        # Il doit y avoir suffisamment de place disponible
        # Le covoiturage ne doit pas etre annule
        # La date de depart ne doit pas etre depassee
        if carpool.organizer != request.user and accepted_subscription_count < carpool.seats_number and not carpool.cancelled and (carpool.frequency == 'REG' or (carpool.frequency == 'OCC' and carpool.occ_departure_datetime >= timezone.now())):
            # Deja inscrit pour ce covoiturage
            try:
                Subscription.objects.get(subscriber=request.user, carpool=carpool)

            # Inscription a ce covoiturage
            except Subscription.DoesNotExist:
                subscription = Subscription(subscriber=request.user, carpool=carpool)
                subscription.save()
                
                sender = settings.MANAGERS[0][0] + ' <' + settings.MANAGERS[0][1] + '>'
                subject = '[mobycity.net] ' + u'Demande d\'inscription à votre covoiturage'
                message = request.user.first_name + ' ' + request.user.last_name + ' (' + request.user.email + ')' + u' souhaite s\'inscrire à votre covoiturage'
                recipients = [carpool.organizer.email]
                
                send_mail(subject, message, sender, recipients)

            messages.success(request, u'Votre inscription a été envoyée à l\'organisateur.')
        else:
            messages.error(request, u'Une erreur est survenue.')
            
        print request.POST    
        
    if 'next' in request.POST:
        return HttpResponseRedirect(request.POST['next'])
    
    return HttpResponseRedirect('/carpooling/search')


@login_required
def user_list_offers(request):
    carpool_list = Carpool.objects.filter(organizer=request.user).order_by('-creation_datetime')
    carpool_id_list = carpool_list.values_list('id', flat=True)
    carpool_list_json = serializers.serialize('json', carpool_list, fields=('departure_latitude', 'departure_longitude', 'arrival_latitude', 'arrival_longitude'))

    subscription_list = Subscription.objects.filter(carpool_id__in=carpool_id_list)

    # Pagination
    paginator = Paginator(carpool_list, 10)
    page = request.GET.get('page')

    try:
        carpool_paginated_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        carpool_paginated_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        carpool_paginated_list = paginator.page(paginator.num_pages)

    # cartography
    category_list_json = serializers.serialize('json', Category.objects.all())
    point_of_interest_list_json = serializers.serialize('json', PointOfInterest.objects.all())

    context = {
        'carpool_list': carpool_paginated_list,
        'carpool_list_json': carpool_list_json,
        'subscription_list': subscription_list,

        # cartography
        'category_list_json': category_list_json,
        'point_of_interest_list_json': point_of_interest_list_json,
    }

    return render(request, 'carpooling/user_list_offers.html', context)


@login_required
def user_cancel_carpool(request):
    if request.method == 'POST' and request.POST['carpool_id']:
        carpool = Carpool.objects.get(pk=request.POST['carpool_id'])

        if carpool.organizer == request.user:
            carpool.cancelled = True
            subscriptions = Subscription.objects.filter(carpool_id=carpool.id)
            
            carpool.save()
            
            # Envoi email
            sender = settings.MANAGERS[0][0] + ' <' + settings.MANAGERS[0][1] + '>'
            subject = '[mobycity.net] ' + u'Annulation de votre covoiturage'
            message = request.user.first_name + ' ' + request.user.last_name + ' (' + carpool.organizer.email + ')' + u' a annulé son covoiturage.'
            recipients = [x.subscriber.email for x in subscriptions]

            send_mail(subject, message, sender, recipients)
            
            # Notification
            messages.success(request, u'Ce covoiturage a été annulé.')
        else:
            messages.error(request, u'Une erreur est survenue.')
            
    return HttpResponseRedirect('/carpooling/user-list-offers')

@login_required
def user_list_subscriptions(request):
    subscription_list = Subscription.objects.filter(subscriber=request.user)
    subscription_carpool_id_list = subscription_list.values_list('carpool_id', flat=True)

    carpool_list = Carpool.objects.filter(id__in=subscription_carpool_id_list)
    carpool_list_json = serializers.serialize('json', carpool_list, fields=('departure_latitude', 'departure_longitude', 'arrival_latitude', 'arrival_longitude'))

    # Pagination
    paginator = Paginator(subscription_list, 10)
    page = request.GET.get('page')

    try:
        subscription_paginated_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        subscription_paginated_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        subscription_paginated_list = paginator.page(paginator.num_pages)

    # cartography
    category_list_json = serializers.serialize('json', Category.objects.all())
    point_of_interest_list_json = serializers.serialize('json', PointOfInterest.objects.all())

    context = {
        'subscription_list': subscription_paginated_list,
        'carpool_list': carpool_list,
        'carpool_list_json': carpool_list_json,

        # cartography
        'category_list_json': category_list_json,
        'point_of_interest_list_json': point_of_interest_list_json,
    }

    return render(request, 'carpooling/user_list_subscriptions.html', context)


@login_required
def user_cancel_subscription(request):
    if request.method == 'POST' and request.POST['subscription_id']:
        subscription = Subscription.objects.get(pk=request.POST['subscription_id'])
        carpool = subscription.carpool

        if subscription.subscriber == request.user:
            subscription.cancelled = True
            subscription.save()
            
            # Envoi email    
            sender = settings.MANAGERS[0][0] + ' <' + settings.MANAGERS[0][1] + '>'
            subject = '[mobycity.net] ' + u'Annulation d\'une inscription à votre covoiturage'
            message = request.user.first_name + ' ' + request.user.last_name + ' (' + request.user.email + ')' + u' a annulé son inscription à votre covoiturage'
            recipients = [carpool.organizer.email]

            send_mail(subject, message, sender, recipients)
            
            # Notification
            messages.success(request, u'Votre inscription a été annulée.')
        else:
            messages.error(request, u'Une erreur est survenue.')
            
    return HttpResponseRedirect('/carpooling/user-list-subscriptions')


@login_required
def user_accept_or_deny_subscription(request):
    if request.method == 'POST' and request.POST['subscription_id']:
        subscription = Subscription.objects.select_related('carpool').get(pk=request.POST['subscription_id'])
        carpool = subscription.carpool
        
        if carpool.organizer == request.user:
            if request.POST.get('accept', False):
                subscription.accepted = True
                
                # Envoi email
                sender = settings.MANAGERS[0][0] + ' <' + settings.MANAGERS[0][1] + '>'
                subject = '[mobycity.net] ' + u'Confirmation de votre inscription à un covoiturage'
                message = carpool.organizer.first_name + ' ' + carpool.organizer.last_name + ' (' + carpool.organizer.email + ')' + u' a accepté votre inscription à son covoiturage.'
                recipients = [subscription.subscriber.email]

                send_mail(subject, message, sender, recipients)
                
            elif request.POST.get('deny', False):
                subscription.accepted = False
                
                # Envoi email
                sender = settings.MANAGERS[0][0] + ' <' + settings.MANAGERS[0][1] + '>'
                subject = '[mobycity.net] ' + u'Annulation de votre inscription à un covoiturage'
                message = carpool.organizer.first_name + ' ' + carpool.organizer.last_name + ' (' + carpool.organizer.email + ')' + u' a refusé votre inscription à son covoiturage.'
                recipients = [subscription.subscriber.email]

                send_mail(subject, message, sender, recipients)

            subscription.save()
            
            # Notification
            messages.success(request, u'Votre choix a été enregistré.')
        else:
            messages.error(request, u'Une erreur est survenue.')
            
    return HttpResponseRedirect('/carpooling/user-list-offers')