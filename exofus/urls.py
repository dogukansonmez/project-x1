from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'subscription.views.home', name='home'),
    url(r'^about$','subscription.views.about', name='about'),
    url(r'^share','subscription.views.share', name='share'),
    url(r'^experience/(?P<id>[1-9]+)$','subscription.views.experiencePage', name='experiencePage'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
    url(r'^logout/','subscription.views.logout_user', name='logout_user'),
)
