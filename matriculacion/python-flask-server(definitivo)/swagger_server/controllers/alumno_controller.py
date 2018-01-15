import connexion
from swagger_server.models.alumno import Alumno
from swagger_server.models.inline_response200 import InlineResponse200
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import mysql.connector
from mysql.connector import errorcode
from flask import abort
import requests

user = "root"
password = ""
database = "matriculacion"

def alumno_get(dni=None):
    """
    Obtiene un alumno
    Devuelve un alumno
    :param dni: DNI del alumno
    :type dni: int

    :rtype: List[InlineResponse200]
    """
    cnx = mysql.connector.connect(user=user, password=password, database=database)
    cursor = cnx.cursor()
    cursor.execute("SELECT `DNI`, `Nombre`, `Apellidos`, `Titulacion`, `curso`, `creditos` FROM `alumno` WHERE `alumno`.`DNI` = {}".format(dni))
    DB = {}
    tuplas = 0
    for (DNI, Nombre, Apellidos, Titulacion, curso, creditos) in cursor:
        DB[tuplas] = Alumno(Apellidos, creditos, curso, dni, Nombre, creditos)
        tuplas +=1
    cursor.close()
    cnx.close
    if tuplas == 0:
        return abort(404, "No se encuentra el alumno")
    return [Alumno for _, Alumno in DB.items()]


def alumno_post(alumno=None):
    """
    Crea un alumno
    Annade un alumno a la base de datos
    :param alumno: La persona a crear
    :type alumno: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        alumno = Alumno.from_dict(connexion.request.get_json())
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO `alumno`(`dni`, `nombre`, `apellidos`, `titulacion`, `curso`, `creditos`) "
                      + "VALUES(\'{}\', \'{}\', \'{}\',\'{}\', \'{}\', \'{}\')".format(alumno.dni, alumno.nombre, alumno.apellidos, alumno.titulacion, alumno.curso, alumno.creditos))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "El alumno no ha podido ser creado.")
    cursor.close()
    cnx.close()
    """
    try:
        apibase= "http://172.22.95.193:8080/profesores/alumno"
        r = requests.post(apibase, json = {'apellidos':alumno.apellidos, 'dni':alumno.dni, 'nombre':alumno.nombre})
        #r = requests.post(apibase, json = {'apellidos':"asdasd", 'dni':20321, 'nombre':"asdliasjdoj"})
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("ERROR")
    return "Alumno creado correctamente."
    """
