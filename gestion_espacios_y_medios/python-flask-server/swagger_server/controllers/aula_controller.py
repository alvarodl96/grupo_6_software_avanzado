import connexion
from swagger_server.models.aula import Aula
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def crea_aula(numero_aula=None):
    """
    Crea un aula
    Añade un aula a la lista de aulas
    :param numero_aula: El aula ha sido creada
    :type numero_aula: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        numero_aula = Aula.from_dict(connexion.request.get_json())
    return 'do some magic!'
