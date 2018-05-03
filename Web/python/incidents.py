conf=Import('../data/config.py')
template=Import('template.py')
chemin = conf.chemin()


def index():
    result = template.entete(chemin)
    result += template.menu(chemin)
    result += template.titre("Reporter un incident",0)
    result += incidents()
    result += template.footer(chemin)
    return result

def incidents():
    vincidents='''
        <section id="incidents">
            <div class="row">
                <div class="col-12 col-md-4 col-sm-6" >
                    <article>
                        <div>
                            <a href="'''+chemin+'''/saisie/saisieCoordonnees.py">
                            <h3>Avec les coordonnées GPS</h3>
                            </a>
                            <p>Texte</p>
                        </div>
                    </article>
                </div>

                <div class="col-12 col-md-4 col-sm-6" >

                    <article>
                        <div>
                            <a href="'''+chemin+'''/saisie/saisieCarte.py">
                            <h3>Avec un point sur la carte</h3>
                            </a>        
                            <p>Texte</p>
                        </div>

                    </article>
                </div>

                <div class="col-12 col-md-4 col-sm-6"  >
                    <article>
                        <div>
                            <a href="'''+chemin+'''/saisie/saisieAdresse.py">
                            <h3>Avec l'adresse postale</h3>
                            </a>
                            <p>Texte </p>
                        </div>
                    </article>
                </div>
            </div>
        </section>
    '''
    return vincidents
