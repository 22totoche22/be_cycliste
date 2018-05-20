conf=Import('../data/config.py')
bdd=Import('../data/bdd.py')
template=Import('template.py')
chemin = conf.chemin()


def index():
    msg = template.entete(chemin)
    msg += template.menu(chemin)
    msg += template.titre("Gérer les utilisateurs",0)
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

            <h2>Liste des utilisateurs</h2>

          <table id="table_utili" class="table" data-toggle="table" data-search="true" data-pagination="true"  data-page-size="4" >
                <thead>
                    <tr>
                        <th data-field="col1" data-sortable="true">idUtilisateur</th>
                        <th data-field="col2" data-sortable="true">Nom</th>
                        <th data-field="col3" data-sortable="true">Prenom</th>
                        <th data-field="col4" data-sortable="true">login</th>
                        <th data-field="col5" data-sortable="true">mail</th>
                        <th data-field="col5" data-sortable="true">nombre d'incidents déclarés</th>
                        <th data-field="col5" data-sortable="true">nombre d'incidents fermés</th>
                    </tr>
                </thead>
          </table>
          
          <h2>Liste des analystes</h2>

          <table id="table_analy" class="table" data-toggle="table" data-search="true" data-pagination="true"  data-page-size="4" >
                <thead>
                    <tr>
                        <th data-field="col1" data-sortable="true">idUtilisateur</th>
                        <th data-field="col2" data-sortable="true">Nom</th>
                        <th data-field="col3" data-sortable="true">Prenom</th>

                    </tr>
                </thead>
          </table>
          
          <h2>Liste des administrateurs</h2>

          <table id="table_admin" class="table" data-toggle="table" data-search="true" data-pagination="true"  data-page-size="4" >
                <thead>
                    <tr >
                        <th data-field="col1" data-sortable="true">idUtilisateur</th>
                        <th data-field="col2" data-sortable="true">Nom</th>
                        <th data-field="col3" data-sortable="true">Prenom</th>
                    </tr>
                </thead>
          </table>
          
          <form id="panel" method="POST" action = "fchangerprofil" enctype="multipart/form-data">
          <hr><label>Rendre</label>
          <input id="lal" name="idUtili" placeholder="idUtilisateur" required type="number" min=2></input>
          <select id="position" name="Profil">
                        <optgroup label="Profil">
                            <option value="1">Analyste</option>
                            <option value="2">Admin</option>
                            <option value="3">Utilisateur de base</option>
                        </optgroup>
          </select>
          <input  type="submit"  value="valider">
          </hr>
        </form>
        
                
         <script>
        function initutili(mess,long,table,long_k){
            var listeutilisateurs = mess;
            lal.value="";
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
        var valeur1= '''+str(affiche_tout_utilisateur())+'''
        var longueur1 = '''+str(len(affiche_tout_utilisateur()))+'''
        var longk1 = '''+str(len(affiche_tout_utilisateur()[0]))+'''
        initutili(valeur1,longueur1,"table_utili",longk1);
        var valeur2= '''+str(affiche_analy())+'''
        var longueur2 = '''+str(len(affiche_analy()))+'''
        var longk2 = '''+str(len(affiche_analy()[0]))+'''
        initutili(valeur2,longueur2,"table_analy",longk2);
        var valeur3= '''+str(affiche_admin())+'''
        var longueur3 = '''+str(len(affiche_admin()))+'''
        var longk3 = '''+str(len(affiche_admin()[0]))+'''
        initutili(valeur3,longueur3,"table_admin",longk3);
        </script>
        
        </body>

       
'''

        return inscription

def affiche_tout_utilisateur():
    result = []
    clot =[]
    ouv =[]
    liste = bdd.affichetoututilisateur()
    nb_cloture = bdd.count_cloture()
    nb_ouverture = bdd.count_ouverture()

    for (idUtilisateur,nb_clo) in nb_cloture:
        clot.append([str(idUtilisateur),str(nb_clo)])

    for (idUtilisateur,nb_ouv) in nb_ouverture:
        ouv.append([str(idUtilisateur),str(nb_ouv)])

    for (idUtilisateur,login,nom,prenom, mail) in liste:
        result.append([str(idUtilisateur),nom.decode(),prenom.decode(),login.decode(),mail.decode(),str(0),str(0)])

    for k,i in enumerate(result):
        for m,n in enumerate(clot):
            if i[0] == n[0]:
                i[6] = str(n[1])
        for x,y in enumerate(ouv):
            if i[0] == y[0]:
                i[5] = str(y[1])

    return result


def fchangerprofil(idUtili,Profil):
    result = template.entete(chemin)
    result += template.menu(chemin)
    result += template.titre("Profil", 0)
    result += "<section>"
    do = False
    for k in affiche_tout_utilisateur():
        if idUtili == k[0]:
            do = True
    if do :
        if Profil == str(2):
            don = False
            for i in affiche_analy():
                if idUtili == str(i[0]):
                    don = True
            if don:
                msg = bdd.changeprofil(idUtili, Profil)
                if msg is None:
                    result += "<div>Le profil de cet utilisateur a été changé en administrateur</div>"
                result += "</section>"
                result += template.footer(chemin)
                return result
            result += "<div>Le profil de cet utilisateur doit d'abord être passé à analyste</div>"
            result += "</section>"
            result += template.footer(chemin)
            return result
        elif Profil == str(1):
            msg = bdd.changeprofil(idUtili, Profil)
            if msg is None:
                result += "<div>Le profil de cet utilisateur a été changé en analyste</div>"
            result += "</section>"
            result += template.footer(chemin)
            return result
        else:
            msg = bdd.changeprofil(idUtili, Profil)
            if msg is None:
                result += "<div>Le profil de cet utilisateur a été changé en utilisateur de base</div>"
            result += "</section>"
            result += template.footer(chemin)
            return result
    result += "<div>Cet utilisateur n'existe pas</div>"
    result += "</section>"
    result += template.footer(chemin)
    return result


def affiche_admin():
    liste_ = []
    liste = bdd.administrateur()
    for (idadmin,nom,prenom) in liste:
        liste_.append([idadmin,nom.decode(),prenom.decode()])
    return liste_

def affiche_analy():
    liste_ = []
    liste = bdd.analyste()
    for (idanal,nom,prenom) in liste:
        liste_.append([idanal,nom.decode(),prenom.decode()])
    return liste_

