from django.contrib import admin

from .models import Bus, BusType, BusStop, BusRoute, Timing, Seat

admin.site.register(Bus)
admin.site.register(BusType)
admin.site.register(BusStop)
admin.site.register(BusRoute)
admin.site.register(Timing)
admin.site.register(Seat)
