# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuickBooking', '0008_seat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='id',
        ),
        migrations.AlterField(
            model_name='bustype',
            name='type',
            field=models.CharField(max_length=5, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='seat',
            name='number',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seat_type',
            field=models.CharField(max_length=5, primary_key=True),
        ),
    ]
