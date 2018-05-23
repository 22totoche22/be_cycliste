#!C:\\python34
# -*- coding: UTF-8 -*-
# enable debugging
import mysql.connector
from mysql.connector import errorcode

conf=Import('../data/config.py')
config=conf.configBD()

def connexion():
    cnx=""
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Mauvais login ou mot de passe")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La Base de données n'existe pas.")
        else:
            print(err)
    return cnx

def close_bd(cursor,cnx):
    cursor.close()
    cnx.close()



# test de l'authentification de l'utilisateur.
# les paramètres sont ceux du formulaire dans l'ordre


def verif_connect(login='', pwd=''):
    cnx = connexion()
    cursor = cnx.cursor()
    query = "SELECT idUtilisateur, login, mdp, surnom, mail FROM Utilisateur WHERE login=%s AND mdp=%s LIMIT 1"
    param = (login, pwd)
    cursor.execute(query, param)
    liste = list(cursor)
    for (idUtilisateur, login, mdp, surnom, mail) in liste:
         Session()["nom"] = login
         Session()["surnom"] = surnom
         Session()["mdp"] = mdp
         Session()["id"] = idUtilisateur
         Session()["mail"] = mail
    close_bd(cursor, cnx)
    return liste




# insertion dans la table incidents


def insertincident(lat="", long="", adresse="", description="",categorie=None,niveau=None, date="") :


    sql = "INSERT INTO Incident (niveauUrgence, description, longitude, latitude, idUtilisateur, idSousCategorie, lieu, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
    param = (niveau, description, long, lat, Session()["id"], categorie, adresse, date)

    try :
        cnx=connexion()
        cursor = cnx.cursor(prepared=True)
        results = cursor.execute(sql, param)
        msg = results
        cnx.commit()
    except mysql.connector.Error as err :
        msg = "Failed select table test: {}".format(err)
        exit(1)
    finally :
        close_bd(cursor, cnx)
    return msg


# Affichage de la table incidents


def affichincident():
    sql = "SELECT niveauUrgence, description, longitude, latitude, idUtilisateur, idSousCategorie, lieu, cloture, idIncident,date,datecloture FROM Incident;"

    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        results = cursor.execute(sql)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste


def afficheutilisateur():
    sql = "SELECT login FROM Utilisateur;"

    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        results = cursor.execute(sql)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste


def afficheurmail():
    sql = "SELECT mail,mdp FROM Utilisateur;"

    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        results = cursor.execute(sql)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste



def insertUtili(login,pwd,surnom,nom,prenom,mail) :


    sql = "INSERT INTO Utilisateur (login,mdp,surnom,nom,prenom,mail) VALUES (%s, %s, %s,%s,%s,%s);"
    param = (login,pwd,surnom,nom,prenom,mail)

    try :
        cnx=connexion()
        cursor = cnx.cursor(prepared=True)
        results = cursor.execute(sql, param)
        msg = results
        cnx.commit()
    except mysql.connector.Error as err :
        msg = "Failed select table test: {}".format(err)
        exit(1)
    finally :
        close_bd(cursor, cnx)
    return msg




def change_surnom(nsurnom):
    sql = "UPDATE Utilisateur SET surnom = %s WHERE idUtilisateur = %s;"
    param = (nsurnom, Session()["id"])
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        results = cursor.execute(sql, param)
        msg = results
        cnx.commit()
    except mysql.connector.Error as err:
        msg = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return msg


def change_mdp(mdp):
    sql = "UPDATE Utilisateur SET mdp=%s WHERE idUtilisateur=%s;"
    param = (mdp, Session()["id"])
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        results = cursor.execute(sql, param)
        msg = results
        cnx.commit()
    except mysql.connector.Error as err:
        msg = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return msg



def recup_categorie():
    sql = "SELECT idSousCategorie, nomSousCategorie, nomCategorie FROM sousCategorie JOIN Categorie ON sousCategorie.idCategorie = Categorie.idCategorie ;"

    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        results = cursor.execute(sql)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste

