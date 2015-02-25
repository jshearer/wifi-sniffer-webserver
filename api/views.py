from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import filters
from rest_framework_bulk import BulkModelViewSet

from models import Host, Receiver, WifiSettings, Location, Recording, Transmitter, CalculatedPosition
from serializers import *


class UserViewSet(BulkModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(BulkModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class HostViewSet(BulkModelViewSet):
    """
    API endpoint that allows hosts to be viewed or edited.
    """
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    filter_fields = ('name', 'device_uid', 'location', 'enabled')

class ReceiverViewSet(BulkModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Receiver.objects.all()
    serializer_class = ReceiverSerializer
    filter_fields = ('host', 'mac_addr', 'channel', 'x', 'y', 'z')

class WifiSettingsViewSet(BulkModelViewSet):
    """
    API endpoint that allows hosts to be viewed or edited.
    """
    queryset = WifiSettings.objects.all()
    serializer_class = WifiSettingsSerializer
    filter_fields = ('enabled', 'ESSID', 'security', 'ip', 'key', 'hidden')

class RecordingViewSet(BulkModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Recording.objects.all()
    serializer_class = RecordingSerializer
    filter_fields = ('rssi', 'data', 'transmitter', 'receiver', 'time')

class TransmitterViewSet(BulkModelViewSet):
    """
    API endpoint that allows hosts to be viewed or edited.
    """
    queryset = Transmitter.objects.all()
    serializer_class = TransmitterSerializer
    filter_fields = ('mac_addr', 'name')


class LocationViewSet(BulkModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_fields = ('name', 'wifi_settings')

class CalculatedPositionViewSet(BulkModelViewSet):
    """
    API endpoint that allows hosts to be viewed or edited.
    """
    queryset = CalculatedPosition.objects.all()
    serializer_class = CalculatedPositionSerializer
    filter_fields = ('time', 'transmitter', 'uncertainty', 'x', 'y', 'z')
