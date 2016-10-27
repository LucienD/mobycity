# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carpooling', '0013_auto_20150819_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_datetime', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('update_datetime', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('cancelled', models.BooleanField(default=False)),
                ('accepted', models.NullBooleanField()),
                ('applicant', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('carpool', models.ForeignKey(to='carpooling.Carpool')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='carpoolsubscription',
            name='applicant',
        ),
        migrations.RemoveField(
            model_name='carpoolsubscription',
            name='carpool',
        ),
        migrations.DeleteModel(
            name='CarpoolSubscription',
        ),
    ]
