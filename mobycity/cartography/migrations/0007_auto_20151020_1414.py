# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cartography', '0006_auto_20151020_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointofinterest',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='image',
            field=models.ImageField(upload_to=b'cartography_pointOfInterest', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='opening_hours',
            field=models.CharField(max_length=254, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='phone',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='website',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
