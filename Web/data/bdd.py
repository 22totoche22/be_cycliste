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


def insertincident(lat="", long="", adresse="", description="",categorie=None,niveau=None) :


    sql = "INSERT INTO Incident (niveauUrgence, description, longitude, latitude, idUtilisateur, idSousCategorie, lieu) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    param = (niveau, description, long, lat, Session()["id"], categorie, adresse)

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
    sql = "SELECT niveauUrgence, description, longitude, latitude, idUtilisateur, idSousCategorie, lieu, cloture, idIncident FROM Incident;"

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



def insertUtili(login,pwd,surnom) :


    sql = "INSERT INTO Utilisateur (login,mdp,surnom) VALUES (%s, %s, %s);"
    param = (login,pwd,surnom)

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

def cloturincident(idincident, raisoncloture):
    sql = "UPDATE Incident SET cloture=1, raisoncloture=%s, idUtilisateurcloture=%s where idIncident=%s;"
    param = (raisoncloture,Session()["id"],idincident)
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