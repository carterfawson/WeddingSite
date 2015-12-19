from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'rsvp_app.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rsvp$', 'rsvp_app.views.rsvp', name='rsvp'),
]
