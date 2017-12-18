import connexion
from swagger_server.models.dni import Dni
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def alumno_post(dni=None):
    """
    Crea un alumno
    Añade un alumno a la lista de alumnos
    :param dni: El alumno ha sido creado
    :type dni: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        dni = Dni.from_dict(connexion.request.get_json())
    return 'do some magic!'
