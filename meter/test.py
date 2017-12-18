from meter.models import Meter, MeterLog
import csv, os, datetime

def read_files(path):
	for root, subF, files in os.walk(path):
		for file in files:
			filepath = os.path.join(root,file)
			print filepath
			if filepath.endswith('.csv'):
				with open(filepath, 'rb') as csvfile:
					csvreader = csv.reader(csvfile, delimiter=',')
					next(csvreader, None)
					for row in csvreader:
						meter = save_meter(row[1])
						save_meter_log(row, meter)


def save_meter(meter):
	print meter
	meter, created = Meter.objects.get_or_create(
		meter_id = meter,
		name = meter
		)
	return meter

def save_meter_log(row, meter):
	ml = MeterLog.objects.create(
		meter = meter,
		sequence_id = row[0],
		event_date = datetime.datetime.strptime(row[2],'%d-%m-%Y %H:%M'),	
		status = row[3],
		)
	ml.save()