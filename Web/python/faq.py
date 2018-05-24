conf=Import('../data/config.py')
template=Import('template.py')
chemin = conf.chemin()

def index():
    result = template.entete(chemin)
    result += template.menu(chemin)
    result += template.titre("Manuel d'utilisation", 0)
    result += faq()
    result += template.footer(chemin)
    return result

def faq():
    vfaq = '''
        <section id="faq">
        
        <iframe src = "''' + chemin + '''/images/tutoriel.mp4"></iframe>
        
        </section>
    '''
    return vfaq