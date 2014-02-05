from django.conf.urls import patterns, include, url
from redWine.views import home  
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    #(r'accounts/login/',include(admin.site.urls)),
    url (r'^$', home),
)