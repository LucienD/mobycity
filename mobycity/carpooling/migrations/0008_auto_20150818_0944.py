# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpooling', '0007_auto_20150818_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpool',
            name='arrival_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='arrival_time',
            field=models.TimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='departure_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='departure_time',
            field=models.TimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='global_price',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
    ]
