# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartography', '0003_auto_20150729_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointofinterest',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
