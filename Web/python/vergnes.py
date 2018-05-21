conf=Import('../data/config.py')
template=Import('template.py')
chemin = conf.chemin()

def index():
    result = template.entete(chemin)
    result += template.menu(chemin)
    result += template.titre("Armand Vergnes", 0)
    result += vergnes()
    result += template.footer(chemin)
    return result

def vergnes():
    vvergnes = '''
        <section id="vergnes">
             <div class="CV">
                <div class="enteteCV">
                    <div class="infoCV">
                        <p>armand.vergnes@alumni.enac.fr</p>
                        <p>Né le 13 juillet 1996</p>
                    </div>
                    <div class="photoCV">
                        <img src="'''+chemin+'''/images/armand.png alt="armand" title="Armand Vergnes>                              
                        </img>
                    </div>
                </div>                  
                                           
                                           
                                           <div class="sectionCV">
                                                <h31>Mon parcours</h31>
                                                    <p><span class="titreCV">2018: Stages en aérodrome</span></p>
                                                    <br>Juillet 2018: Stage à l'altiport de Courchevel</br>
                                                    <br>Août 2018: Stage à l'aérodrome d'Aix-Les-Milles</br>
                                                    <p><span class="titreCV">2017-2020: ENAC</span></p>
                                                    <br>Ecole nationale de l'aviation civile, école d'ingénieur spécialisé
                                                     dans le transport aérien, basée à Toulouse</br>
                                                    <p><span class="titreCV">prépa</span></p>
                                                    <br></br>
                                            </div>
                                            <div class="sectionCV">
                                                <h31>Mes hobbies</h31>
                                                    <p><span class="titreCV">vélo</span></p>
                                                    <br></br>
                                                    <p><span class="titreCV">rugby</span></p>
                                                    <br></br>
                                                    <p><span class="titreCV">rando</span></p>
                                                    <br></br>
                                            </div>

        </section>
    '''
    return vvergnes