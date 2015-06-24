# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=200)),
                ('make', models.CharField(max_length=100)),
                ('capacity', models.IntegerField(default=50)),
            ],
        ),
        migrations.CreateModel(
            name='BusRoute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cost', models.IntegerField(default=1000)),
                ('bus', models.ForeignKey(to='QuickBooking.Bus')),
            ],
        ),
        migrations.CreateModel(
            name='BusStop',
            fields=[
                ('stopname', models.CharField(max_length=100, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='BusType',
            fields=[
                ('type', models.CharField(max_length=20, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('Phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Timing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('depart', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('arrival', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='busroute',
            name='dest',
            field=models.ForeignKey(related_name='destination', to='QuickBooking.BusStop'),
        ),
        migrations.AddField(
            model_name='busroute',
            name='src',
            field=models.ForeignKey(related_name='source', to='QuickBooking.BusStop'),
        ),
        migrations.AddField(
            model_name='busroute',
            name='timing',
            field=models.ForeignKey(to='QuickBooking.Timing'),
        ),
        migrations.AddField(
            model_name='bus',
            name='type',
            field=models.ForeignKey(to='QuickBooking.BusType'),
        ),
    ]
