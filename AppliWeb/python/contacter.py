conf=Import('../data/config.py')
template=Import('template.py')
chemin = conf.chemin()


def contacter():
    vcontact = '''
        <section id="contacter">
            <h2>Des questions ou des commentaires?</h2>
            '''

    # if "nom" in Session() :
    #     vcontact += "Bonjour " + Session()["prenom"] + "<br />Vos données ont été enregistrées"
    # else :
    #     vcontact += "Vos données ont été enregistrées"

    vcontact += '''
            <div class="row">
                <div class="col-12 col-md-10 offset-md-1 form-group">
                    <form method="post" action="'''+chemin+'''/python/page2.py/fcontacter">
                        <input name="name" placeholder="Nom Prénom" type="text" />
                        <input name="email" placeholder="Email" type="text" />
                        <textarea name="message" placeholder="Message"></textarea>
                        <button class="button" type="submit">Envoyer</button>
                    </form>
                </div>
            </div>
        </section>
        '''

    return vcontact
