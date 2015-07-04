from django.http import HttpResponse
#sub directory: stormwatermonitor directory level views
# Create your views here.
from main import *
from track import *

def main(request):
	m = mainPage()
	return HttpResponse(m.content)
	
def track(request):
	t = trackPage(request)
	t.constructPage()
	return HttpResponse(t.content)
