conf=Import('../data/config.py')
bdd=Import('../data/bdd.py')
template=Import('template.py')
chemin = conf.chemin()


def index(essai=''):
    msg = template.entete(chemin)
    msg += template.menu(chemin)
    msg += template.titre("S'inscrire",0)
    msg += inscription(essai)
    msg += template.footer(chemin)
    return msg


def inscription(essai=''):
        inscription = '''
        
            <style>
            #comp{
            color : red;
            
            }
            #insriptionfail{
            color : red}
            </style>
            <section id="inscription">
    
                <div class="row">
                    <div class="col-12 col-md-4 col-sm-6 offset-sm-3 offset-md-4 form-group" onsubmit="return fverif">
                        <label>L'inscription est presque finie ! Veuillez remplir les informations suivantes:</label>
                        <form id="inscrip" method="post" action = "finscrire" enctype="multipart/form-data">
        '''
        if essai != '':
           inscription += ''' <label id="insriptionfail"> Login déjà pris</label>
            '''
        inscription +='''
                            
                            <li><input name="login" placeholder="Votre login" type="text" required/></li>
                            <li><input id=pass1 name="pwd" placeholder="Votre mot de passe" type="password" required/></li>
                            <li><input id=pass2 name="pwd2" placeholder="Retapez votre mot de passe" type="password" onKeyUp="checkpassword()" required/></li>
                            <li><input  name="surnom" placeholder="Surnom" type="text" required/></li>
                            <div id="comp" required></div>
                            <button id = "validerinsc" class="button" type="submit" >S'incrire</button>
                        </form>
                    </div>
                </div>
            </section>
            <script>
            function checkpassword(){
                var champA = document.getElementById("pass1").value;
                var champB = document.getElementById("pass2").value;
                if(champA != champB){
                        
                        comp.innerHTML = "Pas le même mot de passe";
                        document.getElementById("validerinsc").disabled = true;
                }
                if(champA == champB){
                       comp.innerHTML = "";
                        document.getElementById("validerinsc").disabled = false;
                }
            }

            </script>
            '''
        return inscription




def finscrire(login,pwd,pwd2,surnom):
    if login not in affiche_utili():
        result = template.entete(chemin)
        result += template.menu(chemin)
        result += template.titre("Inscription",0)
        result += "<section>"

        msg = bdd.insertUtili(login,pwd,surnom)
        if msg is None:
            result += "<div>Vous êtes bien inscrit</div>"
        result += "</section>"
        result += template.footer(chemin)
    else:
        return index("non")
    return result


def affiche_utili():
    list = []
    liste = bdd.afficheutilisateur()
    for login in liste:

        list.append(login[0].decode())

    return list