def cloturincident(idincident, raisoncloture,date):
    sql = "UPDATE Incident SET cloture=1, raisoncloture=%s, idUtilisateurcloture=%s, datecloture=%s where idIncident=%s;"
    param = (raisoncloture,Session()["id"],date,idincident)
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        results = cursor.execute(sql, param)
        msg = results
        cnx.commit()
    except mysql.connector.Error as err:
        msg = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return msg

def affichetoututilisateur():
    sql = "SELECT idUtilisateur,login,nom,prenom, mail FROM Utilisateur;"

    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        results = cursor.execute(sql)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste

def count_ouverture ():
    sql="SELECT Utilisateur.idUtilisateur,Count(Incident.idUtilisateur) FROM Utilisateur Join Incident ON Utilisateur.idUtilisateur = Incident.idUtilisateur GROUP BY Utilisateur.idUtilisateur"
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        results = cursor.execute(sql)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste

def count_cloture ():
    sql = "SELECT Utilisateur.idUtilisateur, Count(Incident.idUtilisateur) FROM Utilisateur Join Incident ON Utilisateur.idUtilisateur = Incident.idUtilisateurcloture GROUP BY Utilisateur.idUtilisateur"
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        results = cursor.execute(sql)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste

def analyste():
    sql = "SELECT idUtilisateurAnalyste, nom,prenom FROM Analyste JOIN Utilisateur ON idUtilisateurAnalyste=idUtilisateur"
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        results = cursor.execute(sql)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste


def administrateur():
    sql = "SELECT idUtilisateurAdministrateur, nom, prenom FROM Administrateur JOIN Utilisateur ON idUtilisateurAdministrateur=idUtilisateur"
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        results = cursor.execute(sql)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste


def changeprofil(idUtili,Profil):
    if Profil ==str(1):
            sql = "INSERT INTO Analyste (idUtilisateurAnalyste) values (%s) ON DUPLICATE KEY UPDATE idUtilisateurAnalyste=idUtilisateurAnalyste;"
            param = (idUtili)
    elif Profil ==str(2):
            sql = "INSERT INTO Administrateur (idUtilisateurAdministrateur) values (%s) ON DUPLICATE KEY UPDATE idUtilisateurAdministrateur=idUtilisateurAdministrateur;"
            param = (idUtili)
    else:
        sql = "DELETE FROM Analyste WHERE idUtilisateurAnalyste = %s;"
        param = (idUtili)

    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        results = cursor.execute(sql, param)
        msg = results
        cnx.commit()
    except mysql.connector.Error as err:
        msg = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return msg

def aff_admin():
    liste_ = []
    liste = administrateur()
    for (idadmin,nom,prenom) in liste:
        liste_.append(idadmin)
    return liste_

def aff_analy():
    liste_ = []
    liste = analyste()
    for (idanal,nom,prenom) in liste:
        liste_.append(idanal)
    return liste_

def suppincident(idincident):
    sql = "DELETE FROM Incident WHERE idIncident = "+idincident+";"
    param = (int(idincident))
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        results = cursor.execute(sql)
        msg = results
        cnx.commit()
    except mysql.connector.Error as err:
        msg = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return msg

def countincident():
    sql = "SELECT lieu, COUNT(idIncident),SUM(cloture) FROM Incident GROUP BY lieu;"
    param=()
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        results = cursor.execute(sql)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste

def secteurincident():
    sql = "SELECT idSecteur, COUNT(idIncident),SUM(cloture) FROM Incident JOIN Quartier ON Incident.lieu = Quartier.nom GROUP BY idSecteur;"
    param = ()
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        results = cursor.execute(sql)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste

def communeincident():
    sql = "SELECT Commune.nom, COUNT(idIncident),SUM(cloture) FROM Incident JOIN Quartier ON Incident.lieu = Quartier.nom JOIN Commune ON Commune.idCommune = Quartier.idCommune GROUP BY Commune.idCommune;"
    param = ()
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        results = cursor.execute(sql)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste

def categorieincident():
    sql = "SELECT count(idIncident),Categorie.nomCategorie FROM Incident JOIN sousCategorie on Incident.idSousCategorie = sousCategorie.idSousCategorie JOIN Categorie ON Categorie.idCategorie = sousCategorie.idCategorie GROUP BY Categorie.idCategorie"
    param = ()
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        results = cursor.execute(sql)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste