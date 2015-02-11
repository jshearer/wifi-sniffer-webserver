from django.contrib.auth.models import User, Group
from rest_framework import viewsets
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


class ReceiverViewSet(BulkModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Receiver.objects.all()
    serializer_class = ReceiverSerializer

class WifiSettingsViewSet(BulkModelViewSet):
    """
    API endpoint that allows hosts to be viewed or edited.
    """
    queryset = WifiSettings.objects.all()
    serializer_class = WifiSettingsSerializer


class RecordingViewSet(BulkModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Recording.objects.all()
    serializer_class = RecordingSerializer

class TransmitterViewSet(BulkModelViewSet):
    """
    API endpoint that allows hosts to be viewed or edited.
    """
    queryset = Transmitter.objects.all()
    serializer_class = TransmitterSerializer


class LocationViewSet(BulkModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class CalculatedPositionViewSet(BulkModelViewSet):
    """
    API endpoint that allows hosts to be viewed or edited.
    """
    queryset = CalculatedPosition.objects.all()
    serializer_class = CalculatedPositionSerializer
