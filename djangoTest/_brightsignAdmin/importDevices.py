#importDevices.py
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
from django.core.management import execute_from_command_line

import django
#django.setup()
from polls.models import Device

devicesPath = "in_device_old.txt"
def getFileContents(devicesPath):
	devices = []
	with open(devicesPath, 'rt') as fileIn:
		for lineF in fileIn:
			if ',' not in lineF :
				print("Encountered stopping input: " + lineF)
				break
			if  len(lineF) == 0 or lineF[0] == "#":
				#print("Encountered skipping input: " + lineF)
				continue
			device = lineF.split(',')
			devices.append(device)
	return devices

print("Getting device info from file...")
devices = getFileContents(devicesPath)


print("All devices in db now:...")
for d1 in Device.objects.all():
	print(d1)

print("Adding devices to db...")
for device in devices:
	ip = device[0]
	name = device[1]
	serial = device[2].rstrip(None)
	d = Device(device_name = name, serial = serial, ethernet_ip = ip)
	d.save()

print("All devices in db now (deleting as we go):...")
for d1 in Device.objects.all():
	print(d1)
	d1.delete()

print("All devices in db now:...")
for d1 in Device.objects.all():
	print(d1)

"""
execute_from_command_line('print("test")')
until this can be run from command line:
python manage.py shell

from django.utils import timezone
from polls.models import Device

d = Device(device_name = 'ADM2', serial = 'D1E91C001255', ethernet_ip = '10.137.72.35', device_datetime=timezone.now(), device_last_updated=timezone.now())
d.save()

for d1 in Device.objects.all(): print(d1)
for d1 in Device.objects.all(): d1.delete()

django.utils.timezone.now()
"""