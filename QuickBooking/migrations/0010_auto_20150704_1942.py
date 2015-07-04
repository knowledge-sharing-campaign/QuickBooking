# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuickBooking', '0009_auto_20150704_1935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seat',
            old_name='number',
            new_name='seat_id',
        ),
    ]
