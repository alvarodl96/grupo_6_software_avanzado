import connexion
from swagger_server.models.profesor import Profesor
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import mysql.connector
from mysql.connector import errorcode
from flask import abort

user = "root"
password = ""
database = "gestioneym"

def borra_profesor(dni):
    """
    Borra un profesor
    Borra un profesor
    :param dni: DNI del profesor
    :type dni: int

    :rtype: None
    """
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        cursor.execute("DELETE FROM `profesor` WHERE `profesor`.`dni` = {}".format(dni))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "El profesor no ha podido ser borrado.")
    if cursor.rowcount == 0:
        cursor.close()
        cnx.close()
        abort(400, "El profesor no existe.")
    cursor.close()
    cnx.close()
    return "Profesor borrado correctamente."


def crea_profesor(dni):
    """
    Crea un profesor
    Añade un profesor a la lista de profesores
    :param dni: El profesor que se va a añadir
    :type dni: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        dni = Profesor.from_dict(connexion.request.get_json())
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO `profesor` (`dni`, `nombre`, `apellidos`, `nombre_usuario`) "
                   +"VALUES (\'{}\', \'{}\', \'{}\', \'{}\')".format(profesor.dni, profesor.nombre, profesor.apellidos, profesor.nombre_usuario))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "El profesor no ha podido ser creado.")
    cursor.close()
    cnx.close()
    return "Profesor creado correctamente."


def devuelve_profesor(dni):
    """
    Devuelve un profesor
    Devuelve un profesor
    :param dni: dni del profesor
    :type dni: int

    :rtype: List[Profesor]
    """
    cnx = mysql.connector.connect(user=user, password=password, database=database)
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM profesor WHERE dni = \""+str(dni)+"\"")
    DB = {}
    tuplas = 0
    for (dni, nombre, nombre_usuario, apellidos) in cursor:
        DB[tuplas] = Profesor(dni, nombre_usuario, nombre, apellidos)
        tuplas += 1
    cursor.close()
    cnx.close()
    if tuplas == 0:
        return abort(404, "El profesor no existe")
    return [Profesor for _, Profesor in DB.items()]
