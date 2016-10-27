#coding:utf-8

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(null=True, blank=True, upload_to='user_profile_userProfile', verbose_name='Photo')
    phone = models.CharField(blank=True, max_length=15, verbose_name=u'Téléphone')