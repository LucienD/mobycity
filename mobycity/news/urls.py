from django.conf.urls import patterns, url

from news import views


urlpatterns = patterns(
    '',
    url(r'^list/', views.list, name='list'),
    url(r'^$', views.list, name='list'),
)