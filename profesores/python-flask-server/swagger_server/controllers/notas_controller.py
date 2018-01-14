import connexion
from swagger_server.models.calificacion import Calificacion
from swagger_server.models.nota import Nota
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import mysql.connector
from mysql.connector import errorcode
from flask import abort
import requests

user = "root"
password = ""
database = "universidad"
file = open("ips.txt", "r")
ipMatriculacion = file.readline().split(":")[1]

def actualiza_nota(calificacion):
    """
    Actualiza una nota
    Actualiza la nota de un alumno en una asignatura.
    :param calificacion: La calificación que se va a actualizar.
    :type calificacion: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        calificacion = Nota.from_dict(connexion.request.get_json())
    cnx = mysql.connector.connect(user=user, password=password, database=database)    
    cursor = cnx.cursor()
    cursor.execute("UPDATE `calificacion` SET `nota` = "+str(calificacion.nota)
                   +" WHERE `calificacion`.`id_asignatura` = '"+str(calificacion.id_asignatura)
                   +"' AND `calificacion`.`dni_alumno` = '"+str(calificacion.dni_alumno)+"'")
    if cursor.rowcount == 0:
        cursor.close()
        cnx.close()
        abort(400, "La nota no ha podido ser actualizada")
    cnx.commit()
    cursor.close()
    cnx.close()
    return 'Nota actualizada'


def cerrar_acta(idAsignatura):
    """
    Cierra el acta de una asignatura
    Indican que todas los alumnos de una asignatura han sido calificados.
    :param idAsignatura: ID de la asignatura
    :type idAsignatura: int

    :rtype: None
    """
    cnx = mysql.connector.connect(user=user, password=password, database=database)
    cursor = cnx.cursor()
    cursor.execute("SELECT `acta_cerrada` FROM `asignatura` WHERE `id` = '"+str(idAsignatura)+"'")
    tuplas = 0
    for (acta_cerrada) in cursor:
        tuplas += 1
    if tuplas == 0:
        cursor.close()
        cnx.close()
        abort(400, "El acta no ha podido ser cerrada")
    cursor.execute("UPDATE `asignatura` SET `acta_cerrada` = 1 WHERE `id` = "+str(idAsignatura))
    cnx.commit()

    cursor = cnx.cursor()
    cursor.execute("SELECT `dni_alumno`, `nota` FROM `calificacion` WHERE `id_asignatura` = '"+str(idAsignatura)+"'")
    ############################Mandar nota a Matriculacion######################################
    apibase= "http://"+str(ipMatriculacion)+":8080/matriculacion"
    for (dni_alumno, nota) in cursor:
        try:
            aprobado="no"
            if nota>=5:
                aprobado="si"
            r = requests.put('apibase', json = {'DNI_alumno':dni_alumno, 'id_asignatura':idAsignatura, 'aprobada':aprobado})
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            print("RequestException - Error al conectar con el microservicio de matriculacion\n")
    cursor.close()
    cnx.close()
    return 'Acta cerrada correctamente'


def notas_dni_alumno_get(dni):
    """
    Devuelve las notas
    Devuelve las notas del alumno
    :param dni: DNI del alumno
    :type dni: int

    :rtype: List[Calificacion]
    """
    cnx = mysql.connector.connect(user=user, password=password, database=database)
    cursor = cnx.cursor()
    cursor.execute("SELECT `asignatura`.`id`, `asignatura`.`nombre` AS `nomb_asig`, `alumno`.`dni`, `alumno`.`nombre`, `alumno`.`apellidos`, `calificacion`.`nota`\n"
    + "FROM `alumno` \n"
    + "	INNER JOIN `calificacion` ON `alumno`.`dni` = `calificacion`.`dni_alumno`\n"
    + " INNER JOIN `asignatura` ON `calificacion`.`id_asignatura` = `asignatura`.`id`\n"
    + "WHERE `alumno`.`dni` = \""+str(dni)+"\"")
    DB = {}
    tuplas = 0
    for (id, nomb_asig, dni, nombre, apellidos, nota) in cursor:
        DB[tuplas] = Calificacion(dni, id, nota, nombre, apellidos, nomb_asig)
        tuplas += 1
    cursor.close()
    cnx.close()
    if tuplas == 0:
        return abort(404, "El alumno no existe o no está matriculado en ninguna asignatura")
    return [nota for _, nota in DB.items()]


def notas_dni_profesor_get(dni):
    """
    Devuelve las notas
    Devuelve las notas de los alumnos del profesor
    :param dni: DNI del profesor
    :type dni: int

    :rtype: List[Calificacion]
    """
    cnx = mysql.connector.connect(user=user, password=password, database=database)
    cursor = cnx.cursor()
    cursor.execute("SELECT `asignatura`.`id`, `asignatura`.`nombre` AS `nomb_asig`, `alumno`.`dni`, `alumno`.`nombre`, `alumno`.`apellidos`, `calificacion`.`nota`\n"
    + "FROM `alumno` \n"
    + "	INNER JOIN `calificacion` ON `alumno`.`dni` = `calificacion`.`dni_alumno`\n"
    + " INNER JOIN `asignatura` ON `calificacion`.`id_asignatura` = `asignatura`.`id`\n"
    + " INNER JOIN `imparte` ON `asignatura`.`id` = `imparte`.`id_asignatura`\n"
    + " INNER JOIN `profesor` ON `imparte`.`dni_profesor` = `profesor`.`dni`\n"
    + "WHERE `profesor`.`dni` = \""+str(dni)+"\"")
    DB = {}
    tuplas = 0
    for (id, nomb_asig, dni, nombre, apellidos, nota) in cursor:
        DB[tuplas] = Calificacion(dni, id, nota, nombre, apellidos, nomb_asig)
        tuplas += 1
    cursor.close()
    cnx.close()
    if tuplas == 0:
        return abort(404, "El profesor no existe o no tiene alumnos")
    return [nota for _, nota in DB.items()]


def notas_id_asignatura_get(id):
    """
    Devuelve las notas
    Devuelve las notas de la asignatura
    :param id: ID de la asignatura
    :type id: int

    :rtype: List[Calificacion]
    """
    cnx = mysql.connector.connect(user=user, password=password, database=database)
    cursor = cnx.cursor()
    cursor.execute("SELECT `asignatura`.`id`, `asignatura`.`nombre` AS `nomb_asig`, `alumno`.`dni`, `alumno`.`nombre`, `alumno`.`apellidos`, `calificacion`.`nota`\n"
    + "FROM `alumno` \n"
    + "	INNER JOIN `calificacion` ON `alumno`.`dni` = `calificacion`.`dni_alumno`\n"
    + " INNER JOIN `asignatura` ON `calificacion`.`id_asignatura` = `asignatura`.`id`\n"
    + "WHERE `asignatura`.`id` = \""+str(id)+"\"")
    DB = {}
    tuplas = 0
    for (id, nomb_asig, dni, nombre, apellidos, nota) in cursor:
        DB[tuplas] = Calificacion(dni, id, nota, nombre, apellidos, nomb_asig)
        tuplas += 1
    cursor.close()
    cnx.close()
    if tuplas == 0:
        return abort(404, "La asignatura no existe o no tiene alumnos")
    return [nota for _, nota in DB.items()]


def notas_user_profesor_get(nombreUsuario):
    """
    Devuelve las notas
    Devuelve las notas de los alumnos del profesor
    :param nombreUsuario: Nombre de usuario del profesor
    :type nombreUsuario: str

    :rtype: List[Calificacion]
    """
    cnx = mysql.connector.connect(user=user, password=password, database=database)
    cursor = cnx.cursor()
    cursor.execute("SELECT `asignatura`.`id`, `asignatura`.`nombre` AS `nomb_asig`, `alumno`.`dni`, `alumno`.`nombre`, `alumno`.`apellidos`, `calificacion`.`nota`\n"
    + "FROM `alumno` \n"
    + "	INNER JOIN `calificacion` ON `alumno`.`dni` = `calificacion`.`dni_alumno`\n"
    + " INNER JOIN `asignatura` ON `calificacion`.`id_asignatura` = `asignatura`.`id`\n"
    + " INNER JOIN `imparte` ON `asignatura`.`id` = `imparte`.`id_asignatura`\n"
    + " INNER JOIN `profesor` ON `imparte`.`dni_profesor` = `profesor`.`dni`\n"
    + "WHERE `profesor`.`nombre_usuario` = \""+nombreUsuario+"\"")
    DB = {}
    tuplas = 0
    for (id, nomb_asig, dni, nombre, apellidos, nota) in cursor:
        DB[tuplas] = Calificacion(dni, id, nota, nombre, apellidos, nomb_asig)
        tuplas += 1
    cursor.close()
    cnx.close()
    if tuplas == 0:
        return abort(404, "El profesor no existe o no tiene alumnos")
    return [nota for _, nota in DB.items()]
