conf=Import('../data/config.py')
bdd=Import('../data/bdd.py')
template=Import('template.py')
chemin = conf.chemin()


def index(essai=''):
    msg = template.entete(chemin)
    msg += template.menu(chemin)
    msg += template.titre("mot de passe oublié",0)
    msg += inscription(essai)
    msg += template.footer(chemin)
    return msg


def inscription(essai=''):
        inscription = '''
        
            <style>
            #comp{
            color : red;
            
            }
            #insriptionfail{
            color : red}
            </style>
            <section id="inscription">
    
                <div class="row">
                    <div class="col-12 col-md-4 col-sm-6 offset-sm-3 offset-md-4 form-group" onsubmit="return fverif">
                        <label> Veuillez nous rappeler votre mail</label>
                        <form id="inscrip" method="post" action = "fpwd" enctype="multipart/form-data">
        '''
        if essai != '':
           inscription += ''' <label id="insriptionfail"> Vous n'êtes pas dans notre base de donnée</label>
            '''
        inscription +='''
                            
                
                            <li><input   name="email" placeholder="email" type="email" required/></li>

                            <button class="button" type="submit" >Envoyer</button>
                        </form>
                    </div>
                </div>
            </section>
            '''
        return inscription




def fpwd(email):
    list = affiche_pwd()
    pwd = None
    if email in list[0]:
        result = template.entete(chemin)
        result += template.menu(chemin)
        result += template.titre("Inscription",0)
        result += "<section>"
        for k,i in enumerate(list[0]):
            if i == email:
                pwd = list[1][k]
        try:
            envoie_mdp(email, pwd)
            result += "<div>Un mail vous a été envoyé, pensez à changer rapdiement votre mot de passe</div>"
        except Exception:
            result += "<div> Il y a eu un soucis, recommencez ! </div>"

        result += "</section>"
        result += template.footer(chemin)
    else:
        return index("non")
    return result


def affiche_pwd():
    list_mail = []
    list_pwd = []
    liste = bdd.afficheurmail()
    for (mail,pwd) in liste:
        list_mail.append(mail.decode())
        list_pwd.append(pwd.decode())

    return list_mail,list_pwd

def envoie_mdp(email,mdp):
    import smtplib

    TO = email
    SUBJECT = 'Votre mot de passe'
    TEXT = 'Votre mot de passe est : '+mdp

    # Gmail Sign In
    gmail_sender = "totochetotochetotoche@gmail.com"
    gmail_passwd = "totocheTOTOCHE86"

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(gmail_sender, gmail_passwd)

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    server.sendmail(gmail_sender, [TO], BODY)

    server.quit()
