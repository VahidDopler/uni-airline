from django.contrib import admin

from .models import Flight, Airport, Airplane, Country

admin.site.register(Flight)
admin.site.register(Country)
admin.site.register(Airport)
admin.site.register(Airplane)
# Register your models here.
