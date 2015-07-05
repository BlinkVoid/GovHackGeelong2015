class mainPage():
	def __init__(self):
		self.content= ('''
	<!DOCTYPE html>
<html>
	<head>
		<meta></meta>
		<script src="http://maps.googleapis.com/maps/api/js"></script>
		<!--Deakin Lon -38.144061, Lat 144.360345-->
		<script>
			function initialize() {
				var mapProp = {
					center: new google.maps.LatLng(-38.144061, 144.360345),
					zoom: 17,
					mapTypeId: google.maps.MapTypeId.HYBRID
				};
				var map=new google.maps.Map(document.getElementById("googleMap"), mapProp);
			}
			google.maps.event.addDomListener(window, 'load', initialize);
		</script>
		
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
				<p>UserInput</p>
				<form action="">
					Longitude: <input type="text" name="lon"><br>
					Latitude: <input type="text" name= "lat"><br>
					<input type="submit" value="Submit"
				</form>
			</div>
		</div>
	</body>
<html>

	''')