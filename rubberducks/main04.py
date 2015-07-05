class mainPage():
	def __init__(self):
		self.content= ('''
<!DOCTYPE html>
<html>
	<head>
		<meta></meta>
		<script src="http://maps.googleapis.com/maps/api/js"></script>
		<!--Deakin Lon -38.144061, Lat 144.360345-->
		<script src="map.js"></script>
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
			</div>
			<div class="subp_bottom">
				<p>After selecting your location, click to button below</p>
				<form action="">
					Longitude: <input type="text" id="lon" class="coordinates" value="sthhere"><br>
					Latitude: <input type="text" id= "lat" class="coordiantes" value="sthhere"><br>
					<input type="submit" value="Submit"
				</form>
			</div>
		</div>
	</body>
<html>
	''')