from django.conf.urls import patterns, url

from carpooling import views


urlpatterns = patterns(
    '',
    url(r'^offer/', views.offer, name='offer'),
    url(r'^search/', views.search, name='search'),
    url(r'^search-result/', views.search_result, name='search-result'),
    url(r'^subscribe/', views.subscribe, name='subscribe'),
    url(r'^user-list-offers/', views.user_list_offers, name='user-list-offers'),
    url(r'^user-cancel-carpool/', views.user_cancel_carpool, name='user-cancel-carpool'),
    url(r'^user-list-subscriptions/', views.user_list_subscriptions, name='user-list-subscriptions'),
    url(r'^user-cancel-subscription/', views.user_cancel_subscription, name='user-cancel-subscription'),
    url(r'^user-accept-or-deny-subscription/', views.user_accept_or_deny_subscription, name='user-accept-or-deny-subscription'),
    url(r'^$', views.search, name='search'),
)