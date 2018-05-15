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

# insertion dans la table commentaires


# def insertCommentData(email="", message="", name="") :
#     sql = "INSERT INTO commentaire (nom, comment, email) VALUES (%s, %s, %s);"
#     param = (email, message, name)
#
#     try :
#         cnx=connexion()
#         cursor = cnx.cursor(prepared=True)
#         results = cursor.execute(sql, param)
#         msg = results
#         cnx.commit()
#     except mysql.connector.Error as err :
#         msg = "Failed select table test: {}".format(err)
#         exit(1)
#     finally :
#         close_bd(cursor, cnx)
#     return msg


# Affichage de la table commentaires


# def affichCommentData():
#     sql = "SELECT id, nom, comment, email FROM commentaire;"
#
#     try:
#         cnx = connexion()
#         cursor = cnx.cursor(prepared=True)
#         results = cursor.execute(sql)
#         liste = list(cursor)
#     except mysql.connector.Error as err:
#         liste = "Failed select table test: {}".format(err)
#         exit(1)
#     finally:
#         close_bd(cursor, cnx)
#     return liste


# test de l'authentification de l'utilisateur.
# les paramètres sont ceux du formulaire dans l'ordre


def verif_connect(login='', pwd=''):
    cnx = connexion()
    cursor = cnx.cursor()
    query = "SELECT idUtilisateur, login, mdp, surnom FROM Utilisateur WHERE login=%s AND mdp=%s LIMIT 1"
    param = (login, pwd)
    cursor.execute(query, param)
    liste = list(cursor)
    for (idUtilisateur, login, mdp, surnom) in liste:
         Session()["nom"] = login
         Session()["surnom"] = surnom
         Session()["mdp"] = mdp
         Session()["id"] = idUtilisateur
    close_bd(cursor, cnx)
    return liste
