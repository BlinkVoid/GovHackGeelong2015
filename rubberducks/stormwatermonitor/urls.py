from django.conf.urls import url
from . import views
#this is subdirectory level urls
urlpatterns = [
	#ex: /stormwatermonitor
	url(r'^$', views.main, name = 'main'),
	#ex: /stormwatermonitor/main
	url(r'^main$', views.main, name='main'),
	#url('/', views.main, name='main'),
	url(r'^track$', views.track, name='track'),
]

