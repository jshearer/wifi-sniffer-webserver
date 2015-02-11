from django.contrib.auth.models import User, Group
from rest_framework import serializers

from models import Host, Receiver, WifiSettings, Location, Recording, Transmitter, CalculatedPosition


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')



class ReceiverSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Receiver
		fields = ('host', 'mac_addr', 'x', 'y', 'z')

class HostSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Host
		fields = ('name', 'device_uid', 'location')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Location
		fields = ('name', 'wifi_settings')
		
class RecordingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Recording
		fields = ('receiver', 'rssi', 'data', 'transmitter', 'receiver', 'time')

class TransmitterSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Transmitter
		fields = ('mac_addr', 'name')

class CalculatedPositionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = CalculatedPosition
		fields = ('time', 'transmitter', 'uncertainty', 'x', 'y', 'z')

class WifiSettingsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = WifiSettings
		fields = ('enabled', 'ESSID', 'security', 'ip', 'key', 'hidden')

