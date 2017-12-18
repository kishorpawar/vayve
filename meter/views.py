# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from meter.serializers import MeterSerializer, MeterLogSerializer
from meter.models import Meter, MeterLog

# Create your views here.

class MeterViewSet(viewsets.ModelViewSet):
	"""
		API endpoint that returns Meter connection status 
	"""

	queryset = Meter.objects.all()
	serializer_class = MeterSerializer
	
class MeterLogViewSet(viewsets.ModelViewSet):
	queryset = MeterLog.objects.all()
	serializer_class = MeterLogSerializer