# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PointOfInterest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', django_google_maps.fields.AddressField(max_length=100)),
                ('geolocation', django_google_maps.fields.GeoLocationField(max_length=100, blank=True)),
                ('category', models.ForeignKey(to='cartography.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
