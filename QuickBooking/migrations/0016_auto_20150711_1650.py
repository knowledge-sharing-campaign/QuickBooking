# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuickBooking', '0015_seat_bus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='seat_id',
            field=models.CharField(max_length=20, serialize=False, primary_key=True),
        ),
    ]
