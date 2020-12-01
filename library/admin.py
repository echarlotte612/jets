from django.contrib import admin
from .models import Cryptid, Location, Sighting

admin.site.register(Cryptid)
admin.site.register(Location)
admin.site.register(Sighting)
