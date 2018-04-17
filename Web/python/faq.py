conf=Import('../data/config.py')
template=Import('template.py')
chemin = conf.chemin()

def index():
    result = template.entete(chemin)
    result += template.menu(chemin)
    result += template.titre("FAQ", 0)
    result += faq()
    result += template.footer(chemin)
    return result

def faq():
    vfaq = '''
        <section id="faq">
        <h1>Comment est votre blanquette ?</h1>
        <p>Elle est bonne<p>
        <h1>On me dit le plus grand bien de vos harengs-pomme à l'huile </h1>
        <p>Le patron vous en apportera un ramequin, vous vous ferez une idée<p>
        
        </section>
    '''
    return vfaq