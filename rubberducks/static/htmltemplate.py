body='''
			<body>
			<nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/stormwatermonitor/">Rubber Duck XIII - the pollution tracker system</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">Home</a></li>
			<li class="active"><a href="https://hackerspace.govhack.org/content/mighty-ducks-stormwater-tracker">About</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>

    <div class="container">
				<div class="panel">
					<div class="subp_left">
					</div>
					<div class="subp_right">
						<div id="googleMap" style="width:60vw;height:60vh;"></div>
					</div>
					<div class="subp_bottom">
						<p>After selecting your location, click to button below</p>
						<form action="track" method="GET">
							Latitude: <input type="text" id= "lat" class="coordiantes" value="Drag the pin" name="lat"><br>
							Longitude: <input type="text" id="lng" class="coordinates" value="Drag the pin" name="lng"><br>
							<select name="spill">
							<option value="detergent">Detergent</option>
							<option value="oil">Oil</option>
							<option value="duck">Rubber Ducky</option>
							</select>
							<input type="submit" value="Submit">
						</form>
					</div>
				</div>

    </div><!-- /.container -->
				
				<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
				<script src="/static/js/bootstrap.min.js"></script>
			</body>
		'''
		
header = '''
			<head>
				<meta name="viewport" content="width=device-width, initial-scale=1">
				
				<meta></meta>
				<script src="http://maps.googleapis.com/maps/api/js"></script>
				<link href="/static/css/bootstrap.min.css" rel="stylesheet">
				<link href="/static/css/style.css" rel="stylesheet">

				<!--Deakin Lng -38.144061, Lat 144.360345-->'''