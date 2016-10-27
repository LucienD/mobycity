from django.contrib import admin
from django.forms.widgets import TextInput

from django_google_maps.widgets import GoogleMapsAddressWidget
from django_google_maps.fields import AddressField, GeoLocationField

from cartography import models


class CategoryAdmin(admin.ModelAdmin):
    ordering = ['name']
    
admin.site.register(models.Category, CategoryAdmin)


class PointOfInterestAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'address')
    ordering = ['category', 'name']
    
    formfield_overrides = {
        AddressField: {'widget': GoogleMapsAddressWidget},
        GeoLocationField: {'widget': TextInput(attrs={'readonly': 'readonly'})},
    }

admin.site.register(models.PointOfInterest, PointOfInterestAdmin)