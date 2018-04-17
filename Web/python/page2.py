conf=Import('../data/config.py')
bdd=Import('../data/bdd.py')
template=Import('template.py')
chemin = conf.chemin()


def fcontacter(name='', email='', message=''):
    result = template.entete(chemin)
    result += template.menu(chemin)
    result += template.titre("Nous contacter",0)
    result += "<section>"
    msg = bdd.insertCommentData(email, message, name)
    if msg is None:
        result += "<div>Vos données ont été enregistrées</div>"
    result += "<div class='comm'>Liste des commentaires enregistrés dans la base de données</div>"
    result += afficheComment()
    result += "</section>"
    result += template.footer(chemin)
    return result


def afficheComment():
    result = ''
    liste = bdd.affichCommentData()

    for (id, nom, comment, email) in liste:
        result += '<div>'
        result += str(id)+' '
        result += nom.decode()+' '
        result += comment.decode()+' '
        result += email.decode()+' '
        result += '</div>'

    return result



