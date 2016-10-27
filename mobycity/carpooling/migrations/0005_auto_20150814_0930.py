# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carpooling', '0004_auto_20150813_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpool',
            name='arrival_date',
            field=models.DateField(default=django.utils.timezone.now, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='departure_date',
            field=models.DateField(default=django.utils.timezone.now, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='global_price',
            field=models.PositiveSmallIntegerField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
