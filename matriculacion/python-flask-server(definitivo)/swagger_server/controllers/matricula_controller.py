import connexion
from swagger_server.models.inline_response2001 import InlineResponse2001
from swagger_server.models.matricula import Matricula
from swagger_server.models.matricula1 import Matricula1
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

def matricula_get(dni=None):
    """
    Obtiene las asignaturas de un alumno
    Devuelve la matricula de un alumno
    :param dni: DNI del alumno
    :type dni: int

    :rtype: List[InlineResponse2001]
    """
    cnx = mysql.connector.connect(user=user, password=password, database=database)
    cursor = cnx.cursor()
    cursor.execute("SELECT `aprobada`, `id_asignatura`, `DNI_alumno`, `coste` FROM `matricula` WHERE `matricula`.`DNI_alumno` = {}".format(dni))
    DB = {}
    tuplas = 0
    for (aprobada, id_asignatura, dni, coste) in cursor:
        DB[tuplas] = Matricula1(aprobada, coste, dni, id_asignatura)
        tuplas +=1
    cursor.close()
    cnx.close
    if tuplas == 0:
        return abort(404, "No se encuentra el alumno")
    return [Matricula1 for _, Matricula1 in DB.items()]


def matricula_post(matricula=None):
    """
    Crea una matricula
    Annade una matricula en la base de datos
    :param matricula: La matricula a crear
    :type matricula: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        matricula = Matricula1.from_dict(connexion.request.get_json())
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO `matricula`(`DNI_alumno`, `aprobada`, `coste`, `id_asignatura`) "
                      + "VALUES(\'{}\', \'{}\', \'{}\',\'{}\')".format(matricula.dni_alumno, matricula.aprobada, matricula.coste, matricula.id_asignatura))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "La matricula no ha podido ser creada.")
    cursor.close()
    cnx.close()
    
    return "Matricula creada correctamente."


def matricula_put(matricula=None):
    """
    Crea una matricula
    Annade una matricula en la base de datos
    :param matricula: La matricula a crear
    :type matricula: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        matricula = Matricula.from_dict(connexion.request.get_json())
    cnx = mysql.connector.connect(user=user, password=password, database=database)    
    cursor = cnx.cursor()
    cursor.execute("UPDATE `matricula` SET `aprobada` = "+str(matricula.aprobada)
                   +" WHERE `matricula`.`id_asignatura` = '"+str(matricula.id_asignatura)
                   +"' AND `matricula`.`DNI_alumno` = '"+str(matricula.dni_alumno)+"'")
    if cursor.rowcount == 0:
        cursor.close()
        cnx.close()
        abort(400, "La nota no ha podido ser actualizada")
    cnx.commit()
    cursor.close()
    cnx.close()
    return 'Nota actualizada'
    
