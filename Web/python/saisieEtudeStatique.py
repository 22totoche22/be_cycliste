conf=Import('../data/config.py')
template=Import('../python/template.py')
chemin = conf.chemin()


def index():
    result = template.entete(chemin)
    result += template.menu(chemin)
    result += template.titre("Etude Statique",0)
    result += statique()
    result += template.footer(chemin)
    return result

def statique():

    statique = '''
    <link rel="stylesheet" href="http://cdn.dhtmlx.com/5.0/dhtmlx.css" 
    type="text/css"> 
<script src="http://cdn.dhtmlx.com/5.0/dhtmlx.js" 
    type="text/javascript"></script>'''

    return statique