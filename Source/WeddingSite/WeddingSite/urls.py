from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'rsvp_app.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rsvp$', 'rsvp_app.views.rsvp', name='rsvp'),
    url(r'^details$', 'rsvp_app.views.details', name='details'),
    url(r'^about$', 'rsvp_app.views.about', name='about'),
]
