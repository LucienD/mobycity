from django.contrib import admin
from django.forms.widgets import TextInput

from news import models


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'theme', 'publication_datetime')
    readonly_fields = ('creation_datetime', 'update_datetime')
    
admin.site.register(models.News, NewsAdmin)