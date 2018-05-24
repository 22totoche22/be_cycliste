conf = Import('../data/config.py')
template = Import('template.py')
chemin = conf.chemin()


def index():
    result = template.entete(chemin)
    result += template.menu(chemin)
    result += template.titre("Allan Denis", 0)
    result += denis()
    result += template.footer(chemin)
    return result


def denis():
    vdenis = '''

    <style>
      ..page{
    width : 780px;
    margin : auto;
    font-size : 16px;
    font-family : Calibri;
}

body{
     background-image: linear-gradient(to right, green, blue);
    color : white;
}

.photo{
    margin-top : 200px;
}

#image{
    height : 50px;
    width : 50px;
}

#coordonnées{
    float : left;
    margin-left : 250px;
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
    width : 200px;
    margin-right : 25px;
    text-align : left;
}

.sec-droite{
    margin : auto;
    text-align : left;
}

.sec-gauche-main{
    margin-left : 50px;
    float : left;
    font-style : italic;
    font-size : 20px;
    width : 100px;
    text-align : left;
}



.sec-droite-main{
    margin-left : 300px;
    float : right
    margin-top : 0px;
}


.photo{
    margin-left : 100px;
    margin-bottom : 100px;
    margin-top : 0px;
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
    margin-top : 0px;
    margin-bottom : 40px;
}

#sec-gauche-2{
    margin-top : 0px;
    margin-bottom : 70px;
}

#sec-gauche-3{
    margin-top : 0px;
    margin-bottom : 48px;
}

#sec-gauche-4{
    margin-top : 0px;
    margin-bottom : 80px;
}

#sec-gauche-5{
    margin-bottom : 20px;
    margin-top : 0px;
}

#sec-gauche-6{
    margin-top : 0px;
    margin-bottom : 40px;
}

#sec-gauche-7{
    margin-top : 0px;
    margin-bottom : 20px;
}

#sec-gauche-8{
    margin-top : 0px;
    margin-bottom : 100px;
}
    </style>
    

    <head>

        <title>Mon CV</title>
        <meta charset="UTF-8">
        <link rel = "stylesheet", href = "cv.css">
    </head>

    <body>

          <div class = "photo">
                    <img src = "''' + chemin + '''/images/allan2.jpg" width = 150>
                </div>

        <div class = "page">
            <div class = "sec-gauche-main">
                <h2>Profil</h2>
                <p>20 ans</p>
                <p>allandenis974@gmail.com</p>
                <p>22 Rue Mage<br/>
                31000 Toulouse</p>
                <p>06 59 73 91 70</p>
                <p>Français</p>
                <p>Permis B - Permis côtier</p>
                <p>Mobilité : Toute la France</p>
                <hr/>
                <br/>
                <hr/>
                <br/>
                <hr/>



                </div>

            <div class = "sec-droite-main">


                <div section>
                    <h2>Diplôme & Formations</h2>

                    <div class = "sec-gauche">
                        <p id = "sec-gauche-1">Depuis 2017</p>
                        <p id = "sec-gauche-2">2015 - 2017</p>
                        <p>2015</p>
                    </div>

                    <div class = "sec-droite">
                        <p><h3>Ecole nationale de l'aviation civile Toulouse</h3>
                        Première année cursus ingénieur aérospatial<p/>
                        <p><h3>Classe préparatoire aux grandes écoles scientifiques</h3>
                        Lycée Leconte de Lisle Saint-Denis - La Réunion<br/>
                        MPSI/MP</p>
                        <p><h3>Baccalauréat série S-SVT</h3>
                        Mention très bien option chinois LV3<p/>
                    </div>
                </div>

                <div section>
                    <h2>Expériences</h2>

                    <div class = "sec-gauche">
                        <p id = "sec-gauche-3">2017 - 2018</p>
                        <p id = "sec-gauche-4">2016 - 2017</p>
                    </div>

                    <div class = "sec-droite">
                        <p><h3>Projet de groupe</h3>
                        Imlémentation d'une intelligence artificielle pour un jeu de Quarto sur Python</p>
                        <p><h3>Projet de groupe</h3>
                        Travail sur la théorie de la percolation à travers l'étude de la propagation d'un incendie de forêt<br/>
                        Collaboration avec l'Office Nationale des Forêts</p>

                    </div>

                </div>

                <div section>
                    <h2>Compétences</h2>

                    <div class = "sec-gauche">
                        <p id = "sec-gauche-5">Ouverture d'esprit et goût pour la découverte</p>
                        <p id = "sec-gauche-6">Persévérance, assiduité</p>
                        <p id = "sec-gauche-7">Goût pour la compétition et l'excellence</p>
                        <p id = "sec-gauche-8">Esprit d'équipe et d'entraide</p>
                        <p id = "sec-gauche-8">Apprentissage motivé et autonome</p>
                    </div>

                    <div class = "sec-droite">
                        <p>Anglais et Espagnol: courant<br/>
                           Mandarin: intermédiaire<br/>
                            Voyages en Afrique, Asie du Sud, Europe et Océanie</p>
                        <p>Pratique du saxophone en conservatoire durant 8 ans:<br/>
                        -Obtention des 2 premiers cycles du conservatoire<br/>
                        -Participation à la fanfare de l'Ecole Nationale de l'Aviation Civile</p>
                        <p>Pratique du trampoline à haut niveau depuis mes 9 ans:<br/>
                        -Champion de France en trampoline synchronisé en 2012 puis 3ème de France en 2014</p>
                        <br/>
                        <p>Pratique du badminton depuis le collège dans un cadre scolaire:<br/>
                        -Membre de l'équipe de badminton de l'Ecole Nationale de l'Aviation Civile<br/>
                        -Participation aux championnats universitaires<br/>
                        Pratique du beach-tennis depuis quelques années:<br/>
                            -Participation aux championnats du monde en 2015<p/>
                        <p>Notions du transport aérien et de la réglementation aérienne:<br/>
                        -Titulaire de la license théorique de pilote privé<br/>
                        -Notions du pilotage manuel<br/>
                        Connaissance approfondie du langage informatique Python<br/>
                        Connaissance du langage informatique R</p>
                    </div>
                </div>
            </div>
        </div>


    </body>


    '''
    return vdenis