# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartography', '0007_auto_20151020_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='placeholder_image',
            field=models.ImageField(default='', upload_to=b'cartography_category'),
            preserve_default=False,
        ),
    ]
