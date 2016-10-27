# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpooling', '0014_auto_20150819_1757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='applicant',
            new_name='subscriber',
        ),
    ]
