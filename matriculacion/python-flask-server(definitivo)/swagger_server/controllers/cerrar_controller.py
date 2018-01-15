import connexion
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

def cerrar_post():
    """
    Cierra el proceso de matriculacion
    cierra la matriculacion

    :rtype: None
    """

    #apibase= "http://"+str (ipgestionDepartamentos)+":8080/gestionDepartamentos/asignatura
    #apibase2= "http://"+str (ipgestionEspaciosYcobros)+":8080/gestionEspaciosYcobros/matricula
    
    """
    cnx = mysql.connector.connect(user=user, password=password, database=database)
    cursor = cnx.cursor()
    cursor.execute("SELECT COUNT(`DNI_alumno`) AS `num_alumnos`,`id_asignatura` FROM `matricula` GROUP BY id_asignatura")
    for (num_alumnos, id_asignatura) in cursor:
        try:
            r = requests.put(apibase, json = {'num_alumnos': num_alumnos, 'id_asignatura': id_asignatura})
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            print("ERROR")    
    cursor.close()
    cnx.close()
    
    cnx = mysql.connector.connect(user=user, password=password, database=database)
    cursor = cnx.cursor()
    cursor.execute("SELECT SUM(`coste`),`DNI_alumno` FROM `matricula` GROUP BY DNI_alumno")
    for (coste) in cursor:
        try:
            r = requests.put(apibase2, json = {'precio': coste})
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            print("ERROR")
    cursor.close()
    cnx.close()
    return "Periodo de matriculacion cerrado"
    """








            
    
