# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpooling', '0015_auto_20150819_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='accepted',
            field=models.NullBooleanField(default=False),
            preserve_default=True,
        ),
    ]
