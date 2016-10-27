# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpooling', '0011_auto_20150818_2150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carpool',
            old_name='creation_date',
            new_name='creation_datetime',
        ),
        migrations.RenameField(
            model_name='carpool',
            old_name='update_date',
            new_name='update_datetime',
        ),
        migrations.RenameField(
            model_name='carpoolapplication',
            old_name='creation_date',
            new_name='creation_datetime',
        ),
        migrations.RenameField(
            model_name='carpoolapplication',
            old_name='update_date',
            new_name='update_datetime',
        ),
    ]
