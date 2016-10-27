# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body',
            field=djangocms_text_ckeditor.fields.HTMLField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to=b'news_news', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='subtitle',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
