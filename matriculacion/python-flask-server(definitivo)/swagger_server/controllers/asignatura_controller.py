import connexion
from swagger_server.models.asignatura import Asignatura
from swagger_server.models.inline_response2002 import InlineResponse2002
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import mysql.connector
from mysql.connector import errorcode
from flask import abort

user = "root"
password = ""
database = "matriculacion"

def asignatura_id_delete(id):
    """
    Borra una asignatura
    
    :param id: id de la asignatura
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def asignatura_id_get(id=None):
    """
    Obtiene la asignatura
    Devuelve la asignatura en funcion de id
    :param id: id de la asignatura
    :type id: int

    :rtype: List[InlineResponse2002]
    """
    cnx = mysql.connector.connect(user=user, password=password, database=database)
    cursor = cnx.cursor()
    cursor.execute("SELECT `id`, `nombre`, `n_creditos` FROM `asignatura` WHERE `asignatura`.`id` = {}".format(id))
    DB = {}
    tuplas = 0
    for (id, nombre, n_creditos) in cursor:
        DB[tuplas] = Asignatura(id, nombre, n_creditos)
        tuplas +=1
    cursor.close()
    cnx.close
    if tuplas == 0:
        return abort(404, "No se encuentra el alumno")
    return [Asignatura for _, Asignatura in DB.items()]


def asignatura_id_post(asignatura=None):
    """
    Crea una asignatura
    Annade una asignatura en la base de datos
    :param asignatura: La asignatura a crear
    :type asignatura: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        asignatura = Asignatura.from_dict(connexion.request.get_json())
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO `asignatura`(`id`, `nombre`, `n_creditos`) "
                      + "VALUES(\'{}\', \'{}\', \'{}\')".format(asignatura.id, asignatura.nombre, asignatura.n_creditos))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "La asignatura no ha podido ser creada.")
    cursor.close()
    cnx.close()
    """
    try:
        apibase= "http://"+str (ipgestionDepartamentos)+":8080/gestiondepartamentos/asignatura
            r = requests.post(apibase, json = {'Codigo':asignatura.id, 'Nombre_Asignatura':asignatura.nombre}
            r.raise_for_status()
    except requests.exceptions.RequestException as e:
            print("ERROR")"""
    return "Asignatura creada correctamente."
