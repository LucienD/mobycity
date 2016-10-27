# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carpooling', '0005_auto_20150814_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarpoolApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_date', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('update_date', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('cancelled', models.BooleanField(default=False)),
                ('accepted', models.NullBooleanField()),
                ('applicant', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('carpool', models.ForeignKey(to='carpooling.Carpool')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='carpool',
            name='participant',
        ),
        migrations.AddField(
            model_name='carpool',
            name='cancelled',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='carpool',
            name='creation_date',
            field=models.DateField(default=django.utils.timezone.now, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='carpool',
            name='update_date',
            field=models.DateField(default=django.utils.timezone.now, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carpool',
            name='organizer',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
