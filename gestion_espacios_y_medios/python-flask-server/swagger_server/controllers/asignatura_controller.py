import connexion
from swagger_server.models.asignatura import Asignatura
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

def borra_asignatura(codigo):
    """
    Borra una asignatura
    Borra una asignatura
    :param codigo: codigo de la asignatura
    :type codigo: int

    :rtype: None
    """
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        cursor.execute("DELETE FROM `asignatura` WHERE `asignatura`.`codigo_asignatura` = {}".format(codigo))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "La asignatura no ha podido ser borrada.")
    if cursor.rowcount == 0:
        cursor.close()
        cnx.close()
        abort(400, "La asignatura no existe.")
    cursor.close()
    cnx.close()
    return "Asignatura borrada correctamente."


def crea_asignatura(asignatura=None):
    """
    Crea asignatura
    Crea asignatura
    :param asignatura: La asignatura se va a añadir
    :type asignatura: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        asignatura = Asignatura.from_dict(connexion.request.get_json())
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO asignatura (codigo_asignatura,numero_alumnos) "
                   +"VALUES (\'{}\', \'{}\')".format(asignatura.codigo_asignatura, asignatura.numero_alumnos))
        cnx.commit()   
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "La asignatura no ha podido ser creada.")
    cursor.close()
    cnx.close()
    #apibase = "https://"+str(codigo_asignatura)+":8080/alumno_matriculacion/asignatura"
    #try:
    #    r = requests.post('apibase', json = {'codigo_asignatura':asignatura.codigo_asignatura})
    #    r.raise_for_status()
    #except requests.exceptions.RequestException as e:
    #    print("RequestException - Error al conectar con el microservicio de matriculacion de alumnos\n")  
    return "Asignatura creada correctamente."



def devuelve_asignatura(codigo):
    """
    Devuelve una asignatura
    Devuelve una asignatura
    :param codigo: codigo de la asignatura
    :type codigo: int

    :rtype: List[Asignatura]
    """
    cnx = mysql.connector.connect(user=user, password=password, database=database)
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM asignatura WHERE codigo_asignatura = \""+str(codigo)+"\"")
    DB = {}
    tuplas = 0
    for (codigo_asignatura,numero_alumnos) in cursor:
        DB[tuplas] = Asignatura(codigo_asignatura,numero_alumnos)
        tuplas += 1
    cursor.close()
    cnx.close()
    if tuplas == 0:
        return abort(404, "La asignatura no existe")
    return [Asignatura for _, Asignatura in DB.items()]
