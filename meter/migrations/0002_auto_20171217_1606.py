# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-17 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meter',
            name='meter_id',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
