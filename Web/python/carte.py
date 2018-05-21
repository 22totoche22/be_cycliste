conf=Import('../data/config.py')
template=Import('../python/template.py')
chemin = conf.chemin()
bdd = Import('../data/bdd.py')

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
            #floating_panel {
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
        width : 50%;
        margin : auto;
        color : black;
}
        #infowindow {
        color : black;
        }
        #supprimer{
        background : white;
        color: black;
        width : 50%;
        margin : auto;
        }
        #cloturer{
        background : white;
        color: black;
        width : 50%;
        margin : auto;
        }
          input[data-readonly] {
  pointer-events: none;

}
            </style>
    
  <body>
      
      <div id="map"></div>
       <script>
      function initMap() {
            var myLatlng = {lat: 43.6, lng: 1.433333};
            var map = new google.maps.Map(document.getElementById('map'), {
                            zoom: 10,
                            center: myLatlng
            });


          var iconDefault = 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png';'''

    if "login" in Session():
        vcarte += '''
            
          
          id_incident.value ='';'''
    vcarte+= '''     
          var previousMarker;
          var listepoints = '''+str(affiche_incident())+'''
          var i=0;
          li='''+str(len(affiche_incident()))+''';
          while(i<li){
              var marker = new google.maps.Marker({
                  position: {lat : parseFloat(listepoints[i][0]),lng: parseFloat(listepoints[i][1])},
                  map: map,
                  title : listepoints[i][5],
                  icon: iconDefault,
                  opacity : listepoints[i][4]/4,
              });
              var idcat =  listepoints[i][3]-1;
              var cat = '''+str(affiche_categorie())+''';
              var content = '<div id="infowindow">'+
            '<h1 id="firstHeading" class="firstHeading">'+cat[idcat][2]+'</h1>'+
            '<div id="bodyContent">'+
            '<p><b>'+cat[idcat][1]+'</b> : '+listepoints[i][2]+' </p>'+
            '</div>'+
            '</div>';
              previousmarker = marker;
              addInfoWindow(marker, content);
              i++;
              
              
          }
         
      
      }
      function addInfoWindow(marker, message) {
            var infoWindow = new google.maps.InfoWindow({
                content: message,
            });

            google.maps.event.addListener(marker, 'mouseover', function () {
                infoWindow.open(map, marker);
            });
            
            google.maps.event.addListener(marker, 'click', function () {
                '''

    if "login" in Session():
        vcarte+= '''        document.getElementById("id_incident").value =  marker.getTitle();'''

    vcarte += '''previousmarker.setIcon('http://maps.google.com/mapfiles/ms/icons/blue-dot.png');
                marker.setIcon('http://maps.google.com/mapfiles/ms/icons/yellow-dot.png')
                previousmarker = marker;

            });
            
            
            google.maps.event.addListener(marker,'mouseout', function() {
                infoWindow.close(map,marker);
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


    if "login" in Session():

        vcarte += '''
            <div id="cloturer"><label>Pour cloturer un incident, veuillez cliquer sur celui-ci sur la carte</label></div>
            <form id="floating_panel" method="POST" action = "fcloturer" enctype="multipart/form-data">
                <label class="" >idIncident : </label> <input id="id_incident" type="text" name="idincident" value="" required data-readonly>
                <label class="" >raison de la cloture : </label> <input id="raison_clot" type="text" name="raisoncloture" placeholder="réparé,fini..." value="" required >
               <input  type="submit"  value="cloturer">
               </form>'''

    else:

        vcarte += '''<div id="supprimer"><label>Pour cloturer un incident, veuillez-vous connecter</label></div>'''


    


    return vcarte

def affiche_incident():
    liste = bdd.affichincident()
    liste_1 = []

    for (niveauUrgence, description, longitude, latitude, idUtilisateur, idSousCategorie, lieu, cloture,idIncident) in liste:
        if not cloture:
            liste_1.append([latitude.decode(),longitude.decode(),description.decode(),str(idSousCategorie), niveauUrgence.decode(),str(idIncident)])

    return liste_1

def affiche_categorie():
    liste = bdd.recup_categorie()
    liste_2 = []

    for (idSousCategorie,nomSousCategorie, nomCategorie) in liste:
        liste_2.append([str(idSousCategorie),nomSousCategorie.decode(), nomCategorie.decode()])

    return liste_2

def fcloturer(idincident='', raisoncloture=''):
    result = template.entete(chemin)
    result += template.menu(chemin)
    result += template.titre("Cloture",0)
    result += "<section>"
    msg = bdd.cloturincident(idincident, raisoncloture)
    if msg is None:
        result += "<div>L'incident a été cloturé</div>"
    result += "</section>"
    result += template.footer(chemin)
    return result

