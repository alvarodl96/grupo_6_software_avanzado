import connexion
from swagger_server.models.inline_response200 import InlineResponse200
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import mysql.connector
from mysql.connector
import errorcode
from flask
import abort

def pagos_get(dni):
    """
    Consulta la nomina del profesor
    hace una consulta para comprobar la nomina del profesor
    :param dni: DNI del profesor
    :type dni: int

    :rtype: List[InlineResponse200]
    """
    return 'do some magic!'
