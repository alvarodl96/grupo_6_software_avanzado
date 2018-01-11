import connexion
from swagger_server.models.dni1 import Dni1
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import mysql.connector
from mysql.connector
import errorcode
from flask
import abort

user = "root"
password = ""
database = "gestion_pagos"

def crea_profesor(dni):
    """
    Crea un profesor
    Añade un profesor a la lista de profesores
    :param dni: El profesor ha sido creado
    :type dni: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        dni = Dni1.from_dict(connexion.request.get_json())
    try:
        cnx = mysql.connector.connect(user = user, password=password, database=database)
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO 'profesor' ('DNI', 'Nombre', 'Apellidos')"
                       +"VALUES (\'{}\', \'{}\', \'{}\')".format(dni.DNI, dni.Nombre, dni.Apellidos))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "El profesor no se ha podido crear")
    cursor.close()
    cnx.close()
    return "Profesor creado correctamente"

def borrar_profesor(dni)
    """
    Borra un profesor de la lista de profesores
    :param dni: DNI del profesor
    :type dni: int

    :rtype:None
    """
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        cursor.execute("DELETE FROM 'profesor' WHERE 'profesor'.'DNI' = {}".format(dni))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "El profesor no se ha podido borrar.")
    if cursor.rowcount == 0:
        cursor.close()
        cnx.close()
        abort(400, "El profesor no existe.")
    cursor.close()
    cnx.close()
    return "Profesor borrado correctamente."
