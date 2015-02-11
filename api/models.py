from django.db import models
from jsonfield import JSONField

# Create your models here.

class Host(models.Model):
	name = models.CharField(max_length=400)
	device_uid = models.CharField(max_length=100)
	location = models.ForeignKey("Location")

	def __unicode__(self):
		return "%s at %s"%(self.name, self.location)

class Receiver(models.Model):
	host = models.ForeignKey("Host")
	mac_addr = models.CharField(max_length=100)
	x = models.FloatField()
	y = models.FloatField()
	z = models.FloatField()

	def __unicode__(self):
		return "%s at %s"%(self.mac_addr,self.host)

class Location(models.Model):
	name = models.CharField(max_length=100)
	wifi_settings = models.ForeignKey("WifiSettings")

	def __unicode__(self):
		return self.name

class WifiSettings(models.Model):
	enabled = models.BooleanField(default=True)
	ESSID = models.CharField(max_length=100)
	security = models.CharField(max_length=20, default="none")
	ip = models.CharField(max_length=100, default="dhcp")
	key = models.CharField(max_length=400, null=True)
	hidden = models.BooleanField(default=False)

	def __unicode__(self):
		return "ESSID: %s, Security: %s"%(self.ESSID, self.security)

class Recording(models.Model):
	receiver = models.ForeignKey("Receiver")
	rssi = models.FloatField()
	data = models.CharField(max_length=1000, null=True)
	transmitter = models.ForeignKey("Transmitter")
	receiver = models.ForeignKey("Receiver")
	time = models.DateTimeField()

class Transmitter(models.Model):
	mac_addr = models.CharField(max_length=100)
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class CalculatedPosition(models.Model):
	time = models.DateTimeField()
	transmitter = models.ForeignKey("Transmitter")
	uncertainty = models.FloatField()
	x = models.FloatField()
	y = models.FloatField()
	z = models.FloatField()

	def __unicode__(self):
		return "(%f, %f, %f) {%s}"%(self.x, self.y, self.z, self.transmitter)