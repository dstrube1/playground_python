from django.shortcuts import render
from flask import Flask, request, make_response, escape
from django.http import HttpResponse, HttpResponseRedirect
#from django.template import loader
from django.shortcuts import get_object_or_404, render
#from django.http import Http404

from .models import Device
from django.utils import timezone

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

def index(request):
	#return HttpResponse("bsa index")
	allInDB = Device.objects.all()
	#template = loader.get_template('bsa/index.html')
	context = {'allInDB': allInDB,}
	#return HttpResponse(template.render(context, request))
	devices = getFileContents(devicesPath)
	duplicates = ""
	for device in devices:
		ip = device[0]
		name = device[1]
		serial = device[2].rstrip(None)
		foundDuplicate = False
		for dev in allInDB:
			if dev.serial == serial:
				foundDuplicate = True
				duplicates += name + ","
				break
		if foundDuplicate:
			#Skip this one and try the next one
			continue
		d = Device(device_name = name, serial = serial, ethernet_ip = ip, \
			device_datetime = timezone.now(), device_last_updated = timezone.now())
		#this does not check for duplicates
		d.save()

	alert = ""
	"""
	
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
	Note: can use javascript alert:
			script = "" "
			<script><!--alert('Hello')--></script>
	return render(request, 'polls/detail.html', {'question': question})
			"""
	if len(duplicates) > 0:
		alert = "Skipping duplicates: " + duplicates + "; "
	response = alert + "All devices in db: " + str(len(allInDB)) + "; "
	#return HttpResponse(response)
	return render(request, 'bsa/index.html', context)

def getInfo(request, device_id):
	#response = "Info on device id %s." % device_id
	#return HttpResponse(response)
	device = get_object_or_404(Device, pk=device_id)
	return render(request, 'bsa/getInfo.html', {'device':device})

def getSnapshot(request, device_id):
	device = get_object_or_404(Device, pk=device_id)
	
	#TODO: add getSnapshot code here
	try:
		print("request.POST['choice']:")
		print(request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'bsa/getInfo.html', {
           'device':device,
           'error_message': "You didn't select a choice.",})
	
	return HttpResponse("Snapshot on device %s." % escape(device_id))
	#Server error 500:
	#return HttpResponseRedirect(reverse('bsa:snapshotResult', args=(device.id,)))

def snapshotResult(request, device_id):
	device = get_object_or_404(Device, pk=device_id)
	return render(request, 'bsa/snapshotResult.html', {'device': device})

def reboot(request, device_id):
	#return HttpResponse("Rebooting device %s." % device_id)
	#try:
	#	device = Device.objects.get(pk=device_id)
	#except Device.DoesNotExist:
	#	raise Http404("Device does not exist")
	
	device = get_object_or_404(Device, pk=device_id)
	
	#see also:
	#https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/#django.shortcuts.get_list_or_404

	#TODO: add reboot code here

	return render(request, 'bsa/reboot.html', {'device':device})
	
