from django.contrib.auth.models import User, Group
from rest_framework import serializers

from models import Host, Receiver, WifiSettings, Location, Recording, Transmitter, CalculatedPosition


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('pk', 'url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('pk', 'url', 'name')


class ReceiverSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Receiver
		fields = ('pk', 'url', 'host', 'mac_addr', 'x', 'y', 'z')

class HostSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Host
		fields = ('pk', 'url', 'name', 'device_uid', 'location')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Location
		fields = ('pk', 'url', 'name', 'wifi_settings')
		
class RecordingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Recording
		fields = ('pk', 'url', 'rssi', 'data', 'transmitter', 'receiver', 'time')

class TransmitterSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Transmitter
		fields = ('pk', 'url', 'mac_addr', 'name')

class CalculatedPositionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = CalculatedPosition
		fields = ('pk', 'url', 'time', 'transmitter', 'uncertainty', 'x', 'y', 'z')

class WifiSettingsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = WifiSettings
		fields = ('pk', 'url', 'enabled', 'ESSID', 'security', 'ip', 'key', 'hidden')

