# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuickBooking', '0003_remove_busroute_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='busroute',
            name='cost',
            field=models.IntegerField(default=1000),
        ),
    ]
