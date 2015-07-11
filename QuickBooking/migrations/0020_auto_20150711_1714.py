# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuickBooking', '0019_auto_20150711_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bus',
            old_name='Ar_time',
            new_name='arrive_time',
        ),
        migrations.RenameField(
            model_name='bus',
            old_name='dep_time',
            new_name='departure_time',
        ),
    ]
