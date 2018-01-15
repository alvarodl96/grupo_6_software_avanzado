import connexion
import requests 
from swagger_server.models.asignatura import Asignatura
from swagger_server.models.cambio import Cambio
from swagger_server.models.cambio_departa import CambioDeparta
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


def asigna_departamento(cambioDeparta):
    """
    Le pasa un departamento a la asignatura
    Actualiza un departamento a la asignatura
    :param cambioDeparta: Asignatura va a actualizarse
    :type cambioDeparta: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        cambioDeparta = CambioDeparta.from_dict(connexion.request.get_json())
    cnx = mysql.connector.connect(user=user, password=password, database=database)    
    cursor = cnx.cursor()
    cursor.execute("UPDATE `asignatura` SET `Num_Departamento` = "+str(cambioDeparta.num_departamento)
                   +" WHERE `asignatura`.`Codigo` = '"+str(cambioDeparta.codigo)+"'")
    if cursor.rowcount == 0:
        cursor.close()
        cnx.close()
        abort(400, "Departamento no ha podido ser asignado")
    cnx.commit()
    cursor.close()
    cnx.close()
    return "Departamento ha sido asignado a asignatura"


def asigna_profesor(cambio):
    """
    Le pasa un profesor a la asignatura
    Actualiza un profesor a la asignatura
    :param cambio: Asignatura va a actualizarse
    :type cambio: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        cambio = Cambio.from_dict(connexion.request.get_json())
    cnx = mysql.connector.connect(user=user, password=password, database=database)    
    cursor = cnx.cursor()
    cursor.execute("UPDATE `asignatura` SET `Profesor` = "+str(cambio.profesor)
                   +" WHERE `asignatura`.`Codigo` = '"+str(cambio.codigo)+"'")
    cursor.execute("UPDATE `profesor` SET `Carga_Trabajo`=`Carga_Trabajo`+10 WHERE `DNI_profesor`= "+str(cambio.profesor))
    cursor.execute("SELECT `Nombre_Asignatura` AS `nomb_asignatura`,`Num_Departamento` AS `nomb_departamento` FROM `asignatura` WHERE `Codigo`= "+str(cambio.codigo))
    
    for (nomb_asignatura, nomb_departamento) in cursor:
        nombre = nomb_asignatura
        departa = nomb_departamento
    if cursor.rowcount == 0:
        cursor.close()
        cnx.close()
        abort(400, "Profesor no ha podido ser asignado")
    cnx.commit()
    cursor.close()
    cnx.close()
        
    apibase= "http://172.22.95.193:8080/profesores/asignatura"
    try:
        r = requests.post(apibase, json = {'id':cambio.codigo, 'dniProfesor':cambio.profesor, 'nombre':nombre, 'departamento':departa})
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("RequestException - Error al conectar con el microservicio de espacios y medios\n")
    
    return "Profesor ha sido asignado a asignatura"


def delete_asignatura(Codigo):
    """
    Borra una asignatura
    Borra una asignatura de la base de datos
    :param Codigo: Codigo de la asignatura que se quiere borrar
    :type Codigo: int

    :rtype: None
    """
    return 'do some magic!'


def get_asignatura(Codigo):
    """
    Obtiene una asignatura
    Devuelve una asignatura
    :param Codigo: Codigo de la asignatura
    :type Codigo: int

    :rtype: List[Asignatura]
    """
    return 'do some magic!'


def post_asignatura(asignatura):
    """
    Crea una asignatura
    Añade una asignatura a la base de datos
    :param asignatura: La asignatura que se crea
    :type asignatura: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        asignatura = Asignatura.from_dict(connexion.request.get_json())
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO `asignatura` (`Nombre_Asignatura`, `Codigo`, `Profesor`, `Num_Departamento`)"
                   +"VALUES (\'{}\', \'{}\', \'{}\', \'{}\')".format(asignatura.nombre_asignatura, asignatura.codigo, asignatura.profesor, asignatura.num_departamento))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "La asignatura no ha podido ser creada.")
    cursor.close()
    cnx.close()
    return "Asignatura creada correctamente."
