conf=Import('../data/config.py')
template=Import('template.py')
chemin = conf.chemin()

def index():
    result = template.entete(chemin)
    result += template.menu(chemin)
    result += template.titre("Adrien Caillet", 0)
    result += caillet()
    result += template.footer(chemin)
    return result

def caillet():
    vcaillet = '''
    
    <style>
      .page{
    width : 780px;
    margin : auto;
    font-size : 16px;
    font-family : Calibri;
}

body{
     background-image: linear-gradient(to right, green, blue);
    color : white;
}

#presentation{
    border : 3px solid red;
    font-size : 20px;
    color : red;
}

.infophoto{
    height : 250px;
}

.info{
    float : left;
    color : black;
    text-align : justify;
}

.photo{
    float : right;
}

section{
    margin-bottom : 70px;
    text-align = justify;
}

.sec-gauche{
    float : left;
    font-weight : bold;
    font-size : 20px;
    font-style : italic;
    text-align : left;
}

.sec-droite{
    margin-left : 150px;
    margin-top : 0px;
    text-align : left;
}

strong{
    font-size : 16px;
}



h2{
    font-size : 28px;
    color : red;
    border-bottom : 3px solid red;
}

h3{
    font-size : 16px;
    color : red;
    margin-bottom : 0px;
}

#spécial{
    color : red;
    margin-top : 0px;
    margin-bottom : 45px;
}


#sec-gauche-1{
    margin-bottom : 70px;
    margin-top : 0px;
}

#sec-gauche-2{
    margin-bottom : 90px;
    margin-top : 0px;
}

#sec-gauche-3{
    margin-bottom : 64px;
    margin-top : 0px;
}

#sec-gauche-4{
    margin-bottom : 40px;
    margin-top : 0px;
}

#sports{
    margin-bottom : 40px;
}

    </style>

    <head>

        <title>Mon CV</title>
        <meta charset="UTF-8">
        <link rel = "stylesheet", href = "cv.css">
    </head>

    <body>

        <div class = "page">
            <div class = "infophoto">
                <div class = "info">
                        <p id = "presentation">20 ans
                        30 chemin de la Cybellerie,<br/>
                        86280 Saint-Benoit, France<br/>
                        +33 6 14 11 01 37<br/>
                        adrien.caillet@alumni.enac.fr<br/>
                            Permis B
                        </p>
                    
                </div>

                <div class = "photo">
                    <img src = "''' + chemin + '''/images/adrien2.jpg" width = 200>
                </div>
            </div>

            <div section>
                <h2>Formations</h2>

                <div class = "sec-gauche">
                    <p id = "sec-gauche-1">2017 - en cours</p>
                    <p id = "sec-gauche-2">2015 - 2017</p>
                    <p>2012 - 2015</p>
                </div>

                <div class = "sec-droite">
                    <p><h3>Ecole nationale de l'aviation civile [ENAC]; Toulouse, France;</h3>
                    Formation <strong>élève ingénieur IENAC [1ère année, license 3],</strong> Diplôme accrédité par la Commission des titres d'ingénieur [CTI]; <p/>
                    <p><h3>Lycée Camille Guérin, Poitiers, France;</h3>
                    Classe préparatoire physique et science de l'ingénieur [PSI];<br/>Sujet TIPE [Travail d'Initiative Personnelle Encadrée] : Asservissement en position d'une éolienne;<br/></p>
                    <p><h3>Lycée camille Guérin, Poitiers, France;</h3>
                    Baccalauréat scientifique, mention très bien, section européenne anglais.<p/>
                </div>
            </div>

            <div section>
                <h2>Expériences</h2>

                <div class = "sec-gauche">
                    <p id = "sec-gauche-3">Septembre 2017<br>
                    En cours</p>
                    <p id = "sec-gauche-4">Septembre 2017<br>
                    En cours</p>
                    <p>Juillet 2012</p>
                </div>

                <div class = "sec-droite">
                    <p><h3>Membre actif du club robotique de l'ENAC</h3>
                    Paricipation à la coupe de France de robotique<br/>
                    Réalisation du robot secondaire pour la coupe<br/>
                    Responsable intégration;</p>
                    <p><h3>Trésorier d'ENVOL, Junior Entreprise de l'ENAC</h3>
                    Gestion des fonds de l'association, des déclaratifs sociaux et fiscaux<br/>
                    Edition des factures et bulletins de versement;</p>
                    <p><h3>Voyage humanitaire à Madagascar, Assciations FANATENANE / ANCRE</h3>
                    Aide à l'organisation du voyage : récole de fonds<br/>
                    Aide au sein du centre à Fanatenane<br/>
                    Construction d'un bungalow.</p>
                </div>

            </div>

            <div section>
                <h2>Compétences</h2>

                <div class = "sec-gauche">
                    <p id = "spécial">Langues : </p>
                    <p id = "spécial">Informatique : </p>
                </div>

                <div class = "sec-droite">
                    <p><strong>Anglais: </strong>Courant<br/>
                        <strong>Espagnol: </strong>Bon niveau;</p>
                    <p>Bon niveau en <strong>Python</strong><br/>
                    Utilisation de <strong>QT</strong>, Utilisation de <strong>Eagle</strong><br/>
                    Pratique du logiciel <strong>SolidWorks</strong>, Notions langage <strong>C</strong> (Arduino)<br/>
                    Bonne maîtrise du <strong>Pack office</strong> [Word, Excel, PowerPoint].</p>
                </div>
            </div>

            <div section>
                <h2>Centres d'intérêts</h2>

                <div class = "sec-gauche">
                    <p id = "spécial">Sports :</p>
                    <p id = "spécial">Divers :</p>
                </div>

                <div class = "sec-droite">
                    <p id = "sports">Course à pied [club d'athétisme pendant 12 ans - spécialités: demi-fond, triple saut], tennis;</p>
                    <p>Lecture, Voyages.</p>
                </div>

            </div>

        </div>


    </body>


    '''
    return vcaillet