# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuickBooking', '0014_auto_20150704_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='bus',
            field=models.ForeignKey(default=None, to='QuickBooking.Bus'),
        ),
    ]
