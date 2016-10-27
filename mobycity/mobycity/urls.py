from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls import patterns
from django.conf.urls.static import static
from django.contrib import admin

# admin.autodiscover() # Not required for Django 1.7.x+

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mobycity.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', include('news.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^cartography/', include('cartography.urls')),
    url(r'^carpooling/', include('carpooling.urls')),
    url(r'^profile/', include('user_profile.urls')),
    url(r'^', include('cms.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
