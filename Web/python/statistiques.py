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
                <label class="" >quartier/petite commune : </label> <input id="quartier" type="text" name="quartier" value="" onkeyup="count()" placeholder="Capitole de Toulouse, Arnaud Bernard... Merci de respecter la syntaxe">
                <label class="" >secteur : </label><input id="secteur" type="text" name="secteur" value="" onkeyup="countbis()" placeholder="1.1, 1.2, 4.1 ..." >
                <label class="" >Grande commune : </label><input id="commune" type="text" name="secteur" value="" onkeyup="countbisbis()" placeholder="Toulouse..." >
               </form>
            </div>
            </div>
    
    <div id="chart" class="row">
    <div class="col-12 col-md-4 col-sm-6" >
        <canvas id="myChart"></canvas></div>
        <div class="col-12 col-md-4 col-sm-6" >
        <canvas id="my_Chart"></canvas></div>
        <div class="col-12 col-md-4 col-sm-6" >
        <canvas id="my__Chart"></canvas></div>
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
                    options: {scales: {
  yAxes: [{
    ticks: {
     suggestedMin: 0
     }
   }]
  }}
                 });
            }
    </script>
    <script>
    function cat(){
        liste = '''+str(catincident())+''';
        var li = '''+str(len(catincident()))+''';
        result1 =[];
        result2 =[];
        var i =0;
        while(i<li){
            result1.push(liste[i][1]);
            result2.push(liste[i][0]);
            i++;
        }
        var ctx = document.getElementById("my__Chart").getContext('2d');
                var chart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: result1,
                        datasets: [{
                            label: "Nombre total d'incidents par catégorie au total",
                            backgroundColor: 'rgb(255, 99, 132)',
                            borderColor: 'rgb(255, 99, 132)',
                            data: result2,
                        }]
                    },
                    options: {scales: {
  yAxes: [{
    ticks: {
     suggestedMin: 0
     }
   }]
  }}
                 });
        
    }
    
    function test(valeur){
        liste = '''+str(ftest())+''';
        var li = '''+str(len(ftest()))+''';
        result1 =[];
        result2 =[];
        var result3=[];
        var i =0;
        var compte = 0;
        while(i<li){
        if (valeur == liste[i][1]){
                
                result1.push(liste[i][2])
                }
         
            i++;
        }
        console.log(result1)
        var j =0;
        var k = result1.length


        while (j<k){
            if (result2.includes(result1[j])){
                console.log('lol')
                result3[result2.indexOf(result1[j])]++;
            }
            else{result2.push(result1[j]);
            result3.push(1);
            
            }
        j++;
        }
        
        var ctx = document.getElementById("my__Chart").getContext('2d');
                var chart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: result2,
                        datasets: [{
                            label: "Nombre 'incidents par catégorie ",
                            backgroundColor: 'rgb(255, 99, 132)',
                            borderColor: 'rgb(255, 99, 132)',
                            data: result3,
                            ticks: { min: 0}
                        }]
                    },
                    options: {scales: {
  yAxes: [{
    ticks: {
     suggestedMin: 0
     }
   }]
  }}
                 });
      
    }
    
    function testsecteur(valeur){
        liste = '''+str(ftestsecteur())+''';
        var li = '''+str(len(ftestsecteur()))+''';
        result1 =[];
        result2 =[];
        var result3=[];
        var i =0;
        var compte = 0;
        while(i<li){
        if (valeur == liste[i][1]){
                
                result1.push(liste[i][2])
                }
         
            i++;
        }
        console.log(result1)
        var j =0;
        var k = result1.length


        while (j<k){
            if (result2.includes(result1[j])){
                console.log('lol')
                result3[result2.indexOf(result1[j])]++;
            }
            else{result2.push(result1[j]);
            result3.push(1);
            
            }
        j++;
        }
        
        var ctx = document.getElementById("my__Chart").getContext('2d');
                var chart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: result2,
                        datasets: [{
                            label: "Nombre 'incidents par catégorie ",
                            backgroundColor: 'rgb(255, 99, 132)',
                            borderColor: 'rgb(255, 99, 132)',
                            data: result3,
                        }]
                    },
                    options: {scales: {
  yAxes: [{
    ticks: {
     suggestedMin: 0
     }
   }]
  }}
                 });
      
    }
    
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
        choose("my_Chart",result[1]/result[0]*100,"taux cloture en %",quartier.value);
        test(quartier.value);
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
        testsecteur(secteur.value);
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
        cat();
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
    for (commune,nbcree,nbclot) in liste:
        result.append([commune.decode(), str(nbcree),nbclot.decode()])
    return result

def catincident():
    result = []
    liste = bdd.categorieincident()
    for (nb,nom) in liste:
        result.append([str(nb),nom.decode()])
    return result


def ftest():
    result = []
    liste = bdd.test()
    for (id,lieu,nom) in liste:
        result.append([str(id),lieu.decode(),nom.decode()])
    return result

def ftestsecteur():
    result = []
    liste = bdd.testsecteur()
    for (id, secteur,nom) in liste:
        result.append([str(id), secteur.decode(), nom.decode()])
    return result