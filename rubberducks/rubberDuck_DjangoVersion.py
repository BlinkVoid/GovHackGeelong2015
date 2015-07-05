from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
#from pyramid.view import view_config
from main import *
from track import *

#main page
def main_page(request):
	m = mainPage()
	return Response(m.content)
def track_page(request):
	t = trackPage(request)
	t.constructPage()
	return Response(t.content)
if __name__ == '__main__':
	config = Configurator()
	config.add_route('main', '/rubberduck/main')
	config.add_view(main_page, route_name='main')
	config.add_route('track', '/rubberduck/main/track')
	config.add_view(track_page, route_name='track')
	
	
	app = config.make_wsgi_app()
	server = make_server('0.0.0.0', 8080, app)
	server.serve_forever()
	