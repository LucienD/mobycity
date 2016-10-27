# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carpooling', '0010_auto_20150818_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carpool',
            name='arrival_date_time',
        ),
        migrations.RemoveField(
            model_name='carpool',
            name='departure_date_time',
        ),
        migrations.AddField(
            model_name='carpool',
            name='arrival_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='carpool',
            name='arrival_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carpool',
            name='departure_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='carpool',
            name='departure_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
