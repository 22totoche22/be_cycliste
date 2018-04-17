conf=Import('../data/config.py')
bdd=Import('../data/bdd.py')
template=Import('template.py')
chemin = conf.chemin()


def index():
    msg = template.entete(chemin)
    msg += template.menu(chemin)
    msg += template.titre("Se connecter",0)
    msg += connecter()
    msg += template.footer(chemin)
    return msg


def connecter():

    connection = '''
        <section id="connecter">

            <div class="row">
                <div class="col-12 col-md-4 col-sm-6 offset-sm-3 offset-md-4 form-group" >
                    <form method="post" action="'''+chemin+'''/python/connecter.py/verif">
                        <input name="login" placeholder="Votre login" type="text" />
                        <input name="pwd" placeholder="Votre mot de passe" type="text" />
                        <button class="button" type="submit">Se connecter</button>
                    </form>
                </div>
            </div>
		</section>
        '''
    return connection


def verif(login='', pwd=''):
    # resultat = bdd.verif_connect(login, pwd)
    Session()["nom"] = "Lagaffe"
    Session()["prenom"] = "Gaston"
    Session()["login"] = login
    Session()["pwd"] = pwd
    raise HTTP_REDIRECTION(chemin + '/index.py')


def deconnecter():
    if "nom" in Session(): #si la session existe, on la supprime
        del Session()["nom"]
        del Session()["prenom"]
        del Session()["login"]
        del Session()["pwd"]
    raise HTTP_REDIRECTION(chemin+'/index.py')          # la personne est redirigée vers la page d'accueil
