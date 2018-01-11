import connexion
from swagger_server.models.dni2 import Dni2
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import mysql.connector
from mysql.connector
import errorcode
from flask
import abort

user = "root"
password = ""
database = "gestion_pagos"


def crear_matricula(dni):
    """
    Crea matricula
    Crea matricula
    :param dni: La matricula ha sido creada
    :type dni: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        dni = Dni2.from_dict(connexion.request.get_json())
    try:
        cnx = mysql.connector.connect(user=user, password=password, database=database)    
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO 'matricula' ('id_pago', 'dni_alumno')"
                       +"VALUES (\'{}\', \'{}\')".format(dni.id_pago, dni.dni_alumno))
        cnx.commit()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        abort(400, "La matricula no se ha podido crear")
    cursor.close()
    cnx.close()
    return "Matricula creada correctamente."
