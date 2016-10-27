# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carpool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departure_latitude', models.FloatField()),
                ('departure_longitude', models.FloatField()),
                ('arrival_latitude', models.FloatField()),
                ('arrival_longitude', models.FloatField()),
                ('frequency', models.CharField(max_length=3, choices=[(b'OCC', b'Occasional'), (b'REG', b'Regular')])),
                ('departure_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('departure_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('arrival_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('arrival_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('seats_number', models.PositiveSmallIntegerField()),
                ('comment', models.TextField()),
                ('global_price', models.PositiveSmallIntegerField()),
                ('organizer', models.ForeignKey(related_name='carpooling_organizer', to=settings.AUTH_USER_MODEL)),
                ('participant', models.ManyToManyField(related_name='carpooling_participant', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
