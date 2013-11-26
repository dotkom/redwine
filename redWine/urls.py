from django.conf.urls import patterns, include, url
from redWine.views import home  
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    url (r'^$', home),
)