conf=Import('../data/config.py')
template=Import('template.py')
chemin = conf.chemin()


def index():
    result = template.entete(chemin)
    result += template.menu(chemin)
    result += template.titre("Carte",0)
    result += carte()
    result += template.footer(chemin)
    return result

def carte():
    vcarte = '''
         <style>
      #map {
        height: 100%;
      }
      /* Optional: Makes the sample page fill the window. */
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
       #floating-panel {
       position: absolute;
        bottom: 20px;
        left: 0.5%;
        z-index: 5;
        background-color: #fff;
        padding: 5px;
        border: 1px solid #999;
        text-align: center;
        font-family: 'Roboto','sans-serif';
        line-height: 30px;
        padding-left: 10px;
}
        label {
        display : inline-block}
        #1{
        display:inline}
    </style>
  </head>
  <body>
      
     <form id="floating-panel" method="POST" action = "fcontacter" enctype="multipart/form-data">
      <div id=1><label class="" >Latitude : </label> <input id=latitude type="text" name="latitude" value="" disabled></div>
        <div id=2><label class="" >Longitude : </label> <input id=longitude type="text" name="longitude" value="" disabled></div>
        <div id=2><label class="" >Adresse : </label> <input id=adresse type="text" name="adresse" value=""disabled ></div>
        <div id=3><input  type="submit"  value="valider"></div>
      </form>
      <div id="map"></div>
    <script>
      function initMap() {
            var geocoder = new google.maps.Geocoder();
            var myLatlng = {lat: 43.6, lng: 1.433333};
            var map = new google.maps.Map(document.getElementById('map'), {
                            zoom: 10,
                            center: myLatlng
            });

            map.addListener('click', function(event) {
                            placeMarker(event.latLng, map,geocoder);
            });
            latitude.value = "";
            longitude.value= "";
            adresse.value="";
      }
      var marker;
      var latitude = document.getElementById("latitude");
      var longitude = document.getElementById("longitude");
      var adresse = document.getElementById("adresse");
      function placeMarker(location, map,geocoder) {
                    adresse.value = "";
                    if(marker){
                        marker.setPosition(location);
                    }
                    else{
                        marker = new google.maps.Marker({
                        position: location,
                        map: map
                        });
                    }
            map.panTo(marker.getPosition());
            latitude.value = location.lat();
            longitude.value = location.lng();
            geocoder.geocode( { 'location': {lat : parseFloat(location.lat()),lng : parseFloat(location.lng())}}, function(results, status) {

                    if (status === 'OK') {
                        if (results[0]) {

                                  if (results[1].address_components[0].types[1] == "political"){
                                          adresse.value = results[1].address_components[0].long_name;

                                    }



                        }
                        else {
                            window.alert('No results found');
                        }
                    }
                    else {
                            window.alert('Geocoder failed due to: ' + status);
                    }

            });


    }

    </script>
    <script src="https://developers.google.com/maps/documentation/javascript/examples/marker/marker.js">
    </script>
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/
jquery.min.js"></script>

    <script src="https://maps.googleapis.com/maps/api/js?key= AIzaSyAllVFdOZbLMkxQNHMcyCWM3b2TYzASBzQ&callback=initMap"
    async defer></script>
  </body>
        '''

    return vcarte


def fcontacter(latitude='', longitude='', adresse=''):
    result = "les données envoyées sont : <br />lat :" + latitude
    result += "<br /> long :" + longitude
    result += "<br /> adresse :" + adresse
    return result

