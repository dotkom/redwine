from django.conf.urls import patterns, include, url
from redWine.views import redWine_home
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', redWine_home),
    (r'^admin/', include(admin.site.urls)),
    #(r'accounts/login/',include(admin.site.urls)),
    #url (r'^/$', redWine_home),
)