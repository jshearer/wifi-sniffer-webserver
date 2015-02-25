from django.contrib import admin
from models import *

# Register your models here.
admin.site.register(Host)
admin.site.register(Recording)
admin.site.register(Transmitter)
admin.site.register(Receiver)
admin.site.register(Location)
admin.site.register(WifiSettings)
admin.site.register(CalculatedPosition)