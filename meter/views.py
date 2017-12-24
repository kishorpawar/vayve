# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q, Count, When, Case

from rest_framework import viewsets

from meter.serializers import MeterSerializer, MeterLogSerializer
from meter.models import Meter, MeterLog, CONNECTION_STATUS

# Create your views here.

class MeterViewSet(viewsets.ModelViewSet):
	"""
		API endpoint that returns Meter connection status 
	"""

	queryset = Meter.objects.all()
	serializer_class = MeterSerializer
	
	def get_queryset(self):
	    qs = super(MeterViewSet, self).get_queryset()
	    qs = qs.annotate(
	    		# connected = Case(When(status = 'C', then='event_date')),
	    		# # disconnected = Case(When(status = 'D', then='event_date'))
	    		connected = Count('meter_logs__status'),
	    		disconnected = Count('meter_logs__status')
	    	)	
	    return qs
	
class MeterLogViewSet(viewsets.ModelViewSet):
	queryset = MeterLog.objects.all()
	serializer_class = MeterLogSerializer
