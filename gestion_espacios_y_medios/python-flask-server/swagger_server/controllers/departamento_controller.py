import connexion
from swagger_server.models.departamento import Departamento
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def crea_departamento(codigo=None):
    """
    Crea Departamento
    Crea departamento
    :param codigo: El departamento ha sido creado
    :type codigo: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        codigo = Departamento.from_dict(connexion.request.get_json())
    return 'do some magic!'
