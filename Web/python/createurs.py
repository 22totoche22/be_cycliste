conf=Import('../data/config.py')
template=Import('template.py')
chemin = conf.chemin()

def index():
    result = template.entete(chemin)
    result += template.menu(chemin)
    result += template.titre("Créateurs", 0)
    result += createurs()
    result += template.footer(chemin)
    return result

def createurs():
    vcreateurs = '''
        <section id="createurs">

            <div class="row">
                <div class="col-ç col-md-3 col-sm-4" >
                    <article>
                        <div>
                            <h3>Adrien Caillet</h3>
                            <img src="C:/karrigell/www/images/adrien.jpg alt="adrien" title="Adrien Caillet"/>
                        </div>
                    </article>
                </div>
                
                <div class="col-ç col-md-3 col-sm-4" >
                    <article>
                        <div>
                            <h3>Allan Denis</h3>
                            <img src="C:/karrigell/www/images/allan.jpg alt="allan" title="Allan Denis"/>
                        </div>
                    </article>
                </div>
                
                <div class="col-ç col-md-3 col-sm-4" >
                    <article>
                        <div>
                            <h3>Matthias Petit</h3>
                        </div>
                    </article>
                </div>
                
                <div class="col-ç col-md-3 col-sm-4" >
                    <article>
                        <div>
                            <h3>Armand Vergnes</h3>
                        </div>
                    </article>
                </div>

                
            </div>
        </section>
    '''
    return vcreateurs