# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('QuickBooking', '0016_auto_20150711_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='Ar_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='bus',
            name='dep_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
