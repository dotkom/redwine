from django.conf.urls import include
from redwine.views import redwine_home, redwine_com, redwine_top
from django.contrib import admin
from django.urls import re_path

admin.autodiscover()

urlpatterns = [
    re_path(r"^top/$", redwine_top),
    re_path(r"^([\w-]+)/$", redwine_com),
    re_path(r"^$", redwine_home),
]
