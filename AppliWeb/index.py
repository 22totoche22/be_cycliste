conf=Import('data/config.py')
template=Import('python/template.py')
contact=Import('pyhon/contacter.py')
chemin = conf.chemin()

def index():
    result = template.entete(chemin)
    result += template.menu(chemin)
    result += template.titre("Incidents cyclistes")
    result += accueil()
    result += contact.contacter()
    result += template.footer(chemin)
    return result


def accueil():
    vaccueil = '''
        <section id="accueil">

            <div class="row">
                <div class="col-12 col-md-4 col-sm-6" >
                    <article>
                            <div>
                            <h3>Incidents</h3>
                        </div>
                    </article>
                </div>

                <div class="col-12 col-md-4 col-sm-6" >

                    <article>
                        <div>
                            <h3>Carte</h3>
                        </div>

                    </article>
                </div>

                <div class="col-12 col-md-4 col-sm-6"  >
                    <article>
                        <div>
                            <h3>Les soirées</h3>
                        </div>
                    </article>
                </div>
            </div>
        </section>
    '''
    return vaccueil


