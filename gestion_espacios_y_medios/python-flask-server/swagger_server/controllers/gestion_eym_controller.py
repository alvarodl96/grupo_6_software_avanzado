import connexion
from swagger_server.models.gestion_eym import GestionEYM
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def devuelve_boolean_aula(id):
    """
    Devuelve aula
    Devuelve si esta ocupada
    :param id: id de la gestion
    :type id: int

    :rtype: List[GestionEYM]
    """
    return 'do some magic!'


def devuelve_factura(id):
    """
    Devuelve factura
    Devuelve la factura
    :param id: id de la gestion
    :type id: int

    :rtype: List[GestionEYM]
    """
    return 'do some magic!'


def reserva_aula(id):
    """
    Reserva aula
    Reserva un aula
    :param id: id de la gestion
    :type id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        id = GestionEYM.from_dict(connexion.request.get_json())
    return 'do some magic!'
