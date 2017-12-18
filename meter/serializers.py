from meter.models import Meter, MeterLog

from rest_framework import serializers



class MeterLogSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = MeterLog
		fields = ('status', 'event_date')


class MeterSerializer(serializers.HyperlinkedModelSerializer):
	meter_logs = MeterLogSerializer(many = True)
	class Meta:
		model = Meter
		fields = ('url', 'meter_id', 'name', 'meter_logs')



