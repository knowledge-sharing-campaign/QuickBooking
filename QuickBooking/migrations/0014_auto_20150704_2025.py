# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuickBooking', '0013_auto_20150704_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busroute',
            name='duration',
            field=models.CharField(default=20, max_length=10),
        ),
        migrations.AlterField(
            model_name='bustype',
            name='type',
            field=models.CharField(max_length=20, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seat_type',
            field=models.CharField(max_length=20),
        ),
    ]
