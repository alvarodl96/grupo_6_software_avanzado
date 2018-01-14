import connexion
from swagger_server.models.dni import Dni
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import mysql.connector
from mysql.connector import errorcode
from flask import abort

user= "root"
password = ""
database = "gestion_pagos"


def crea_alumno(dni):
    """
    Crea un alumno
    Añade un alumno a la lista de alumnos
    :param dni: El alumno ha sido creado
    :type dni: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        dni = Dni.from_dict(connexion.request.get_json())
    try:
	cnx = mysql.connector.connect(user=user, password=password, database=database)
	cursor = cnx.cursor()
	cursor.execute("INSERT INTO 'alumno' ('DNI', 'Nombre', 'Apellidos', 'Asignatura', 'Plazos')"
                       +"VALUES (\'{}\', \'{}\', \'{}\')".format(dni.DNI, dni.Nombre, dni.Apellidos, dni.Asignatura, dni.Plazos))
	cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "El alumno no se ha creado")
    cursor.close()
    cnx.close()
    return "Alumno creado correctamente"

def borrar_alumno(dni)
    """
    Borra un alumno
    :param dni: DNI del alumno
    :type dni: int

    :rtype: None
    """
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)
        cursor = cnx.cursor()
        cursor.execute("DELETE FROM 'DNI' WHERE 'dni'.'DNI' = {}".format(dni))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "El alumno no ha sido borrado")
    if cursor.rowcount == 0:
        cursor.close()
        cnx.close()
        abort(400, "El alumno no existe")
    cursor.close()
    cnx.close()
    return "Alumno borrado correctamente"
