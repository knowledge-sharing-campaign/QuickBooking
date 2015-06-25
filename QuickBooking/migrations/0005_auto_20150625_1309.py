# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuickBooking', '0004_busroute_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timing',
            old_name='arrival',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='timing',
            name='depart',
        ),
    ]
