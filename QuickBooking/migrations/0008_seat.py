# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuickBooking', '0007_busroute_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('occupied', models.BooleanField(default=False)),
                ('number', models.IntegerField()),
                ('seat_type', models.ForeignKey(to='QuickBooking.BusType')),
            ],
        ),
    ]
