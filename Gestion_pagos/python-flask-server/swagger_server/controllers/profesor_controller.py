import connexion
from swagger_server.models.dni1 import Dni1
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def profesor_post(dni=None):
    """
    Crea un profesor
    Añade un profesor a la lista de profesores
    :param dni: El profesor ha sido creado
    :type dni: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        dni = Dni1.from_dict(connexion.request.get_json())
    return 'do some magic!'
