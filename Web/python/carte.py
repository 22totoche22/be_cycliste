conf=Import('../data/config.py')
template=Import('../python/template.py')
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

}
        
            </style>
    
  <body>
      
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