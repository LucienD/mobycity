# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpooling', '0017_auto_20150907_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carpool',
            name='global_price',
        ),
        migrations.AddField(
            model_name='carpool',
            name='free',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
