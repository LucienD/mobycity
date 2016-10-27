#coding:utf-8

from django.db import models
from django.utils import timezone
from djangocms_text_ckeditor.fields import HTMLField


class News(models.Model):
    creation_datetime = models.DateTimeField(default=timezone.now, verbose_name=u'Date de création')
    update_datetime = models.DateTimeField(default=timezone.now, verbose_name=u'Date de mise à jour')
    publication_datetime = models.DateTimeField(default=timezone.now, verbose_name=u'Date de publication')
    
    title = models.CharField(max_length=255, verbose_name=u'Titre')
    subtitle = models.CharField(blank=True, max_length=255, verbose_name=u'Sous-titre')
    theme = models.CharField(max_length=100, verbose_name=u'Thème')
    body = HTMLField(verbose_name=u'Contenu')
    image = models.ImageField(upload_to='news_news', verbose_name=u'Image')
    
    link1 = models.URLField(blank=True, verbose_name=u'Lien 1')
    link2 = models.URLField(blank=True, verbose_name=u'Lien 2')
    link3 = models.URLField(blank=True, verbose_name=u'Lien 3')
    
    class Meta:
        verbose_name = u'Actualité'
        verbose_name_plural = u'Actualités'