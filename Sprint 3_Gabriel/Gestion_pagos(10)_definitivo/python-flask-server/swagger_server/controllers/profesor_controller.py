import connexion
from swagger_server.models.actualizacion_pago import ActualizacionPago
from swagger_server.models.profesor import Profesor
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
#r = requests.post(apibase, json = {'dni_profesor', 'carga_trabajo'})
#profInfo=r.json()
def crea_profesor(profesor):
    """
    Crea un profesor
    Añade un profesor a la lista de profesores
    :param profesor: Se va a añadir un profesor
    :type profesor: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        profesor = Profesor.from_dict(connexion.request.get_json())
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO `profesor`(`DNI`, `Nombre`, `Apellidos`)"
                       +"VALUES (\'{}\', \'{}\', \'{}\')".format(profesor.dni, profesor.nombre, profesor.apellidos))
        cnx.commit()
    except mysql.connector.Error as e:
        cnx.close()
        cursor.close()
        abort(400, "El profesor no ha podido ser creado")
    cursor.close()
    cnx.close()
    return "El profesor ha sido creado correctamente"

def borrar_profesor(dni):
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
        cursor.execute("DELETE FROM `profesor` WHERE `profesor`.`DNI` = {}".format(dni))
        cnx.commit()
    except mysql.connector.Error as e:
        cnx.close()
        cursor.close()
        abort(400, "El profesor no ha podido ser borrado.")
    if cursor.rowcount == 0:
        cnx.close()
        cursor.close()
        abort(400, "El profesor no existe.")
    cursor.close()
    cnx.close()
    return "Profesor borrado correctamente."

def get_profesor(dni):
    """
    consulta un profesor
    consulta caracteristicas profesor
    :param dni: Dni del profesor
    :type dni: int

    :rtype: List[Profesor]
    """
    cnx = mysql.connector.connect(user=user, password=password, database=database)
    cursor = cnx.cursor()
    cursor.execute("SELECT `profesor`.`DNI`, `profesor`.`Nombre`, `profesor`.`Apellidos` \n"
                   +"FROM `profesor` \n"
                   +"WHERE `profesor`.`DNI` = \""+str(dni)+"\"")
    DB = {}
    tuplas = 0
    for (dni, Nombre, Apellidos) in cursor:
        DB[tuplas] = Profesor(dni, Nombre, Apellidos)
        tuplas += 1
    cursor.close()
    cnx.close()
    if tuplas == 0:
        return abort(404, "El profesor no existe")
    return [dni for _, dni in DB.items()]

def actualizar_pago_profesor(dni):
    """
    Actualiza el pago a profesor
    Actualiza el pago al profesor
    :param dni: Se va a actualizar el pago
    :type dni: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        dni = ActualizacionPago.from_dict(connexion.request.get_json())
    return 'do some magic!'
