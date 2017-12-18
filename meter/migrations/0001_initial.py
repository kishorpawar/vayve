# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-16 16:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter_id', models.IntegerField(unique=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'vv_meter',
            },
        ),
        migrations.CreateModel(
            name='MeterLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_id', models.BigIntegerField()),
                ('event_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('C', 'connected'), ('D', 'disconnected')], default='D', max_length=1)),
                ('meter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meter_logs', to='meter.Meter')),
            ],
            options={
                'db_table': 'vv_meter_log',
            },
        ),
    ]
