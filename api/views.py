from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from models import Host, Receiver, WifiSettings, Location, Recording, Transmitter, CalculatedPosition
from serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



class HostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hosts to be viewed or edited.
    """
    queryset = Host.objects.all()
    serializer_class = HostSerializer


class ReceiverViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Receiver.objects.all()
    serializer_class = ReceiverSerializer

class WifiSettingsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hosts to be viewed or edited.
    """
    queryset = WifiSettings.objects.all()
    serializer_class = WifiSettingsSerializer


class RecordingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Recording.objects.all()
    serializer_class = RecordingSerializer

class TransmitterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hosts to be viewed or edited.
    """
    queryset = Transmitter.objects.all()
    serializer_class = TransmitterSerializer


class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class CalculatedPositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hosts to be viewed or edited.
    """
    queryset = CalculatedPosition.objects.all()
    serializer_class = CalculatedPositionSerializer
