from django.conf.urls import include, url
from redwine.views import redwine_home, redwine_com, redwine_top
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^top/$', redwine_top),
    url(r'^(\w+)/$', redwine_com),
    url(r'^$', redwine_home),
    url(r'^admin/', admin.site.urls),
    # (r'accounts/login/',include(admin.site.urls)),
]
