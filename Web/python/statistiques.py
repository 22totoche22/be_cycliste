conf=Import('../data/config.py')
template=Import('../python/template.py')
chemin = conf.chemin()
bdd=Import('../data/bdd.py')

def index():
    result = template.entete(chemin)
    result += template.menu(chemin)
    result += template.titre("Statistiques",0)
    result += statistiques()
    result += template.footer(chemin)
    return result


def statistiques():

    vstatistiques = '''
    <style>
    #chart{
    background : white;
    #myChart{
    width : 50px;
    }
    
    }
    
    </style>
    
    <section id="statistiques">
            <div class="row">
            <div class="col-12 col-md-6 col-sm-6" >
                    <article>
                        <div>
                        <iframe src=../../images/maptoulouse.pdf width=100% height=500px type='application/pdf'></iframe>
                    </article>
            </div>
            <div class="col-12 col-md-6 col-sm-6" >
            <form id="fpanel" method="POST" action = "fselectnbincident" enctype="multipart/form-data">
                <label class="" >quartier/petite commune : </label> <input id="quartier" type="text" name="quartier" value="" onkeyup="count()" placeholder="Capitole, Arnaud Bernard... Merci de respecter la syntaxe">
                <label class="" >secteur : </label><input id="secteur" type="text" name="secteur" value="" onkeyup="countbis()" placeholder="1.1, 1.2, 4.1 ..." >
                <label class="" >Grande commune : </label><input id="commune" type="text" name="secteur" value="" onkeyup="countbisbis()" placeholder="Toulouse..." >
               </form>
            </div>
            </div>
    
    <div id="chart" class="row">
    <div class="col-12 col-md-6 col-sm-6" >
        <canvas id="myChart"></canvas></div>
        <div class="col-12 col-md-6 col-sm-6" >
        <canvas id="my_Chart"></canvas></div>
    </div>
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.4.0/Chart.min.js"></script>
    <script>
    quartier.value ="";
    secteur.value ="";
    commune.value ="";
            function choose(graphe,liste,labell,title){
                var ctx = document.getElementById(graphe).getContext('2d');
                var chart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: [labell],
                        datasets: [{
                            label: title,
                            backgroundColor: 'rgb(255, 99, 132)',
                            borderColor: 'rgb(255, 99, 132)',
                            data: [liste],
                        }]
                    },
                    options: {}
                 });
            }
    </script>
    <script>
    function count(){
        liste = '''+str(selectbincident())+''';
        var li = '''+str(len(selectbincident()))+''';
        var i =0;
        var j=0;
        while(i<li){
            if (liste[i][0] == quartier.value){
                var result = [liste[i][1],liste[i][2]]
            }
            i++;
        }
        choose("myChart",result[0],"nombre d'incidents dans le quartier",quartier.value);
        choose("my_Chart",result[1]/result[0]*100,"taux cloture",quartier.value);
    }
    function countbis(){
        liste = '''+str(secteurincident())+''';
        var li = '''+str(len(secteurincident()))+''';
        var i =0;
        var j=0;
        while(i<li){
            if (liste[i][0] == secteur.value){
                var result = [liste[i][1],liste[i][2]]
            }
            i++;
        }
        choose("myChart",result[0],"nombre d'incidents dans le secteur",secteur.value);
        choose("my_Chart",result[1]/result[0]*100,"taux cloture",secteur.value);
        }
        function countbisbis(){
        liste = '''+str(communeincident())+''';
        var li = '''+str(len(communeincident()))+''';
        var i =0;
        var j=0;
        while(i<li){
            if (liste[i][0] == commune.value){
                var result = [liste[i][1],liste[i][2]]
            }
            i++;
        }
        choose("myChart",result[0],"nombre d'incidents dans la commune",commune.value);
        choose("my_Chart",result[1]/result[0]*100,"taux cloture",commune.value);
        }
    </script>

                
      '''
    return vstatistiques










def selectbincident():
    result = []
    liste = bdd.countincident()
    for (lieu,nbcree,nbclot) in liste:
        result.append([lieu.decode(),str(nbcree),nbclot.decode()])
    return result

def secteurincident():
    result = []
    liste = bdd.secteurincident()
    for (secteur,nbcree,nbclot) in liste:
        result.append([secteur.decode(),str(nbcree),nbclot.decode()])
    return result

def communeincident():
    result = []
    liste = bdd.communeincident()
    for (commune, nbcree, nbclot) in liste:
        result.append([commune.decode(), str(nbcree), nbclot.decode()])
    return result