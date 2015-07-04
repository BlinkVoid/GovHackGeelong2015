from static import popEn
from static import popEn2

from static import map_track

class trackPage():
#Lng, Lat in request format
	def __init__(self, request):
		self.request = request
		self.value = self.request.GET
		self.result = []
		self.result = popEn.feedPip(str(self.value["lat"]) + " " + str(self.value["lng"]))
		self.result = popEn2.feedPip2nd(self.result)
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
		head = ('''
				<head>
					<meta></meta>

					<!--v0.3-getting the form updated according to the drag drop pin-->
					<script src="http://maps.googleapis.com/maps/api/js"></script>''')
		head += map_track.map2(self.result).api
		head += ('''
					<title>Rubber Duck - follow the pollution</title>
				</head>
		''')
		body = ('''
				<body>
					<div id='heading'> 
						<p>Rubber Duck XIII - the pollution tracker system</p>
					</div>
					<div class="panel">
						<p>This is the entire map field. divide into three sections</p>
						<div class="subp_left">
						</div>
						<div class="subp_right">
							<div id="googleMap" style="width:500px;height:380px;"></div>
							<div><p>The get response is:  ''')
		#there will be two pairs of coordinates that correspond to two end points of one section of storm drain pips. 
		#use the coordinates to map out poly line in google maps.

		testLat = ("Lat: " + self.result[0] + " ")
		testLng = ("Lng: " + self.result[1] + " ")
		body += testLng
		body += testLat
		body += ("""</p>
						</div></div>
						<div class="subp_bottom">
							<input />
						</div>
					</div>
				</body>""")
		html_c = "</html>"
		self.content = html_o + head + body + html_c