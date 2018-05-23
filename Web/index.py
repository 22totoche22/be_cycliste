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
    if "login" in Session():
        if Session()["id"] in bdd.aff_analy():
            vcorps = '''
                <section id="corps">
        
                    <div class="row">
                        <div class="col-12 col-md-4 col-sm-6" >
                            <article>
                                <div>
                                    <a href="'''+chemin+'''/python/saisieCarte.py">                      
                                    <h3>Incidents</h3>
                                    <img src="''' + chemin + '''/images/incident.jpg">
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
                                    <img src="''' + chemin + '''/images/carte.jpg">
                                    </a>        
                                    <p>Carte des incidents cyclistes dans la région toulousaine</p>
                                    
                                </div>
        
                            </article>
                        </div>
    
                    <div class="col-12 col-md-4 col-sm-6"  >
                        <article>
                            <div>
                                <a href="'''+chemin+'''/python/statistiques.py">
                                <h3>Statistiques</h3>
                                <img src =" '''+chemin+''' /images/graphique.gif">
                                </a>
                                <p>Consultez les données mise en graphiques des incidentes cyclistes </p>
                            </div>
                        </article>
                    </div>
                </div>
            </section>
    '''
        else:
            vcorps = '''
                <section id="corps">
        
                    <div class="row">
                        <div class="col-18 col-md-6 col-sm-9" >
                            <article>
                                <div>
                                    <a href="'''+chemin+'''/python/saisieCarte.py">                      
                                    <h3>Incidents</h3>
                                    <img src="''' + chemin + '''/images/incident.jpg">
                                    </a>
                                    <p>Reporter un incident</p>
                                </div>
                            </article>
                        </div>
        
                        <div class="col-18 col-md-6 col-sm-9" >
        
                            <article>
                                <div>
                                    <a href="''' + chemin + '''/python/carte.py">
                                    <h3>Carte</h3>
                                    <img src="''' + chemin + '''/images/carte.jpg">
                                    </a>        
                                    <p>Carte des incidents cyclistes dans la région toulousaine</p>
                                    
                                </div>
        
                            </article>
                        </div>
                    </div>
                </section>
            '''
    else:
        vcorps = '''
                        <section id="corps">

                            <div class="row">
                                <div class="col-18 col-md-6 col-sm-9" >
                                    <article>
                                        <div>
                                            <a href="''' + chemin + '''/python/connecter.py">                      
                                            <h3>Incidents</h3>
                                            <img src="''' + chemin + '''/images/incident.jpg">
                                            </a>
                                            <p>Reporter un incident</p>
                                        </div>
                                    </article>
                                </div>

                                <div class="col-18 col-md-6 col-sm-9" >

                                    <article>
                                        <div>
                                            <a href="''' + chemin + '''/python/carte.py">
                                            <h3>Carte</h3>
                                            <img src="''' + chemin + '''/images/carte.jpg">
                                            </a>        
                                            <p>Carte des incidents cyclistes dans la région toulousaine</p>

                                        </div>

                                    </article>
                                </div>
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
                        <article>
                            <p><a href="https://www.cols-cyclisme.com/">Col-Cyclisme</a></p>
                            <br>Les montées près de chez vous</br>
                        </article>
                        <article>
                            <p><a href="https://www.eau-cyclisme.com/">Eau-Cyclisme</a></p>
                            <br>La carte des points d'eau pour vos sorties cyclistes</br>
                        </article>
                    </ul>
                </nav>
            </div>
        </article>
    </section>
        '''

    return liens
