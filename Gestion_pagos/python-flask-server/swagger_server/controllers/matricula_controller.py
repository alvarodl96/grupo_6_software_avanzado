import connexion
from swagger_server.models.dni2 import Dni2
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def matricula_post(dni=None):
    """
    Crea matricula
    Crea matricula
    :param dni: La matricula ha sido creada
    :type dni: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        dni = Dni2.from_dict(connexion.request.get_json())
    return 'do some magic!'
