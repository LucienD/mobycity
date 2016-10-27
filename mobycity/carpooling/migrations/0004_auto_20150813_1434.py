# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('carpooling', '0003_auto_20150813_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpool',
            name='participant',
            field=models.ManyToManyField(related_name='carpooling_participant', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
