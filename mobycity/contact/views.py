# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

from contact.forms import ContactForm


def contact_form(request):
    if not request.user.is_anonymous():
        user_first_name = request.user.first_name
        user_last_name = request.user.last_name
        user_email = request.user.email
    else:
        user_first_name = ''
        user_last_name = ''
        user_email = ''
    
    form = ContactForm(request.POST or None, initial={'first_name': user_first_name, 'last_name': user_last_name, 'email': user_email})
    
    context = {
        'form': form,
    }
    
    if request.method == 'POST':
        if form.is_valid():
            # Envoi mail
            sender = settings.MANAGERS[0][0] + ' <' + settings.MANAGERS[0][1] + '>'
            subject = u'[mobycity.net] ' + form.cleaned_data['subject']
            message = u'Vous avez reçu un nouveau message de ' + form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name'] + ' (' + form.cleaned_data['email'] + ') : \n\n' + form.cleaned_data['message']
            recipients = [x[1] for x in settings.MANAGERS]
            
            send_mail(subject, message, sender, recipients)
            
            messages.success(request, u'Votre message a été envoyé.')
            
            return HttpResponseRedirect('')
    
    return render(request, 'contact/contact_form.html', context)