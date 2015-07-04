# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuickBooking', '0010_auto_20150704_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='seat_type',
            field=models.CharField(max_length=10, primary_key=True),
        ),
    ]
