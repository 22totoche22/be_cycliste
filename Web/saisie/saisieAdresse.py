conf=Import('../data/config.py')
template=Import('../python/template.py')
chemin = conf.chemin()


def index():
    result = template.entete(chemin)
    result += template.menu(chemin)
    result += template.titre("Saisie avec adresse",0)
    result += adresse()
    result += template.footer(chemin)
    return result

def adresse():
    vadresse='''
        <section id="adresse">
            <h5>Reporter l'incident</h5>
                <form method="post" action="bddIncidents.py" enctype="multipart/form-data">
                    <textarea name="Adresse" placeholder="Adresse postale"></textarea>
                    <select name="Cause">
                        <optgroup label="Catégorie de la cause">
                            <option value="1">Route</option>
                            <option value="2">Trafic</option>
                        </optgroup>
                    </select>
                    <button class="button" type="submit">Envoyer</button>
                </form>
        </section>
                    
    '''
    return vadresse
