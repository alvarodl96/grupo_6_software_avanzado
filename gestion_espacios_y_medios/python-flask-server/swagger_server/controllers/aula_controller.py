import connexion
from swagger_server.models.aula import Aula
from swagger_server.models.reserva import Reserva
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

def borra_aula(numero):
    """
    Borra un aula
    Borra un aula
    :param numero: codigo del aula
    :type numero: int

    :rtype: None
    """
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        cursor.execute("DELETE FROM `aula` WHERE `aula`.`numero_aula` = {}".format(numero))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "El aula no ha podido ser borrada.")
    if cursor.rowcount == 0:
        cursor.close()
        cnx.close()
        abort(400, "El aula no existe.")
    cursor.close()
    cnx.close()
    return "Aula borrada correctamente."


def crea_aula(aula=None):
    """
    Crea un aula
    Añade un aula a la lista de aulas
    :param aula: El aula ha sido creada
    :type aula: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        aula = Aula.from_dict(connexion.request.get_json())
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO aula (codigo_asignatura, numero_aula,capacidad,precio,tipo, factura) "
                   +"VALUES (\'{}\', \'{}\',\'{}\', \'{}\',\'{}\',\'{}\')".format(aula.codigo_asignatura, aula.numero_aula, aula.capacidad, aula.precio, aula.tipo, aula.factura))      
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "El aula no ha podido ser creada.")
    cursor.close()
    cnx.close()
    return "Aula creada correctamente."


def devuelve_aula(numero):
    """
    Devuelve un aula
    Devuelve un aula
    :param numero: numero del aula
    :type numero: int

    :rtype: List[Aula]
    """
    cnx = mysql.connector.connect(user=user, password=password, database=database)
    cursor = cnx.cursor()
    cursor.execute("SELECT aula.codigo_asignatura, aula.numero_aula, aula.capacidad, aula.precio, aula.tipo, aula.factura FROM aula WHERE numero_aula = \""+str(numero)+"\"")
    DB = {}
    tuplas = 0
    for (codigo_asignatura, numero_aula, capacidad, precio, tipo, factura) in cursor:
        DB[tuplas] = Aula(codigo_asignatura, numero_aula, capacidad, precio, tipo, factura)
        tuplas += 1
    cursor.close()
    cnx.close()
    if tuplas == 0:
        return abort(404, "El aula no existe")
    return [Aula for _, Aula in DB.items()]


def reserva_aula(numero_aula):
    """
    Reserva aula y genera factura
    Reserva el aula y genera factura
    :param numero_aula: numero_aula
    :type numero_aula: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        numero_aula = Reserva.from_dict(connexion.request.get_json())
    cnx = mysql.connector.connect(user=user, password=password, database=database)    
    cursor = cnx.cursor()
    cursor.execute("SELECT `codigo_asignatura` AS `cod` , `precio` AS `prec` FROM `aula` WHERE `numero_aula` = "+str(numero_aula.numero_aula))

    for (cod, prec) in cursor:
        codigo = cod
        preci = prec
    if (codigo == 0):
        cursor.execute("UPDATE `aula` SET `codigo_asignatura` = "+str(numero_aula.horas*250)
                        +" WHERE `aula`.`numero_aula` = '"+str(numero_aula.numero_aula)+"'")
        cursor.execute("UPDATE `aula` SET `factura` = "+str(numero_aula.horas*preci)
                       +" WHERE `aula`.`numero_aula` = '"+str(numero_aula.numero_aula)+"'")
    else:
        return abort (404, "Aula utilizada para labores docentes")
    
    if cursor.rowcount == 0:
        cursor.close()
        cnx.close()
        abort(400, "La reserva de aula no se ha podido realizar")
    cnx.commit()
    cursor.close()
    cnx.close()
    return 'Reserva actualizada'
