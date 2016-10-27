from django.contrib import admin
from django.forms.widgets import TextInput

from carpooling.models import Carpool, Subscription


class CarpoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'organizer', 'frequency', 'cancelled')

admin.site.register(Carpool, CarpoolAdmin)


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'subscriber', 'carpool', 'cancelled', 'accepted')

admin.site.register(Subscription, SubscriptionAdmin)