from static import map
from static import htmltemplate
class mainPage():
	def __init__(self):
		self.mapScript = map.api
		self.HTML_o = '''
		<!DOCTYPE html>
		<html>
		'''
		self.HTML_c = "</html>"
		self.head= htmltemplate.header
		self.head += self.mapScript
		self.head += ('''
				<!--v0.3-getting the form updated according to the drag drop pin-->

				<title>Mighty Ducks Storm-water Tracker - follow the pollution</title>
			</head>
		''')
		self.body = htmltemplate.body
		self.body += ("""
				<div id="info">
				</div>
				</div>
			</div>

    </div><!-- /.container -->
			</body>""")
		self.content= self.HTML_o + self.head + self.body + self.HTML_c
'''
changeLog:
need to be awake of id="googleMap" tag, where the height and width css must be specified for the map to show within the window
'''