conf=Import('data/config.py')
template=Import('python/template.py')
chemin = conf.chemin()

def index():
    result = template.entete(chemin)
    result += template.menu(chemin)
    result += template.titre("Incidents Cyclistes",1)
    result += corps()
    result += template.footer(chemin)
    return result


def corps():
    vcorps = '''
        <section id="corps">

            <div class="row">
                <div class="col-12 col-md-4 col-sm-6" >
                    <article>
                        <div>
                            <h3>Incidents</h3>
                            <p>Texte</p>
                        </div>
                    </article>
                </div>

                <div class="col-12 col-md-4 col-sm-6" >

                    <article>
                        <div>
                            <a href="'''+chemin+'''/python/Carte.py">
                            <h3>Carte</h3>
                            </a>        
                            <p>Texte</p>
                        </div>

                    </article>
                </div>

                <div class="col-12 col-md-4 col-sm-6"  >
                    <article>
                        <div>
                            <h3>Statistiques</h3>
                            <p>Texte </p>
                        </div>
                    </article>
                </div>
            </div>
        </section>
    '''
    return vcorps


