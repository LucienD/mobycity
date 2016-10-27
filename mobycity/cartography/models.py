#coding:utf-8

from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from django_google_maps.fields import AddressField, GeoLocationField


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Titre')
    image = models.ImageField(upload_to='cartography_category', verbose_name=u'Image')
    placeholder_image = models.ImageField(upload_to='cartography_category', verbose_name=u'Image de remplacement')

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = u'Catégorie'
        verbose_name_plural = u'Catégories'


class PointOfInterest(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Nom')
    category = models.ForeignKey(Category, verbose_name=u'Catégorie')
    description = HTMLField(blank=True, verbose_name=u'Description')
    address = AddressField(max_length=100, verbose_name=u'Adresse')
    geolocation = GeoLocationField(verbose_name=u'Géolocalisation')
    image = models.ImageField(upload_to='cartography_pointOfInterest', blank=True, verbose_name=u'Image')
    phone = models.CharField(max_length=10, blank=True, verbose_name=u'Téléphone')
    website = models.URLField(blank=True, verbose_name=u'Site internet')
    opening_hours = models.CharField(max_length=254, blank=True, verbose_name=u'Heures d\'ouverture')

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = u'Point d\'intérêt'
        verbose_name_plural = u'Points d\'intérêt'