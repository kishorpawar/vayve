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
        def get_queryset(self):       
            qs = super(MeterViewSet, self).get_queryset()
#            qs = qs.filter()
            return qs 
	
class MeterLogViewSet(viewsets.ModelViewSet):
	queryset = MeterLog.objects.all()
	serializer_class = MeterLogSerializer
