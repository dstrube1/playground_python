from django.db import models

class Device(models.Model):
	device_name = models.CharField(max_length=20)
	device_datetime = models.DateTimeField('device datetime')
	device_last_updated = models.DateTimeField('device last updated')
	uptime = models.IntegerField(default=0)
	boot_version_number = models.CharField(max_length=20, default='')
	os_version_number = models.CharField(max_length=20, default='')
	assets_page_url = models.CharField(max_length=200, default='') 
	serial = models.CharField(max_length=24) ###################
	ethernet_ip = models.CharField(max_length=20) ##############
	model = models.CharField(max_length=10, default='')
	mac = models.CharField(max_length=20, default='')
	video_mode = models.CharField(max_length=20, default='')
	company = models.CharField(max_length=20, default='')
	def __str__(self):
		return self.device_name	

class Firmware(models.Model):
	firmware_name = models.CharField(max_length=20, default='')
	firmware_url = models.CharField(max_length=200, default='')
	def __str__(self):
		return self.firmware_name	

class Snapshot(models.Model):
	#device_name = models.CharField(max_length=20)
	device = models.ForeignKey(Device, on_delete=models.CASCADE)
	snapshot_datetime = models.DateTimeField('snapshot date')
	snapshot_url = models.CharField(max_length=200, default='') 
	snapshot_path = models.CharField(max_length=200, default='') 
	def __str__(self):
		return self.device.device_name + " : " + str(self.snapshot_datetime)
