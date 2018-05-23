bdd=Import('../data/bdd.py')

def entete(chemin=''):
    ventete = '''
    <!DOCTYPE HTML>
    <html lang="fr">
        <head>
                    <title></title>
                    <meta charset="UTF-8" />
                    <link rel="stylesheet" type="text/css" href="'''+chemin+'''/css/all.css" />
                    
        </head>
        <body>
        '''
    return ventete

def menu(chemin=''):
    menu='''
    <nav>
        <ul>
        <article id="enteteConnecter">
        <li>
        '''

    if "login" in Session():
         if Session()["id"] in bdd.aff_admin():
            menu+='''
                <a href="'''+chemin+'''/python/gestionutilisateur.py">
                    Gestion des utilisateurs
                </a>
                <a href="'''+chemin+'''/python/gestionincidents.py">
                    Gestion des incidents
                </a>'''

         menu += '''<a href="'''+chemin+'''/python/mon_compte.py">
                mon compte
            </a>
            
        '''
    if "login" in Session():
         menu+='''
            <a href="'''+chemin+'''/python/connecter.py/deconnecter">
                Se déconnecter
            </a>
        '''
    else:
        menu+='''
            <a href="'''+chemin+'''/python/connecter.py">
                Se connecter
            </a>
        '''
    menu+='''
            </li>
            </article>
            <article id="enteteMenu">
            <li>
                <a href="'''+chemin+'''/python/createurs.py">
                    Créateurs
                </a>
            </li>
            <li>
                <a href="'''+chemin+'''/python/faq.py">
                    Manuel d'utilisation
                </a>
            </li>
            <li>
                <a href="'''+chemin+'''/index.py">
                    Accueil
                </a>
            </li>
        </ul>
        </article>
    </nav>
   '''

    return menu


def titre(intitule='', paragraphe=0):
    titre = '''
        <header id="top2">
                
                '''

    if "login" in Session():
          titre+="<p>Bonjour "+Session()["surnom"]+"</p>"

    titre+='''
    <hr></hr>
    <hr></hr>
    <hr></hr>
    <h1>'''+intitule+'''</h1>
    </header>
        '''

    if paragraphe==1:
        titre = '''
            <header>
                    
             '''

    if "login" in Session():
          titre+="<p>Bonjour "+Session()["surnom"]+"</p>"

    titre+='''
    <hr></hr>
    <hr></hr>
    <hr></hr>
    <h1>''' + intitule + '''</h1>
    </header>
        '''

    return titre


def footer(chemin=''):
    footer = '''
            <footer id="footer">
            <p> &copy; Tout droits reservés &copy;</p>
            </footer>
                
            
        '''

    return footer


