from django.contrib import admin

from .models import Device

admin.site.register(Device)

#Temporary, just to get some values going:
from .models import Firmware
from .models import Snapshot

admin.site.register(Firmware)
admin.site.register(Snapshot)
