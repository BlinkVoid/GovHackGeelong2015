from static import lineslines
from static import pipelineNetwork
class map2():	
	
	def __init__(self, location, value):
		self.locationDic = {}
		self.nodeName = []
		
		#====changes to display pipeline as a whole
		#self.pipeNetwork = lineslines.mapPipelines()
		#print (self.pipeNetwork)
		#self.pipeLocationDic = {}
		#self.pipeNodeName = []
		#(self.pipeLocationDic, self.pipeNodeName) = self.readLocation(self.pipeNetwork, 'pipe')
		
		# for a in range(10):
			# print("name " + self.pipeNodeName[a] + self.pipeLocationDic[self.pipeNodeName[a]])
		#==============================================
		(self.locationDic, self.nodeName) = self.readLocation(location, 'node')
		#print (self.nodeName)
		#print (self.locationDic)
		#========================= to be used in plotting plotPolylines
		#original
		#pipLineVariable = self.declearVariables()
		#modified=== feed with variable
		pipLineVariable = self.declearVariables(self.nodeName, "pipLine")
		#declear varialbe with the pipe network as well
		#pipLineNetVariable = self.declearVariables(self.pipeNodeName, "NetPipLines")
		#=========================
		#declearVariables
		variableDeclaration = self.genDeclaration(self.locationDic, self.nodeName)
		#declear pipenet varialbe
		#=========using static declearation for speed.
		#pipLineNetVariableDeclaration = self.genDeclaration(self.pipeLocationDic, self.pipeNodeName)
		#============original ===============
		# plotPolylines = pipLineVariable + '''
		# var flightPath=new google.maps.Polyline({
		  # path:pipLine,
		  # strokeColor:"#0063BD",
		  # strokeOpacity:0.8,
		  # strokeWeight:5
		  # });
		
		# flightPath.setMap(map);'''
		#===================changes
		plotPolylines = pipLineVariable + '''
		var flightPath=new google.maps.Polyline({
		  path:pipLine,
		  strokeColor:"#0063BD",
		  strokeOpacity:0.8,
		  strokeWeight:5
		  });

		flightPath.setMap(map);'''
		#=======================
		self.api = '''
		<script>'''
		self.api += variableDeclaration
		self.api += '''
			var map;
			//var maker = new google.maps.Marker({map:map, })
			//var infowindow = new google.maps.InfoWindow();
			//var marker;
			//var infowindow;
			var fLng, fLat;
			var myCenter = new google.maps.LatLng(''' + value['lat'] + ''',''' + value['lng'] + ''' ); //lag and lng

			function initialize() {
				var mapProp = {
					center: myCenter,
					zoom: 17,
					mapTypeId: google.maps.MapTypeId.ROADMAP
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
	def readLocation(self,location, tName):
		index = 0
		nodeName = []
		# locationCoordinates = []
		locationDic = {}
		
		for i in range(int(len(location) / 2)):
			nodeName.append(tName + str(i))
		# for c in range(int(len(location) - 1)):
			# locationCoordinates.append(c)
		while index < len(nodeName):
			locationDic[nodeName[index]] = [location[index*2], location[index*2 + 1]]
			index += 1
		return (locationDic, nodeName)
	#==original== 
	#def declearVariables(self):
	def declearVariables(self, nodeList, graphName):
		variableString = "var " + graphName + " = ["
		indexc = 0
		#while indexc < (len(self.nodeName) - 1):
		while indexc < (len(nodeList) - 1):
			#variableString += (self.nodeName[indexc] + ", ")
			variableString += (nodeList[indexc] + ", ")
			indexc += 1
		#variableString += (self.nodeName[indexc] + " ];")
		##might cause problem here
		#variableString += "];"
		variableString += (nodeList[indexc] + " ];")
		return variableString
		
	def genDeclaration(self, tNodeDic, tNodeName):
		variableDeclaration = ""
		print("len: " + str(len(tNodeName)))
		#print(tNodeName)
		for name in tNodeName:
			variableDeclaration += ("var " + name + " = new google.maps.LatLng(" + str(tNodeDic[name][0]) + ", " + str(tNodeDic[name][1]) + ");")
		return variableDeclaration
		