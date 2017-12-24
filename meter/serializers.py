from meter.models import Meter, MeterLog

from rest_framework import serializers



class MeterLogSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = MeterLog
		fields = ('sequence_id', 'status', 'event_date')


class MeterSerializer(serializers.HyperlinkedModelSerializer):

	connected = serializers.IntegerField()
	disconnected = serializers.IntegerField()
	meter_logs = MeterLogSerializer(many = True)

	class Meta:
		model = Meter
		fields = ('url', 'meter_id', 'name', 'connected', 'disconnected', 'meter_logs',)



