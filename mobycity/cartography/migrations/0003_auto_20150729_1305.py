# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cartography', '0002_pointofinterest_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointofinterest',
            name='description',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True),
            preserve_default=True,
        ),
    ]
