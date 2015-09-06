api = '''
<script>
		
	var map;
	//var maker = new google.maps.Marker({map:map, });
	//var infowindow = new google.maps.InfoWindow();
	var marker;
	var infowindow;
	var fLng, fLat;
	var myCenter = new google.maps.LatLng(-38.144061, 144.360345); //lag and lng
	//var myCenter0;
	var failed = false;
	
	function locate(){
		navigator.geolocation.getCurrentPosition(initialize, fail);
	}
	
	function fail(){
		failed = true;
		initialize()
	}
	function initialize(position) {
	//function initialize(){
		
		if (failed == false) {
			//locating works
			myCenter = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
		}
		
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
		
	}
	
	function updateForm(location){
		fLng = document.getElementById("lng");
		fLat = document.getElementById("lat");
		fLng.value = location.lng();
		fLat.value = location.lat();
	}
	google.maps.event.addDomListener(window, 'load', locate);
	//$(#googleMap).load("static/loading2.gif");
	/*
	version 0.4 changelog:
	have finished the function that allows drag and drop marker and update the coordinates in the input field. thus these coordinates can be transferred to another page via GET method
	*/
</script>
'''