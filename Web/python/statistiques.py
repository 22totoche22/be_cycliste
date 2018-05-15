conf=Import('../data/config.py')
template=Import('../python/template.py')
chemin = conf.chemin()


def index():
    result = template.entete(chemin)
    result += template.menu(chemin)
    result += template.titre("Statistiques",0)
    result += statistiques()
    result += template.footer(chemin)
    return result


def statistiques():

    vstatistiques = '''
    <section id="statistiques">
            <div class="row">
                <div class="col-12 col-md-6 col-sm-8" >
                    <article>
                        <div>
                            <a href="'''+chemin+'''/saisie/saisieEtudeStatique.py">
                            <h3>Etude statique</h3>
                            </a>
                            <p>Texte</p>
                        </div>
                    </article>
                </div>
                
                <div class="col-12 col-md-6 col-sm-8" >
                    <article>
                        <div>
                            <a href="'''+chemin+'''/saisie/saisieEtudeTemporelle.py">
                            <h3>Etude temporelle</h3>
                            </a>
                            <p>Texte</p>
                        </div>
                    </article>
                </div>'''

    return vstatistiques
