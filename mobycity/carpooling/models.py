#coding:utf-8

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


lat_1km = 0.008
lng_1km = 0.012


class Carpool(models.Model):
    creation_datetime = models.DateTimeField(blank=True, default=timezone.now, verbose_name=u'Date de création')
    update_datetime = models.DateTimeField(blank=True, default=timezone.now, verbose_name=u'Date de mise à jour')

    organizer = models.ForeignKey(User)

    departure_latitude = models.FloatField(verbose_name=u'Départ - latitude')
    departure_longitude = models.FloatField(verbose_name=u'Départ - longitude')
    arrival_latitude = models.FloatField(verbose_name=u'Arrivée - latitude')
    arrival_longitude = models.FloatField(verbose_name=u'Arrivée - longitude')

    FREQUENCY_CHOICES = (
        ('OCC', u'Ponctuel'),
        ('REG', u'Régulier'),
    )
    frequency = models.CharField(max_length=3, choices=FREQUENCY_CHOICES, default='OCC', verbose_name=u'Fréquence')

    occ_departure_datetime = models.DateTimeField(null=True, blank=True, verbose_name=u'Date de départ')
    occ_arrival_datetime = models.DateTimeField(null=True, blank=True, verbose_name=u'Date d\'arrivée')
    
    reg_departure_time = models.TimeField(null=True, blank=True, verbose_name=u'Heure de départ')
    reg_arrival_time = models.TimeField(null=True, blank=True, verbose_name=u'Heure d\'arrivée')

    SEATS_NUMBER_CHOICES = [(i,i) for i in range(1, 11)]
    SEATS_NUMBER_CHOICES.append((None, u'Places disponibles'))
    seats_number = models.PositiveSmallIntegerField(max_length=10, choices=SEATS_NUMBER_CHOICES, verbose_name=u'Places disponibles')
    
    free = models.BooleanField(default=True, verbose_name=u'Covoiturage gratuit')
    comment = models.TextField(blank=True, verbose_name=u'Commentaire')
    cancelled = models.BooleanField(default=False, verbose_name=u'Annulé')

    class Meta:
        verbose_name = u'Covoiturage'
        verbose_name_plural = u'Covoiturages'

    def __unicode__(self):
        return '%d' % self.id

class Subscription(models.Model):
    creation_datetime = models.DateTimeField(blank=True, default=timezone.now, verbose_name=u'Date de création')
    update_datetime = models.DateTimeField(blank=True, default=timezone.now, verbose_name=u'Date de mise à jour')

    subscriber = models.ForeignKey(User, verbose_name=u'Inscrit')
    carpool = models.ForeignKey(Carpool, verbose_name=u'Covoiturage')

    cancelled = models.BooleanField(default=False, verbose_name=u'Annulée')
    accepted = models.NullBooleanField(default=None, verbose_name=u'Acceptée')

    class Meta:
        verbose_name = u'Inscription'
        verbose_name_plural = u'Inscriptions'

    def __unicode__(self):
        return '%d' % self.id
