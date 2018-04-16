def entete(chemin=''):
    ventete = '''
    <!DOCTYPE HTML>
    <html lang="fr">
        <head>
                    <title>Mon premier site</title>
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
            <li>
                <a href="'''+chemin+'''/index.py">
                    <span class="fa-layers fa-2x">
                        <i class="fas fa-circle"></i>
                        <i class="fa-inverse fas fa-home" data-fa-transform="shrink-7 left-1"></i>
                    </span>
                    Accueil
                </a>
            </li>
            <li>
                <a href="'''+chemin+'''/index.py#ecole">
                    <span class="fa-layers fa-2x">
                          <i class="fas fa-circle"></i>
                          <i class="fa-inverse fas fa-plane" data-fa-transform="shrink-7"></i>
                    </span>
                    L'école
                </a>
                <ul>
                    <li><a href="https://fr-fr.facebook.com/events/1871861779808708/" target="blank"><i class="fas fa-baseball-ball"></i> EAG 2018</a></li>
                    <li><a href="'''+chemin+'''/index.py#contacter"><i class="fas fa-phone"></i> Nous Contacter</a></li>
                </ul>
            </li>
            <li>
                <a href="'''+chemin+'''/python/clubs.py">
                    <span class="fa-layers fa-2x">
                          <i class="fas fa-circle"></i>
                          <i class="fa-inverse fas fa-list" data-fa-transform="shrink-7"></i>
                    </span>
                    Les clubs
                </a>
            </li>
            <li>
        '''

    menu+='''
            <a href="'''+chemin+'''/python/connecter.py">
                <span class="fa-layers fa-2x">
                        <i class="fas fa-circle"></i>
                        <i class="fa-inverse fas fa-user" data-fa-transform="shrink-7"></i>
                </span>
                Se connecter
            </a>
        '''
    menu+='''
            </li>
        </ul>
    </nav>
   '''


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
                    <p>Trois années inoubliables</p>
             </header>
            '''
    return titre


def footer(chemin=''):
    vfooter = '''
            <footer>&copy All right reserved ENAC
            </footer>
            <script type="text/javascript" src= " '''+chemin+'''/js/jquery-3.3.1.min.js" ></script>
            <script type="text/javascript" src= " '''+chemin+'''/library/fontawesome-free-5.0.6/svg-with-js/js/fontawesome-all.min.js" ></script>
            <script type="text/javascript" src= " '''+chemin+'''/library/bootstrap-4.0.0-dist/js/bootstrap.min.js" ></script>
            <script type="text/javascript" src= " '''+chemin+'''/library/bootstrap-table/dist/bootstrap-table.min.js" ></script>
        </body>
        </html>
        '''
    return vfooter
