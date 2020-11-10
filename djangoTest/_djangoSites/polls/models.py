from django.db import models

class Device(models.Model):
	device_name = models.CharField(max_length=20)
	device_datetime = models.DateTimeField('device datetime')
	device_last_updated = models.DateTimeField('device last updated')
	uptime = models.IntegerField(default=0)
	boot_version_number = models.CharField(max_length=20)
	os_version_number = models.CharField(max_length=20)
	assets_page = models.CharField(max_length=200) 
	serial = models.CharField(max_length=24) ###################
	ethernet_ip = models.CharField(max_length=20) ##############
	model = models.CharField(max_length=10)
	mac = models.CharField(max_length=20)
	video_mode = models.CharField(max_length=20)
	def __str__(self):
		return self.device_name	

class Firmware(models.Model):
	firmware_name = models.CharField(max_length=20)
	firmware_page = models.CharField(max_length=200) 
	def __str__(self):
		return self.firmware_name	

class Snapshot(models.Model):
	device_name = models.CharField(max_length=20)
	snapshot_datetime = models.DateTimeField('date published')
	snapshot_page = models.CharField(max_length=200) 
	def __str__(self):
		return self.device_name + " : " + str(self.snapshot_datetime)
