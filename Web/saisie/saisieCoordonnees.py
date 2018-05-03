conf = Import('../data/config.py')
template = Import('../python/template.py')
chemin = conf.chemin()


def index():
    result = template.entete(chemin)
    result += template.menu(chemin)
    result += template.titre("Saisie avec coordonnées", 0)
    result += coordonnees()
    result += template.footer(chemin)
    return result


def coordonnees():
    vcoordonnees = '''
        <section id="coordonnes">
            <h5>Reporter l'incident</h5>
                <form method="post" action="bddIncidents.py" enctype="multipart/form-data">
                    <div class="row">
                        <div class="col-12 col-md-4 col-sm-6" >
                            <article>
                                <textarea name="latitude" placeholder="Latitude"></textarea>
                            </article>
                        </div>
                        <div class="col-12 col-md-4 col-sm-6" >
                            <article>
                                <textarea name="longitude" placeholder="Longitude"></textarea>
                            </article>
                        </div>
                        <div class="col-12 col-md-4 col-sm-6" >
                            <article>
                                <input type="checkbox" name="choix[]" value="1A"/> Récupérer les coordonnées GPS de l'appareil
                            </article>
                        </div>
                    </div>
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
    return vcoordonnees
