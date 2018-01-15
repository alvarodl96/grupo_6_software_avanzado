import connexion
from swagger_server.models.departamento import Departamento
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


def delete_departamento(Num_Departamento):
    """
    Borra un departamento
    Borra un departamento del sistema
    :param Num_Departamento: Codigo del departamento a borrar
    :type Num_Departamento: int

    :rtype: None
    """
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        cursor.execute("DELETE FROM `departamento` WHERE `departamento`.`Num_Departamento` = {}".format(Num_Departamento))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "El departamento no se ha podido borrar.")
    if cursor.rowcount == 0:
        cursor.close()
        cnx.close()
        abort(400, "El departamento no existe.")
    cursor.close()
    cnx.close()
    return "Departamento borrado correctamente."



def get_departamento(Codigo):
    """
    Obtiene un departamento
    Devuelve un departamento
    :param Codigo: Codigo del departamento
    :type Codigo: int

    :rtype: List[Departamento]
    """
    return 'do some magic!'


def post_departamento(departamento):
    """
    Crea departamento
    Añade un departamento al sistema
    :param departamento: El Departamento es creado
    :type departamento: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        departamento = Departamento.from_dict(connexion.request.get_json())
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO `departamento` (`Edificio`, `Nomb_Departamento`, `Num_Departamento`, `Titulacion`)"
                   +"VALUES (\'{}\', \'{}\', \'{}\', \'{}\')".format(departamento.edificio, departamento.nomb_departamento, departamento.num_departamento, departamento.titulacion))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "El departamento no ha podido ser creado.")
    cursor.close()
    cnx.close()
    return "Departamento creado correctamente."
