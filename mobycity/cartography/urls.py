from django.conf.urls import patterns, url

from cartography import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
)