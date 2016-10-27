# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartography', '0005_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointofinterest',
            name='image',
            field=models.ImageField(default='', upload_to=b'cartography_pointOfInterest'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pointofinterest',
            name='opening_hours',
            field=models.CharField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pointofinterest',
            name='phone',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pointofinterest',
            name='website',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
