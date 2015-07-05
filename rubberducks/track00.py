from static import popEn
class trackPage():
	def __init__(self, request):
		self.request = request
		self.value = self.request.GET
		self.content= ('''
			<!DOCTYPE html>
			<html>
				<head>
					<meta></meta>

					<!--v0.3-getting the form updated according to the drag drop pin-->

					<title>Rubber Duck - follow the pollution</title>
				</head>
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
		testLon = ("Lat: " + self.value["lat"] + " ")
		testLat = ("Lng: " + self.value["lng"] + " ")
		self.content += testLon
		self.content += testLat
		self.content += ("""</p>
						</div></div>
						<div class="subp_bottom">
							<input />
						</div>
					</div>
				</body>
			<html>
		""")