# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carpooling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpool',
            name='arrival_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='arrival_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='departure_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='departure_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
