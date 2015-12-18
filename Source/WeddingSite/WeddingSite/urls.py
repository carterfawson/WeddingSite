from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'WeddingSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('rsvp_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
