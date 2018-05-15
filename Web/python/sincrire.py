conf=Import('../data/config.py')
bdd=Import('../data/bdd.py')
template=Import('template.py')
chemin = conf.chemin()


def index():
    msg = template.entete(chemin)
    msg += template.menu(chemin)
    msg += template.titre("S'inscrire",0)
    msg += inscription()
    msg += template.footer(chemin)
    return msg


def inscription():
        inscription = '''
            <section id="inscription">
    
                <div class="row">
                    <div class="col-12 col-md-4 col-sm-6 offset-sm-3 offset-md-4 form-group" >
                        <label>L'inscription est presque finie ! Veuillez remplir les informations suivantes:</label>
                        <form method="post" action = "finscrire" enctype="multipart/form-data">
                            <input name="login" placeholder="Votre login" type="text" required/>
                            <input id=pass1 name="pwd" placeholder="Votre mot de passe" type="password" required/>
                            <input id=pass2 name="pwd2" placeholder="Retapez votre mot de passe" type="password" onBlur="checkpassword()" required/>
                            <input name="surnom" placeholder="Surnom" type="text" required/>
                            <div id="comp" required></div>
                            <button class="button" type="submit">S'incrire</button>
                        </form>
                    </div>
                </div>
            </section>
            <script>
            function checkpassword(){
                var champA = document.getElementById("pass1").value;
                var champB = document.getElementById("pass2").value;
                var div_comp = document.getElementById("divcomp");
                if(champA != champB){

                        comp.innerHTML = "Pas le même mot de passe";
                        divcomp.value ="aa";
                }
                if(champA == champB){
                       comp.innerHTML = "";
                        divcomp.value = "";
                }
            }
            </script>
            '''
        return inscription

def finscrire(login,pwd,pwd2,surnom):
            result = "les données envoyées sont : <br />login :" + login
            result += "<br /> mdp :" + pwd
            result += "<br /> surnom :" + surnom

        return result


