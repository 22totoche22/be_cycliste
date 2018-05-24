conf = Import('../data/config.py')
template = Import('template.py')
chemin = conf.chemin()


def index():
    result = template.entete(chemin)
    result += template.menu(chemin)
    result += template.titre("Matthias Petit", 0)
    result += petit()
    result += template.footer(chemin)
    return result


def petit():
    vpetit = '''
    
    <style>
    
    .page{
    width : 780px;
    margin : auto;
    font-size : 16px;
    font-family : Calibri;
}

#h1-bis{
    border : 5px solid white;
    text-align : center;
    color : white;
}

body{
     background-image: linear-gradient(to right, green, blue);
    color : white;
}

.infophoto{
    height : 250px;
}

.info{
    float : left;
    margin : auto;
    color : white;
    text-align : justify;
}

.photo{
    float : right;
    width : 100px;
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
    width : 150px;
    margin-right : 25px;
}

.sec-droite{
    margin-top : 0px;
    text-align : justify;
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
    margin-bottom : 45px;
    margin-top : 0px;
}

#sec-gauche-2{
    margin-bottom : 95px;
    margin-top : 0px;
}

#sec-gauche-3{
    margin-bottom : 45px;
    margin-top : 0px;
}

#sec-gauche-4{
    margin-bottom : 60px;
    margin-top : 0px;
}

#sec-gauche-5{
    margin-bottom : 75px;
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

                        <p>Matthias PETIT<br/>
                            24/04/1998 (20 ans) <br/>
                        ENAC, Résidence LB325, 7 Avenue Edouard Belin<br/>
                            31400 Toulouse<br/>
                            <U><B>Tél: </B></U>06 52 65 37 43<br/>
                            <U><B>Mail: matthias.petit36@gmail.com</B></U></p>
                    </p>
                </div>

                <div class = "photo">
                    <img src = "''' + chemin + '''/images/matthias.jpg" width = 150>
                </div>
            </div>

            <h1 id = "h1-bis"><B>ELEVE INGENIEUR 1ère ANNEE</B><br/>
                <strong>ECOLE NATIONALE DE L'AVIATION CIVILE</strong></h1>

            <div section>
                <h2>Formation :</h2>

                <div class = "sec-gauche">
                    <p id = "sec-gauche-1">2017 - 2020</p>
                    <p id = "sec-gauche-2">2015 - 2017</p>
                    <p>2012 - 2015</p>
                </div>

                <div class = "sec-droite">
                    <p><h3>Ecole nationale de l'aviation civile</h3>
                   Cycle <B>IENAC</B> (ingénieur ENAC)</p>
                    <h3>Lycée Louis-le-Grand,</h3> Paris V
                    <p>Classe préparatoire <B>MPSI - MP</B> (Mathématiques et Physique)<br/>
                        Option: Sciences Industrielles pour l'Ingénieur</p>
                    <p><h3>Lycée Pierre et Marie Curie, Châteauroux</h3>
                    Diplôme: <B>Baccalauréat scientifique</B> option Mathématiques<br/>
                    Mention: <B> Très Bien</B> (félicitations du jury)<p/>
                </div>
            </div>

            <div section>
                <h2>Expérience :</h2>

                <div class = "sec-gauche">
                    <p id = "sec-gauche-3">Novembre 2017 - Janvier 2018</p>
                    <p id = "sec-gauche-4">Septembre 2016 - Juin 2017</p>

                </div>

                <div class = "sec-droite">
                    <p>Projet de <B>programmation Python</B> en groupe<br/>
                        Apprentissage par renforcement d'Intelligence Artificielle pour des jeux d'arcade, méthode du Q-Learning</p>
                    <p>Travail d'Initiative Personnelle Encadré (<B>TIPE</B>)<br/>
                   Gammes, tempéraments et intervalles en musique, liens avec le développement de nombres en fraction continue</p>
                </div>

            </div>

            <div section>
                <h2>Compétences :</h2>

                <div class = "sec-gauche">
                    <p id = "sec-gauche-5">Informatique</p>
                    <p id = "sec-gauche-1">Anglais</p>
                    <p>Espagnol</p>

                </div>

                <div class = "sec-droite">
                    <p>Formation approfondie et exhaustive de l'ENAC<br/>
                        Programmation <B>Python</B>, Interfaces <B>Qt</B>, Systèmes d'exploitation, Réseaux, Bases de données, Applications Web, Bureautique</p>
                    <p>Parfaite maîtrise, <B>960 points</B> au TOEIC blanc (examen ENAC)<br/>
                        Séjour d'études linguistiques d'une semaine à <B>Oxford</B> (OISE</p>
                    <p>Intermédiaire</p>
                </div>
            </div>

            <div section>
                <h2>Centres d'intérêt :</h2>

                <div class = "sec-gauche">
                    <p>Piano et solfège</p>
                    <p>jeu d'échecs</p>
                </div>

                <div class = "sec-droite">
                    <p>10 ans de formation en Conservatoire, concerts de jazz</p>
                    <p>Ancien joueur de club, tournois nationaux</p>
                </div>

            </div>

        </div>


    </body>


    '''
    return vpetit