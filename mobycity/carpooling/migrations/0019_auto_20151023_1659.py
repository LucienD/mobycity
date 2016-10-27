# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpooling', '0018_auto_20151023_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carpool',
            name='arrival_date',
        ),
        migrations.RemoveField(
            model_name='carpool',
            name='arrival_time',
        ),
        migrations.RemoveField(
            model_name='carpool',
            name='departure_date',
        ),
        migrations.RemoveField(
            model_name='carpool',
            name='departure_time',
        ),
        migrations.AddField(
            model_name='carpool',
            name='occ_arrival_datetime',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='carpool',
            name='occ_departure_datetime',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='carpool',
            name='reg_arrival_time',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='carpool',
            name='reg_departure_time',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
