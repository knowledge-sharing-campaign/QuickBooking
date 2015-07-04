# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuickBooking', '0012_auto_20150704_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bustype',
            name='type',
            field=models.CharField(max_length=10, serialize=False, primary_key=True),
        ),
    ]
