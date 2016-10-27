# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carpooling', '0006_auto_20150818_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpool',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpoolapplication',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpoolapplication',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True),
            preserve_default=True,
        ),
    ]
