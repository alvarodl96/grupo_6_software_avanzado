import connexion
from swagger_server.models.asignatura import Asignatura
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import mysql.connector
from mysql.connector import errorcode
from flask import abort

user = "root"
password = ""
database = "universidad"

def borra_asignatura(id):
    """
    Borra una asignatura
    Borra una asignatura y todas sus notas.
    :param id: ID de la asignatura
    :type id: int

    :rtype: None
    """
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        #cursor.execute("DELETE FROM `calificacion` WHERE `calificacion`.`id_asignatura` = {}".format(id))
        cursor.execute("DELETE FROM `asignatura` WHERE `asignatura`.`id` = {}".format(id))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "La asignatura no ha podido ser borrada.")
    if cursor.rowcount == 0:
        cursor.close()
        cnx.close()
        abort(400, "La asignatura no existe.")
    cursor.close()
    cnx.close()
    return "Asignatura borrada correctamente."


def crear_asignatura(asignatura):
    """
    Crea una asignatura
    Añade una asignatura a la lista de asignaturas.
    :param asignatura: La asignatura que se va a añadir.
    :type asignatura: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        asignatura = Asignatura.from_dict(connexion.request.get_json())
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO `asignatura` (`id`, `nombre`, `departamento`, `acta_cerrada`) "
                   +"VALUES (\'{}\', \'{}\', \'{}\', 0)".format(asignatura.id, asignatura.nombre, asignatura.departamento))
        cnx.commit()
        cursor.execute("INSERT INTO `imparte` (`id_asignatura`, `dni_profesor`) "
                   +"VALUES (\'{}\', \'{}\')".format(asignatura.id, asignatura.dni_profesor))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "La asignatura no ha podido ser creada.")
    cursor.close()
    cnx.close()
    return "Asignatura creada correctamente."
