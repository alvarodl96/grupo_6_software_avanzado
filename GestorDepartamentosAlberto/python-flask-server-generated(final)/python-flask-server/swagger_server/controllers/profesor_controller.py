import connexion
from swagger_server.models.profesor import Profesor
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import mysql.connector
from mysql.connector import errorcode
from flask import abort

user= "root"
password = ""
database = "gestor_departamento"


def delete_profesor(DNI_profesor):
    """
    Borra un profesor
    Borra un profesor del sistema
    :param DNI_profesor: DNI del profesor cuya matricula se quiera borrar
    :type DNI_profesor: int

    :rtype: None
    """
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        cursor.execute("DELETE FROM `profesor` WHERE `profesor`.`DNI_profesor` = {}".format(DNI_profesor))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "El profesor no se ha podido borrar.")
    if cursor.rowcount == 0:
        cursor.close()
        cnx.close()
        abort(400, "El profesor no existe.")
    cursor.close()
    cnx.close()
    return "Profesor borrado correctamente."



def profesor_get(DNI_profesor):
    """
    Obtiene profesor
    Devuelve un profesor
    :param DNI_profesor: DNI del profesor
    :type DNI_profesor: int

    :rtype: List[Profesor]
    """
    return 'do some magic!'


def profesor_post(profesor):
    """
    Crea un profesor
    Añade una profesor al sistema
    :param profesor: El profesor que se crea
    :type profesor: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        profesor = Profesor.from_dict(connexion.request.get_json())
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO `profesor` (`Carga_Trabajo`, `DNI_profesor`)"
                   +"VALUES (\'{}\', \'{}\')".format(profesor.carga_trabajo, profesor.dni_profesor))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "El profesor no ha podido ser creado.")
    cursor.close()
    cnx.close()
    """
    apibase= "http://"+str(ipGastosYCobros)+":8080/GastosYCobros/Pagos"
    try:
        r = requests.put(apibase, json = {'dniProfesor':profesor.dni_profesor, 'nomina':profesor.carga_trabajo })
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("RequestException - Error al conectar con el microservicio de espacios y medios\n")
    """
    return "Profesor creado correctamente."
