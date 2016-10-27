# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpooling', '0008_auto_20150818_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpool',
            name='frequency',
            field=models.CharField(default=b'OCC', max_length=3, choices=[(b'OCC', b'Occasional'), (b'REG', b'Regular')]),
            preserve_default=True,
        ),
    ]
