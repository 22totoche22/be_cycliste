conf=Import('../data/config.py')
bdd=Import('../data/bdd.py')
template=Import('template.py')
chemin = conf.chemin()


def index(essai=''):
    msg = template.entete(chemin)
    msg += template.menu(chemin)
    msg += template.titre("Se connecter",0)
    msg += connecter(essai)
    msg += template.footer(chemin)
    return msg


def connecter(essai=''):
    if essai=="":
        connection = '''
            <section id="connecter">
    
                <div class="row">
                    <div class="col-12 col-md-4 col-sm-6 offset-sm-3 offset-md-4 form-group" >
                        <form method="post" action="'''+chemin+'''/python/connecter.py/verif">
                            <input name="login" placeholder="Votre login" type="text" />
                            <input name="pwd" placeholder="Votre mot de passe" type="password" />
                            <button class="button" type="submit">Se connecter</button>
                        </form>
                        <label>Pas de compte ?</label>
                                <a href="'''+chemin+'''/python/sincrire.py">
                                S'inscrire
                                 </a>
                    </div>
                </div>
            </section>
            '''
    else:
        connection = '''
                    <section id="connecter">

                        <div class="row">
                            <div class="col-12 col-md-4 col-sm-6 offset-sm-3 offset-md-4 form-group" >
                                <form method="post" action="''' + chemin + '''/python/connecter.py/verif">
                                    <label>Mauvais mot de passe ou mauvais identifiant</label>
                                    <input name="login" placeholder="Votre login" type="text" />
                                    <input name="pwd" placeholder="Votre mot de passe" type="password" />
                                    <button class="button" type="submit">Se connecter</button>
                                </form>
                                <label>Pas de compte ?</label>
                                <a href="'''+chemin+'''/python/sincrire.py">
                                S'inscrire
                                 </a>
                            </div>
                        </div>
                    </section>
                    '''

    return connection


def verif(login='', pwd=''):
    if bdd.verif_connect(login, pwd):
        Session()["surnom"] = Session()["surnom"]
        Session()["login"] = login
        Session()["pwd"] = pwd
        raise HTTP_REDIRECTION(chemin + '/index.py')
    else:
        msg = template.entete(chemin)
        msg += template.menu(chemin)
        msg += template.titre("Se connecter", 0)
        msg += connecter('non')
        msg += template.footer(chemin)
        return msg




def deconnecter():
    if "login" in Session(): #si la session existe, on la supprime
        del Session()["surnom"]
        del Session()["login"]
        del Session()["pwd"]
    raise HTTP_REDIRECTION(chemin+'/index.py')          # la personne est redirigée vers la page d'accueil
