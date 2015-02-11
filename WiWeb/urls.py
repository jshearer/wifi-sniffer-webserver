from django.conf.urls import url, include
from rest_framework_bulk.routes import BulkRouter
from api import views

router = BulkRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

router.register(r'hosts', views.HostViewSet)
router.register(r'receivers', views.ReceiverViewSet)
router.register(r'transmitters', views.TransmitterViewSet)
router.register(r'wifisettings', views.WifiSettingsViewSet)
router.register(r'recordings', views.RecordingViewSet)
router.register(r'locations', views.LocationViewSet)
router.register(r'calculatedpositions', views.CalculatedPositionViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]