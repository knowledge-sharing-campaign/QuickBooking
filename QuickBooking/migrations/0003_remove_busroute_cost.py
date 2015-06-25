# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuickBooking', '0002_auto_20150623_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='busroute',
            name='cost',
        ),
    ]
