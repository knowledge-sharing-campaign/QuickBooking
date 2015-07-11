# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('QuickBooking', '0018_auto_20150711_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timing',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True),
        ),
    ]
