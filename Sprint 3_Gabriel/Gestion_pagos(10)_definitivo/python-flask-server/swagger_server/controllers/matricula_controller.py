import connexion
from swagger_server.models.actualizacion_matricula import ActualizacionMatricula
from swagger_server.models.matricula import Matricula
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

def borra_matricula(dni):
    """
    Borra una matricula
    Borra una matricula dado el dni del alumno
    :param dni: DNI del alumno
    :type dni: int

    :rtype: None
    """
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        cursor.execute("DELETE FROM `matricula` WHERE `matricula`.`dni_alumno` = {}".format(dni))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "La matricula no ha podido ser borrado.")
    if cursor.rowcount == 0:
        cursor.close()
        cnx.close()
        abort(400, "El alumno no existe.")
    cursor.close()
    cnx.close()
    return "Matricula borrada correctamente."

def calcular_precio(plazo):
    """
    Calcula el precio de la matricula
    """
    total=0
    if connexion.request.is_json:
        plazo = Matricula.from_dict(connexion.request.get_json())
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)
        cursor = cnx.cursor()
        if plazo==1:
            total = ("UPDATE `matricula` SET `precio` = "+str(plazo.precio)
                    + "WHERE `matricula`.`dni_alumno` = "+str(plazo.dni_alumno)+"'")
        elif plazo==2:
            total = ("UPDATE `matricula` SET `precio` = "+str(plazo.precio/2)
                    + "WHERE `matricula`.`dni_alumno` = "+str(plazo.dni_alumno)+"'")
        elif plazo==3:
            total = ("UPDATE `matricula` SET `precio` = "+str(plazo.precio/3)
                    + "WHERE `matricula`.`dni_alumno` = "+str(plazo.dni_alumno)+"'")
    except mysql.connector.Error as e:
        cnx.close()
        cursor.close()
        abort(400, "La matricula no se ha podido crear")
    cursor.close()
    cnx.close()
    return total
        

def crear_matricula(matricula):
    """
    Crea matricula
    Crea matricula del alumno
    :param matricula: La matricula se va a crear
    :type matricula: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        matricula = Matricula.from_dict(connexion.request.get_json())
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO `matricula` (`dni_alumno`, `id_pago`, `plazos`, `Reserva`, `precio`)"
                       +"VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\')".format(matricula.dni_alumno, matricula.id, matricula.plazos, matricula.reserva, matricula.precio))
        if (matricula.plazos==1):
            #cursor.execute("INSERT INTO `matricula` (`precio`)"
            #               +"VALUES (\'{}')".format(matricula.precio))
            cursor.execute("UPDATE `matricula` SET `precio` = `precio`"
                            +" WHERE `matricula`.`dni_alumno` = '"+str(matricula.dni_alumno)+"'")
        elif (matricula.plazos==2):
            #cursor.execute("INSERT INTO `matricula` (`precio`)"
            #               +"VALUES (\'{}')".format((matricula.precio)/2))
            cursor.execute("UPDATE `matricula` SET `precio` = `precio`/2"
                            +" WHERE `matricula`.`dni_alumno` = '"+str(matricula.dni_alumno)+"'")
        elif (matricula.plazos==3):
            #cursor.execute("INSERT INTO `matricula` (`precio`)"
            #               +"VALUES (\'{}')".format((matricula.precio)/3))
            cursor.execute("UPDATE `matricula` SET `precio` = `precio`/3"
                            +" WHERE `matricula`.`dni_alumno` = '"+str(matricula.dni_alumno)+"'")
        cnx.commit()
    except mysql.connector.Error as e:
        cnx.close()
        cursor.close()
        abort(400, "La matricula no se ha podido crear")
    cursor.close()
    cnx.close()
    return "Matricula creada correctamente"


def get_matricula(dni):
    """
    Consulta la matricula del alumno
    Consulta la matricula del alumno dado su dni
    :param dni: DNI del alumno
    :type dni: int

    :rtype: List[Matricula]
    """
    cnx = mysql.connector.connect(user=user, password=password, database=database)
    cursor = cnx.cursor()
    cursor.execute("SELECT `matricula`.`dni_alumno`, `matricula`.`id_pago`, `matricula`.`precio`, `matricula`.`plazos`, `matricula`.`Reserva`\n"
                   + "FROM `matricula` \n"
                   + "WHERE `matricula`.`dni_alumno` = \""+str(dni)+"\"")
    DB = {}
    tuplas = 0
    for (dni_alumno, id_pago, precio, plazos, Reserva) in cursor:
        DB[tuplas] = Matricula(dni_alumno, id_pago, precio, plazos, Reserva)
        tuplas += 1
    cursor.close()
    cnx.close()
    if tuplas == 0:
        return abort(404, "La matricula no existe")
    return [dni for _, dni in DB.items()]

def actualizar_matricula(dni):
    """
    Actualiza la matricula
    actualiza la matricula despues de hacer la matricula el alumno
    :param dni: El precio se va a actualizar
    :type dni: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        dni = ActualizacionMatricula.from_dict(connexion.request.get_json())
    cnx = mysql.connector.connect(user=user, password=password, database=database)    
    cursor = cnx.cursor()
    cursor.execute("UPDATE `matricula` SET `precio` = "+str(dni.precio)
                   +" WHERE `matricula`.`dni_alumno` = '"+str(dni.dni_alumno)+"'")
    if cursor.rowcount == 0:
        cursor.close()
        cnx.close()
        abort(400, "La matricula no ha podido ser actualizada")
    cnx.commit()
    cursor.close()
    cnx.close()
    return 'Matricula actualizada'
