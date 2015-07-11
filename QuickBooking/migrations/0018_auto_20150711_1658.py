# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('QuickBooking', '0017_auto_20150711_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='Ar_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='bus',
            name='dep_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='timing',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, blank=True),
        ),
    ]
