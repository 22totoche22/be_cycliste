conf = Import('../data/config.py')
template = Import('template.py')
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
    margin-left : 100px;
    margin-top : 20px;
    font-size : 20px;
    color : red;
}

.infophoto{
    height : 250px;
}

.info{
    float : left;
    color : black;
}

.photo{
    float : right;
}

section{
    margin-bottom : 70px;
    text-align = justify
}

.sec-gauche{
    float : left;
    font-weight : bold;
    font-size : 20px;
    font-style : italic;
    margin-right : 25px;
}

.sec-droite{
    margin-left : 150px;
    margin-top : 0px;
}

strong{
    font-size : 16px;
}



h2{
    font-size : 28px;
    color : red;
    text-transform : uppercase;
    border-bottom : 3px solid red;
}

h3{
    font-size : 16px;
    color : red;
    margin-bottom : 0px;
}


#sec-gauche-1{
    margin-bottom : 40px;
    margin-top : 0px;
}

#sec-gauche-2{
    margin-bottom : 70px;
    margin-top : 0px;
}

#sec-gauche-3{
    margin-bottom : 80px;
    margin-top : 0px;
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
                        <p id = "presentation">13/07/1996 (21 ans)<br/>
                        à Aix-en-Provence, Frnace<br/>
                        CA223, 7 Avenue Edouard Belin CS54005<br/>
                            31055 TOULOUSE CEDEX 04<br/>
                            +33 6 74 18 82 61<br/>
                       armand.vergnes@alumni.enac.fr
                        </p>

                </div>

                <div class = "photo">
                    <img src = "''' + chemin + '''/images/armand.jpg" width = 200>
                </div>
            </div>

            <div section>
                <h2>Formations:</h2>

                <div class = "sec-gauche">
                    <p id = "sec-gauche-1">2011 - 2014</p>
                    <p id = "sec-gauche-1">2014 - 2017</p>
                    <p>2017 - 2020</p>
                </div>

                <div class = "sec-droite">
                    <p><h3>Lycée Vauvenargues, Aix-en-Provence</h3>
                    Baccalauréat Scientifique option Science de l'ingénieur, Mention très Bien<p/>
                    <p><h3>Lycée Champollion, Grenoble</h3>
                    Classes préparatoires scientifiques MPSI-MP-MP*</p>
                    <p><h3>Ecole Nationale de l'Aviation Civile, Toulouse</h3>
                    Cours sur la réglementation aérienne, généralités sur les aéroports, mécanique du vol, etc<p/>
                </div>
            </div>

            <div section>
                <h2>Expériences Professionnelles:</h2>

                <div class = "sec-gauche">
                    <p id = "sec-gauche-2">2017:</p>
                    <p id = "sec-gauche-1">2018:</p>
                    <p>2018:</p>
                </div>

                <div class = "sec-droite">
                    <p><h3>Projet Python à l'ENAC</h3>
                    Création d'un logiciel sur 2 mois en Python pour l'aide à la visualisation des performances de décollage et d'atterrissage d'un avion</p>
                    <p><h3>Prestataire de services pour Deliveroo, Toulouse (en cours)</h3>
                    Coursier pour Deliveroo (livraison de repas), expérience dans l'entrepreneuriat</p>
                    <p><h3>Stage à l'altiport de Courchevel:</h3>
                    Stage ouvrier de première année d'école d'ingénieur sur l'exploitation aéroportuaire dans les conditions spécifiques d'un altiport. Mise en place d'une base de données sur les interventions sur pistes pour des points sensibles de la piste.</p>
                </div>

            </div>

            <div section>
                <h2>Compétences notables:</h2>

                <div class = "sec-gauche">
                    <p id = "sec-gauche-2">Langues: </p>
                    <p id = "sec-gauche-3">Informatique: </p>
                    <p>License:</p>
                </div>

                <div class = "sec-droite">
                    <p>-Anglais, courant (985 au TOEIC blanc ENAC)<br/>
                       -Allemand, notions<br/>
                       -Italien, notions</p>
                    <p>-Maîtrise du Pack Office (Word, Excel, PowerPoint)<br/>
                       -Maîtrise du langage Python et de QT<br/>
                       -Pratique du logiciel SolidWorks</p>
                    <p>-Voiture Permis B<br/>
                       -Avion PPL théorique (actuellement en formation pratique)</p>
                </div>
            </div>

            <div section>
                <h2>Centres d'intérêts:</h2>

                <div class = "sec-gauche">
                    <p>Cyclisme sur route,</p>
                    <p>Rugby,</p>
                    <p>Volley,</p>
                    <p>VTT,</p>
                </div>

                <div class = "sec-droite">
                    <p> 4 ans de compétition avec l'AVC Aix</p>
                    <p> Membre de l'équipe de rugby de l'ENAC</p>
                    <p> Capitaine de l'équipe de la classe de 2015 à 2017 et 2 fois finaliste du tournoi du lycée</p>
                    <p> Compétitions scolaires (UNSS)</p>
                </div>

            </div>

        </div>


    </body>


    '''
    return vvergnes