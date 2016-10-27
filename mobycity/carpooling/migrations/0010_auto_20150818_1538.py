# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpooling', '0009_auto_20150818_1034'),
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
            name='arrival_date_time',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='carpool',
            name='departure_date_time',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
