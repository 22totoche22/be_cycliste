conf=Import('../data/config.py')
bdd=Import('../data/bdd.py')
template=Import('template.py')
chemin = conf.chemin()


def index():
    msg = template.entete(chemin)
    msg += template.menu(chemin)
    msg += template.titre("Gérer les incidents",0)
    msg += gestion_utili()
    msg += template.footer(chemin)
    return msg


def gestion_utili():
    inscription = '''
        <style>
        #position{
        width : 20%;
        }
        label{
        color: black;
        }
        #panel{
        background : white;
        width : 50%;
        margin : auto;
        }
        input[data-readonly] {
  pointer-events: none;

        </style>
        <head>


</head>
        <body>

            <h2>Liste des incidents</h2>

          <table id="table_inci" class="table" data-toggle="table" data-search="true" data-pagination="true"  data-page-size="4" >
                <thead>
                    <tr>
                        <th data-field="col1" data-sortable="true">idIncident</th>
                        <th data-field="col2" data-sortable="true">niveauUrgence</th>
                        <th data-field="col3" data-sortable="true">description</th>
                        <th data-field="col4" data-sortable="true">cloture</th>
                        <th data-field="col8" data-sortable="true">idUtilisateur</th>
                        <th data-field="col10" data-sortable="true">idSouscategorie</th>
                        <th data-field="col11" data-sortable="true">lieu</th>
                    </tr>
                </thead>
          </table>

         

          <form id="panel" method="POST" action = "fsupprimer" enctype="multipart/form-data">
          <hr>
          <input id="lala" name="idincident" placeholder="idIncident" required type="number" ></input>
          <input  type="submit"  value="supprimer">
          </hr>
        </form>


         <script>
        function initinci(mess,long,table,long_k){
            var listeutilisateurs = mess;
            lala.value="";
            var table = document.getElementById(table);
            var i=0;
            var li= long;
            while(i<li){
                  var row = table.insertRow(i+1);
                  var j=0;
                  var k = long_k
                  while (j<k){
                      var cell1 = row.insertCell(j);
                      cell1.innerHTML = listeutilisateurs[i][j];
                      j++
                      }
                  i++;
                  }
        }
        var valeur1= ''' + str(affiche_tout_incident()) + '''
        var longueur1 = ''' + str(len(affiche_tout_incident())) + '''
        var longk1 = ''' + str(len(affiche_tout_incident()[0])) + '''
        initinci(valeur1,longueur1,"table_inci",longk1);
        </script>

        </body>


'''

    return inscription


def affiche_tout_incident():
    result = []
    liste = bdd. affichincident()
    for (niveauUrgence, description, longitude, latitude, idUtilisateur, idSousCategorie, lieu, cloture, idIncident) in liste:
        result.append([str(idIncident),niveauUrgence.decode(), description.decode(), str(cloture), str(idUtilisateur), str(idSousCategorie), lieu.decode()])
    return result

def fsupprimer(idincident=''):
    result = template.entete(chemin)
    result += template.menu(chemin)
    result += template.titre("Suppression",0)
    result += "<section>"
    do = False
    for k in affiche_tout_incident():
        if k[0] == str(idincident):
            do = True
    if do:
        msg = bdd.suppincident(idincident)
        if msg is None:
            result += "<div>L'incident a été supprimé</div>"
        result += "</section>"
        result += template.footer(chemin)
        return result
    else:
        result += "<div>L'incident n'existe pas</div>"
        result += "</section>"
        result += template.footer(chemin)
        return result