class map2():	
	
	def __init__(self, location):
		self.locationDic = {}
		self.nodeName = []
		#=========================
		(self.locationDic, self.nodeName) = self.readLocation(location)
		print (self.nodeName)
		print (self.locationDic)
		#========================= to be used in plotting plotPolylines
		pipLineVariable = self.declearVariables()
		#=========================
		#declearVariables
		variableDeclaration = self.genDeclaration()
		#
		plotPolylines = pipLineVariable + '''
		var flightPath=new google.maps.Polyline({
		  path:pipLine,
		  strokeColor:"#0063BD",
		  strokeOpacity:0.8,
		  strokeWeight:5
		  });

		flightPath.setMap(map);'''
		#===================
		self.api = '''
		<script>'''
		self.api += variableDeclaration
		self.api += '''
			var map;
			//var maker = new google.maps.Marker({map:map, })
			//var infowindow = new google.maps.InfoWindow();
			var marker;
			var infowindow;
			var fLng, fLat;
			var myCenter = new google.maps.LatLng(-38.144061, 144.360345); //lag and lng

			function initialize() {
				var mapProp = {
					center: myCenter,
					zoom: 17,
					mapTypeId: google.maps.MapTypeId.HYBRID
				};
				map=new google.maps.Map(document.getElementById("googleMap"), mapProp);
				//event click to drop a pin
				marker = new google.maps.Marker({
					map:map, 
					position: myCenter,
					draggable: true,
					title: "Drag me!"
				})
				infowindow = new google.maps.InfoWindow({
						content: 'Latitude: ' + myCenter.lat() + '<br>Longtitude: ' + myCenter.lng()
					});
				
				google.maps.event.addListener(marker, 'drag', function(event){
					updateForm(event.latLng)
				});
		'''
		self.api += plotPolylines
		self.api += '''
			}
			function updateForm(location){
				fLng = document.getElementById("lng");
				fLat = document.getElementById("lat");
				fLng.value = location.lng();
				fLat.value = location.lat();
			}
			google.maps.event.addDomListener(window, 'load', initialize);

			/*
			version 0.4 changelog:
			have finished the function that allows drag and drop marker and update the coordinates in the input field. thus these coordinates can be transferred to another page via GET method
			*/
		</script>
		'''
	def readLocation(self,location):
		index = 0
		nodeName = []
		locationCoordinates = []
		locationDic = {}
		
		for i in range(int(len(location) / 2)):
			nodeName.append("node" + str(i))
		for c in range(int(len(location) - 1)):
			locationCoordinates.append(c)
		while index < len(nodeName):
			locationDic[nodeName[index]] = [location[index*2], location[index*2 + 1]]
			index += 1
		return (locationDic, nodeName)
	def declearVariables(self):
		variableString = "var pipLine = ["
		indexc = 0
		while indexc < (len(self.nodeName) - 1):
			variableString += (self.nodeName[indexc] + ", ")
			indexc += 1
		variableString += (self.nodeName[indexc] + " ];")
		return variableString
		
	def genDeclaration(self):
		variableDeclaration = ""
		for name in self.nodeName:
			variableDeclaration += ("var " + name + " = new google.maps.LatLng(" + str(self.locationDic[name][0]) + ", " + str(self.locationDic[name][1]) + ");")
		return variableDeclaration
		