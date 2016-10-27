# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_datetime', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('update_datetime', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('publication_datetime', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('theme', models.CharField(max_length=100)),
                ('body', djangocms_text_ckeditor.fields.HTMLField(blank=True)),
                ('image', models.ImageField(upload_to=b'news_news')),
                ('link1', models.URLField(blank=True)),
                ('link2', models.URLField(blank=True)),
                ('link3', models.URLField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
