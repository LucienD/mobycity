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
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_datetime', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('update_datetime', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('read', models.BooleanField(default=False)),
                ('content', models.CharField(max_length=255)),
                ('recipient', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
