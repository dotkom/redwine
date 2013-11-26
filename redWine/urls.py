from django.conf.urls import patterns, include, url
from redWine.views import home  
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    url (r'^$', home),
    # Examples:
    # url(r'^$', 'vinstraff.views.home', name='home'),
    # url(r'^vinstraff/', include('vinstraff.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     #url(r'^admin/', include(admin.site.urls)),
)
