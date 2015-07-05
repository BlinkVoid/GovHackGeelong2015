from static import popEn3
from static import map_track
from static import htmltemplate
from static import spill

class trackPage():
#Lng, Lat in request format
	def __init__(self, request):
		self.request = request
		self.value = self.request.GET
		self.result = []
		#self.result = popEn.feedPip(str(self.value["lat"]) + " " + str(self.value["lng"]))
		#self.result = popEn2.feedPip2nd(self.result)
		self.result = popEn3.feedPip(str(self.value["lat"]) + " " + str(self.value["lng"]))
		self.content= ""

	
	def processResult(self):
		index = 0
		nodeName = []
		#position = []
		positionDic = {}
		for i in range(len(self.result)):
			nodeName.append("node" + str(i))
		while index < len(nodeName):
			positionDic[nodeName[index]] = [str(self.result[index*2]), str(self.result[index*2 + 1])]
			index += 1
		return (positionDic, nodeName)
		
	def constructPage(self):
		html_o =('''
			<!DOCTYPE html>
			<html>''')
		head = htmltemplate.header
		head += map_track.map2(self.result, self.value).api
		head += ('''
					<title>Mighty Ducks Storm-water Tracker - follow the pollution</title>
				</head>
		''')
		body = htmltemplate.body
		#there will be two pairs of coordinates that correspond to two end points of one section of storm drain pips. 
		#use the coordinates to map out poly line in google maps.

		#testLat = ("Lat: " + self.result[0] + " ")
		#testLng = ("Lng: " + self.result[1] + " ")
		#body += testLng
		#body += testLat
		body += spill.spill(str(self.value["spill"]))
		body += ("""
						
				</div>
			</div>

    </div><!-- /.container -->
				
				<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
				<script src="/static/js/bootstrap.min.js"></script>
			</body>""")
		html_c = "</html>"
		self.content = html_o + head + body + html_c