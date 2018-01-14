import connexion
from swagger_server.models.actualizacion_pago import ActualizacionPago
from swagger_server.models.pagos import Pagos
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



def borrar_pago(id):
    """
    Borra un pago
    Borra un pago segun el id
    :param id: ID matricula
    :type id: int

    :rtype: None
    """
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        cursor.execute("DELETE FROM `pagos` WHERE `pagos`.`id` = {}".format(id))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "El pago no ha podido ser borrado.")
    if cursor.rowcount == 0:
        cursor.close()
        cnx.close()
        abort(400, "El pago no existe.")
    cursor.close()
    cnx.close()
    return "Pago borrado correctamente."


def crea_pago(pago):
    """
    Inserta un pago
    Inserta un pago
    :param pago: El pago se va a crear
    :type pago: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        pago = Pagos.from_dict(connexion.request.get_json())
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO `pagos` (`dni_profesor`, `id`, `impreso`, `recordatorio`, `carga_trabajo`, `Nomina`) "
                   +"VALUES (\'{}\', \'{}\', \'{}\',\'{}\', \'{}\', \'{}\')".format(pago.dni_profesor, pago.id, pago.impreso, pago.recordatorio, pago.carga_trabajo, pago.nomina))
        cnx.commit()
    except mysql.connector.Error as e:
        cnx.close()
        cursor.close()
        abort(400, "El pago no ha podido ser creado.")
    cursor.close()
    cnx.close()
    #apibase = "https://"+str(ipDepartamentos)+":8080/gestor_departamento/profesor"
    #try:
    #    r = requests.post('apibase', json = {'DNI_profesor':profesor.dni, 'Carga_Trabajo':0})
    #    r.raise_for_status()
    #except requests.exceptions.RequestException as e:
    #    print("RequestException - Error al conectar con el microservicio de espacios y medios\n")
    return "Pago creado correctamente."


def pago_profesor(dni):
    """
    Consulta la nomina del profesor
    hace una consulta para comprobar la nomina del profesor
    :param dni: DNI del profesor
    :type dni: int

    :rtype: List[Pagos]
    """
    cnx = mysql.connector.connect(user=user, password=password, database=database)
    cursor = cnx.cursor()
    cursor.execute("SELECT `pagos`.`dni_profesor`, `pagos`.`id`, `pagos`.`impreso`, `pagos`.`recordatorio`, `pagos`.`carga_trabajo`, `pagos`.`Nomina` \n"
                   +"FROM `pagos` \n"
                   +"WHERE `pagos`.`dni_profesor` = \""+str(dni)+"\"")
    DB = {}
    tuplas = 0
    for (dni_profesor, id, impreso, recordatorio, carga_trabajo, Nomina) in cursor:
        DB[tuplas] = Pagos(dni_profesor, id, impreso, recordatorio, carga_trabajo, Nomina)
        tuplas += 1
    cursor.close()
    cnx.close()
    if tuplas == 0:
        return abort(404, "El pago no existe")
    return [dni for _, dni in DB.items()]

def actualizar_pago(dni):
    """
    Actualiza el pago a profesor
    Actualiza el pago al profesor
    :param dni: Se va a actualizar el pago
    :type dni: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        dni = ActualizacionPago.from_dict(connexion.request.get_json())
    cnx = mysql.connector.connect(user=user, password=password, database=database)    
    cursor = cnx.cursor()
    cursor.execute("UPDATE `pagos` SET `carga_trabajo` = "+str(dni.nomina)
                   +" WHERE `pagos`.`dni_profesor` = '"+str(dni.dni_profesor)+"'")
    if cursor.rowcount == 0:
        cursor.close()
        cnx.close()
        abort(400, "El pago no ha podido ser actualizada")
    cnx.commit()
    cursor.close()
    cnx.close()
    return 'Pago actualizado'
