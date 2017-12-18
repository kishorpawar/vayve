# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

CONNECTION_STATUS = (
	('C', 'connected'),
	('D', 'disconnected')
	)


class Meter(models.Model):
	meter_id = models.CharField(unique = True, max_length=20)
	name = models.CharField(max_length = 50, blank = True, null = True)

	class Meta:
		db_table = 'vv_meter'

		def __str__(self):
			return self.name


class MeterLog(models.Model):
	meter = models.ForeignKey(Meter, related_name='meter_logs')
	sequence_id = models.BigIntegerField()
	event_date = models.DateTimeField(blank = True, null = True)
	status = models.CharField(max_length = 1, choices = CONNECTION_STATUS, default='D')

	class Meta:
		db_table = 'vv_meter_log'

