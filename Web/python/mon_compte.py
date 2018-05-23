conf=Import('../data/config.py')
bdd=Import('../data/bdd.py')
template=Import('template.py')
chemin = conf.chemin()


def index(essai=''):
    msg = template.entete(chemin)
    msg += template.menu(chemin)
    msg += template.titre("Mon compte",0)
    msg += mon_compte(essai)
    msg += template.footer(chemin)
    return msg


def mon_compte(essai=''):
    compte = '''
        <style>
        label {
        color : black}
        
        #moncompte{
        background : #fff;
        width : 65%;
        text-align : center;
        margin : auto;
        }
        #comp_{
        color : red
        }
        #mdp_fail{
        color : red
        }
        </style>
                    <section id="compte">

                        <div id = "moncompte" class="row">
                            <div class="col-12 col-md-4 col-sm-6 offset-sm-3 offset-md-4 form-group" >
                                
                                
                                
                                    <hr><label>Vos informations sont :</label></hr>
                                    <hr><label>Login : '''+Session()["login"]+'''</label></hr>
                                    <hr><label>Surnom : '''+Session()["surnom"]+'''</label></hr>
                                    <hr><label>Mail : '''+Session()["mail"]+'''</label></hr>
                                    <br></br><br></br><br></br>
                                     <b><hr><label>Changer surnom</label></hr></b>
                                        <form id = "change_surnom" method="post" action="fchange_surnom" enctype="multipart/form-data"> 
                                        <hr><input name="surnom" placeholder="Votre nouveau surnom" type="text" /></hr>
                                        <hr><button id="change_surnom" class="button" type="submit">Changer</button></hr>
                                        </form>
                                        <br></br><br></br>
                                        <hr><label>Changer mot de passe </label></hr>'''
    if essai !='':
        compte += '''<label id=mdp_fail >Mauvais mot de passe  '''
    compte += '''                                    
                                        
                                        
                                        <form id = "change_mdp" method="post" action="fchange_mdp" enctype="multipart/form-data">
                                        <hr><input id=pass_0 name="pwd" placeholder="Votre ancien mot de passe" type="password" required/></hr> 
                                        <hr><input id=pass_1 name="pwd1" placeholder="Votre nouveau mot de passe" type="password" required/></hr>
                                        <hr><input id=pass_2 name="pwd2" placeholder="Retapez votre nouveau mot de passe" type="password" onKeyUp="checkpassword()" required/></hr>
                                        <div id="comp_" required></div>
                                        <hr><button id="changemdp" class="button" type="submit">Changer</button></hr>
                                        
                           
                            </div>
                        </div>
                    </section>
                     <script>
            function checkpassword(){
                var champA = document.getElementById("pass_1").value;
                var champB = document.getElementById("pass_2").value;
                if(champA != champB){
                        
                        comp_.innerHTML = "Pas le même mot de passe";
                        document.getElementById("changemdp").disabled = true;
                }
                if(champA == champB){
                       comp_.innerHTML = "";
                       document.getElementById("changemdp").disabled = false;
                }
            }

            </script>
                    '''

    return compte

def fchange_surnom(surnom):
        result = template.entete(chemin)
        result += template.menu(chemin)
        result += template.titre("Login",0)
        result += "<section>"
        msg = bdd.change_surnom(surnom)
        if msg is None:
            result += "<div>Vous nouveau surnom a bien été enregistré, reconnectez-vous pour voir les changements !</div>"
        result += "</section>"
        result += template.footer(chemin)
        return result


def fchange_mdp(pwd, pwd1,pwd2):
    if Session()["pwd"] == pwd:
        result = template.entete(chemin)
        result += template.menu(chemin)
        result += template.titre("Login", 0)
        result += "<section>"
        msg = bdd.change_mdp(pwd1)
        if msg is None:
            result += "<div>Vous nouveau surnom a bien été enregistré, reconnectez-vous pour voir les changements !</div>"
        result += "</section>"
        result += template.footer(chemin)

    else:
        return index("non")
    return result
