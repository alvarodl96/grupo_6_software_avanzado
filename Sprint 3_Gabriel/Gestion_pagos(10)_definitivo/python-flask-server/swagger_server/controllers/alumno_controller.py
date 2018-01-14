import connexion
from swagger_server.models.alumno import Alumno
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import mysql.connector
from mysql.connector import errorcode
from flask import abort
import requests
import json
import time

user = "root"
password = ""
database = "gestion_pagos"
apibase = "https://localhost:8080"
#r = requests.post(apibase, json = {'dni_alumno', 'coste/precio'})
#alumnInfo=r.json()
def crea_alumno(alumno):
    """
    Crea un alumno
    Añade un alumno a la lista de alumnos
    :param alumno: El alumno se va a crear
    :type alumno: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        alumno = Alumno.from_dict(connexion.request.get_json())
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO `alumno` (`DNI`, `Nombre`, `Apellidos`, `Asignatura`) "
                   +"VALUES (\'{}\', \'{}\', \'{}\',\'{}\')".format(alumno.dni, alumno.nombre, alumno.apellidos, alumno.asignatura))
        cnx.commit()
    except mysql.connector.Error as e:
        cnx.close()
        cursor.close()
        abort(400, "El alumno no ha podido ser creado.")
    cursor.close()
    cnx.close()
    return "Alumno creado correctamente."

def borrar_alumno(dni):
    """
    Borra alumno
    Borra un alumno
    :param dni: DNI del alumno
    :type dni: int

    :rtype: None
    """
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        cursor.execute("DELETE FROM `alumno` WHERE `alumno`.`DNI` = {}".format(dni))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "El alumno no ha podido ser borrado.")
    if cursor.rowcount == 0:
        cursor.close()
        cnx.close()
        abort(400, "El alumno no existe.")
    cursor.close()
    cnx.close()
    return "Alumno borrado correctamente."

def get_alumno(dni):
    """
    Consulta un alumno
    Consulta un alumno dado su dni
    :param dni: Dni del alumno
    :type dni: int

    :rtype: List[Alumno]
    """
    cnx = mysql.connector.connect(user=user, password=password, database=database)
    cursor = cnx.cursor()
    cursor.execute("SELECT `alumno`.`DNI`, `alumno`.`Nombre`, `alumno`.`Apellidos`, `alumno`.`Asignatura` \n"
                   +"FROM `alumno` \n"
                   +"WHERE `alumno`.`DNI` = \""+str(dni)+"\"")
    DB = {}
    tuplas = 0
    for (dni, nombre, apellidos, asignatura) in cursor:
        DB[tuplas] = Alumno(dni, nombre, apellidos, asignatura)
        tuplas += 1
    cursor.close()
    cnx.close()
    if tuplas == 0:
        return abort(404, "El alumno no existe")
    return [dni for _, dni in DB.items()]
