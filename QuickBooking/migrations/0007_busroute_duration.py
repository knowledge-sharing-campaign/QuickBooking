# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuickBooking', '0006_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='busroute',
            name='duration',
            field=models.CharField(default=6, max_length=10),
        ),
    ]
