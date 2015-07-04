from static import map

class mainPage():
	def __init__(self):
		self.mapScript = map.api
		self.HTML_o = '''
		<!DOCTYPE html>
		<html>
		'''
		self.HTML_c = "</html>"
		self.head='''
			<head>
				<meta></meta>
				<script src="http://maps.googleapis.com/maps/api/js"></script>
				<!--Deakin Lng -38.144061, Lat 144.360345-->'''
		self.head += self.mapScript
		self.head += ('''
				<!--v0.3-getting the form updated according to the drag drop pin-->

				<title>Rubber Duck - follow the pollution</title>
			</head>
		''')
		self.body='''
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
					</div>
					<div class="subp_bottom">
						<p>After selecting your location, click to button below</p>
						<form action="track" method="GET">
							Latitude: <input type="text" id= "lat" class="coordiantes" value="Drag the pin" name="lat"><br>
							Longitude: <input type="text" id="lng" class="coordinates" value="Drag the pin" name="lng"><br>
							
							
							<input type="submit" value="Submit">
						</form>
					</div>
				</div>
			</body>
		'''
		self.content= self.HTML_o + self.head + self.body + self.HTML_c
'''
changeLog:
need to be awake of id="googleMap" tag, where the height and width css must be specified for the map to show within the window
'''