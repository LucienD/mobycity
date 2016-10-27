from django.conf.urls import patterns, url

from contact import views


urlpatterns = patterns(
    '',
    url(r'^$', views.contact_form, name='contact_form'),
)