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
            <li>
                <a href="'''+chemin+'''/index.py">
                    Accueil
                </a>
            </li>
            </li>
            <li>
                <a href="'''+chemin+'''/python/createurs.py">
                    Créateurs
                </a>
            </li>
        </ul>
    </nav>
   '''

    if "login" in Session():
          menu+="<div>Bonjour "+Session()["surnom"]+"</div>"


    return menu


def titre(intitule='', paragraphe=0):
    titre = '''
        <header id="top2">
                <h1>'''+intitule+'''</h1>
         </header>
        '''

    if paragraphe==1:
        titre = '''
            <header>
                    <h1>''' + intitule + '''</h1>
             </header>
            '''
    return titre


def footer(chemin=''):
    footer = '''
    <nav>
        <ul>
            <li>
                <a href="'''+chemin+'''/python/contact.py">
                    Laissez un commentaire
                </a>
            </li>
            <li>
                <a href="'''+chemin+'''/python/faq.py">
                    FAQ
                </a>
            </li>
        </ul>
    </nav>
                
            
        '''

    return footer

def copyright(chemin=''):
    copyright = '''
    
        <div>
            <p> Tout droits reservés à Armand Vergnes</p>
        </div>
    
    '''
    return copyright

