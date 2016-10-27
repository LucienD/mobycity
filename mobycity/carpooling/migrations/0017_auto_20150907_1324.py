# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpooling', '0016_auto_20150820_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='accepted',
            field=models.NullBooleanField(default=None),
            preserve_default=True,
        ),
    ]
