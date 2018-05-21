conf=Import('../data/config.py')
template=Import('../python/template.py')
chemin = conf.chemin()
bdd = Import('../data/bdd.py')

def index():
    result = template.entete(chemin)
    result += template.menu(chemin)
    result += template.titre("Déclarer un incident",0)
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
        bottom: 20px;
        left: 0.5%;
        z-index: 5;
        background-color: #fff;
        padding: 5px;
        border-left: 10% solid #fff;
        text-align: center;
        font-family: 'Roboto','sans-serif';
        line-height: 30px;
        padding-left: 10px;
        width : 70%;
        margin : auto;
        
}
    #sous_carte{
    color : #fff
    }
    #dessus_carte{
    color : #fff
    }
    label {
    color : black;
    }
    input[data-readonly] {
  pointer-events: none;

}
    #description_inci{
    width : 80%;
    }

    </style>
  </head>
  <body>
      
     
      
    <label id = "dessus_carte">Veuillez cliquer sur le lieu de l'incident</label>
    <hr></hr>
      <div id="map"></div>
      <hr></hr>
      <label id = "sous_carte">Veuillez remplir les informations relatives à l'incident</label>
      <hr></hr>
      <form id="floating-panel" method="POST" action = "fenvoyer" enctype="multipart/form-data">
        <li><label class="" >Latitude : </label> <input id=latitude type="text" name="latitude" value="" required data-readonly>
        <label class="" >Longitude : </label> <input id=longitude type="text" name="longitude" value="" required data-readonly>
        <label class="" >Quartier : </label> <input id=adresse type="text" name="adresse" value="" required data-readonly></li>
        <input id=ville type="text" name="ville" value="" hidden>
        <li><label class="" > Description de l'incident</label>
        <li><textarea id = "description_inci" name="Description" placeholder="Décrivez l'incident"></textarea></li>
        <li><label class="" >Catégorie </label>
        <select name=Categorie>
                        <optgroup label="Revetement">
                            <option value="1">trou dans la chaussée</option>
                            <option value="2">chaussée déformée</option>
                            <option value="3">objet sur la chaussée</option>
                            <option value="4">chaussée glissante</option>
                        </optgroup>
                        <optgroup label="Travaux">
                            <option value="5">piste cyclabe inutilisable</option>
                            <option value="6">danger</option>
                        </optgroup>
                        <optgroup label="Permanent">
                            <option value="7">lieu interdit pour les cyclistes</option>
                            <option value="8">lieu dangereux pour les cyclistes</option>
                        </optgroup>
                        <optgroup label="Trafic">
                            <option value="9">embouteillage</option>
                            <option value="10">accident de la route</option>
                        </optgroup>
                        <optgroup label="Autre">
                            <option value="11">autre</option>
                        </optgroup>
        </select>
        <label class="" >Niveau d'urgence </label>
        <select name="Niveau">
                        <optgroup label="Niveau d'urgence">
                            <option value="1">bas</option>
                            <option value="2">moyen</option>
                            <option value="3">fort</option>
                            <option value="4">élevé</option>
                        </optgroup>
        </select></li>
     
        <input  type="submit"  value="valider">
      </form>
      <hr></hr>
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
            ville.value="";
      }
      var marker;
      var latitude = document.getElementById("latitude");
      var longitude = document.getElementById("longitude");
      var adresse = document.getElementById("adresse");
      var ville = document.getElementById("ville");
      function placeMarker(location, map,geocoder) {
                    adresse.value = "";
                    ville.value = "";
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
                                          ville.value = results[1].address_components[1].long_name;
                                          

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

    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAgsaVTjTFgU__1we6rLRCRMRZkr1rc0DU&callback=initMap"
    async defer></script>
  </body>
        '''

    return vcarte


# def fenvoyer(latitude='', longitude='', adresse='',ville='', Categorie='',Description='',Niveau=''):
#         result = "les données envoyées sont : <br />lat :" + latitude
#         result += "<br /> long :" + longitude
#         result += "<br /> adresse :" + adresse
#         result += "<br /> description :" + Description
#         result += "<br /> Categorie :" + Categorie
#         result += "<br /> niveau :" + Niveau
#         return result

def fenvoyer(latitude='', longitude='', adresse='',ville='', Categorie='',Description='',Niveau=''):
    result = template.entete(chemin)
    result += template.menu(chemin)
    result += template.titre("Incident",0)
    result += "<section>"
    msg = bdd.insertincident(latitude, longitude, adresse, Description, Categorie, Niveau)
    if msg is None:
        result += "<div>L'incident a été enregistré</div>"
    #result += "<div class='comm'>Liste des incidents enregistrés dans la base de données</div>"
    #result += afficheincident()
    result += "</section>"
    result += template.footer(chemin)
    return result


def afficheincident():
    result = ''
    liste = bdd.affichincident()

    for (latitude, longitude, adresse, description, categorie, niveau, lieu) in liste:
        result += '<div>'
        result += str(id)+' '
        result += latitude.decode()+' '
        result += longitude.decode()+' '
        result += adresse.decode()+' '
        result += description.decode() + ' '
        result += str(categorie) + ' '
        result += str(niveau) + ' '
        result += lieu.decode() + ' '
        result += '</div>'

    return result