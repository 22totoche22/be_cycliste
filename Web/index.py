conf=Import('data/config.py')
template=Import('python/template.py')
chemin = conf.chemin()
bdd=Import('../data/bdd.py')

def index():
    result = template.entete(chemin)
    result += template.menu(chemin)
    result += template.titre("Incidents Cyclistes",1)
    result += corps()
    result += liens()
    result += template.footer(chemin)
    return result


def corps():

    vcorps = '''
        <section id="corps">

            <div class="row">
                <div class="col-12 col-md-4 col-sm-6" >
                    <article>
                        <div>'''
    if "login" in Session():
               vcorps += '''             <a href="'''+chemin+'''/python/saisieCarte.py">'''
    else:
                vcorps += '''<a href="''' + chemin + '''/python/connecter.py">'''

    vcorps += '''                      
       <h3>Incidents</h3>
                            </a>
                            <p>Reporter un incident</p>
                        </div>
                    </article>
                </div>

                <div class="col-12 col-md-4 col-sm-6" >

                    <article>
                        <div>
                            <a href="''' + chemin + '''/python/carte.py">
                            <h3>Carte</h3>
                            <img src="''' + chemin + '''/images/fond.jpg">
                            </a>        
                            <p>Carte des incidents cyclistes dans la région toulousaine</p>
                            
                        </div>

                    </article>
                </div>'''
    if "login" in Session():
        if Session()["id"] in bdd.aff_analy():
            vcorps += '''

                <div class="col-12 col-md-4 col-sm-6"  >
                    <article>
                        <div>
                            <a href="'''+chemin+'''/python/statistiques.py">
                            <h3>Statistiques</h3>
                            <img src =" '''+chemin+''' /images/LogoStats.png">
                            </a>
                            <p>Texte </p>
                        </div>
                    </article>
                </div>'''
    vcorps +='''
            </div>
        </section>
       '''

    return vcorps

def liens(chemin=''):
    liens = '''
    <section id="liens">
        <article>
            <div>
                <h4>Quelques liens utiles</h4>
                <nav>
                    <ul>
                        <li>
                        Lien 1
                        </li>
                        <li>
                        Lien 2
                        </li>
                        <li>
                        Lien 3
                        </li>
                    </ul>
                </nav>
            </div>
        </article>
    </section>
        '''

    return liens
