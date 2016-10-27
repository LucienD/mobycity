from django.conf.urls import patterns, url

from user_profile import views


urlpatterns = patterns(
    '',
    url(r'^change-picture/', views.change_picture, name='user_profile_change_picture'),
    url(r'^change-phone/', views.change_phone, name='user_profile_change_phone'),
    url(r'^$', views.index, name='user_profile_index'),
)