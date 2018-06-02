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

	def get(self, request, format=None):
		start = None
		result = []
		meter = request.query_params.get("meter")
		if meter:
			meter_obj = Meter.objects.get(meter_id=meter)
			logs = MeterLog.objects \
							.filter(meter=meter_obj) \
							.order_by('sequence_id')
			for log in logs:
				if log.status == "Connected":
					if start is None:
					    start = log.event_date
				else:
					result.append(
						{
							"connected_time" : start, 
							"disconnected_time" : log.event_date,
							"sequence_id" : log.sequence_id
						})
					start = None
		else:
			result = """Please try using following format. merters/?meter=<meter_id>"""
					
		return Response(result, status=200)
