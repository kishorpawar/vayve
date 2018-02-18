# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q, Count, When, Case

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from meter.serializers import MeterSerializer, MeterLogSerializer
from meter.models import Meter, MeterLog, CONNECTION_STATUS

# Create your views here.

class ListMeterLogs(APIView):
	"""
		API endpoint that returns Meter connection status 
	"""

	# queryset = Meter.objects.all()
	# serializer_class = MeterSerializer
	
	# def get_queryset(self):
	#     qs = super(MeterViewSet, self).get_queryset()
	#     qs = qs.annotate(
	#     		# connected = Case(When(status = 'C', then='event_date')),
	#     		# # disconnected = Case(When(status = 'D', then='event_date'))
	#     		connected = Count('meter_logs__status'),
	#     		disconnected = Count('meter_logs__status')
	#     	)	
	#     return qs

	def get(self, request, format=None):
		start = None
		result = []
		meter = request.query_params.get("meter")
		meter_obj = Meter.objects.get(meter_id=meter)
		logs = MeterLog.objects \
						.filter(meter=meter_obj) \
						.order_by('sequence_id')
		for log in logs:
			if log.status == "Connected":
				if start is None:
				    start = log.event_date
			else:
				result.append([start, log.event_date])
				start = None
		return Response(result, status=200)
	
class MeterLogViewSet(viewsets.ModelViewSet):
	queryset = MeterLog.objects.all()
	serializer_class = MeterLogSerializer
