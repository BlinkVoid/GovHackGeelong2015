from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
#this is top level topology urls, placed in root directory
#points to app stormwatermonitor with its urls definition

urlpatterns = [
    url(r'^stormwatermonitor/', include('stormwatermonitor.urls')),
]

urlpatterns += staticfiles_urlpatterns()