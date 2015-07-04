# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuickBooking', '0011_auto_20150704_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='seat_type',
            field=models.ForeignKey(to='QuickBooking.BusType'),
        ),
    ]
