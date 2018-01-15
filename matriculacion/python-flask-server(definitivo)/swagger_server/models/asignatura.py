# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Asignatura(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id: int=None, nombre: str=None, n_creditos: int=None):
        """
        Asignatura - a model defined in Swagger

        :param id: The id of this Asignatura.
        :type id: int
        :param nombre: The nombre of this Asignatura.
        :type nombre: str
        :param n_creditos: The n_creditos of this Asignatura.
        :type n_creditos: int
        """
        self.swagger_types = {
            'id': int,
            'nombre': str,
            'n_creditos': int
        }

        self.attribute_map = {
            'id': 'id',
            'nombre': 'nombre',
            'n_creditos': 'n_creditos'
        }

        self._id = id
        self._nombre = nombre
        self._n_creditos = n_creditos

    @classmethod
    def from_dict(cls, dikt) -> 'Asignatura':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The asignatura of this Asignatura.
        :rtype: Asignatura
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """
        Gets the id of this Asignatura.

        :return: The id of this Asignatura.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """
        Sets the id of this Asignatura.

        :param id: The id of this Asignatura.
        :type id: int
        """

        self._id = id

    @property
    def nombre(self) -> str:
        """
        Gets the nombre of this Asignatura.

        :return: The nombre of this Asignatura.
        :rtype: str
        """
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        """
        Sets the nombre of this Asignatura.

        :param nombre: The nombre of this Asignatura.
        :type nombre: str
        """

        self._nombre = nombre

    @property
    def n_creditos(self) -> int:
        """
        Gets the n_creditos of this Asignatura.

        :return: The n_creditos of this Asignatura.
        :rtype: int
        """
        return self._n_creditos

    @n_creditos.setter
    def n_creditos(self, n_creditos: int):
        """
        Sets the n_creditos of this Asignatura.

        :param n_creditos: The n_creditos of this Asignatura.
        :type n_creditos: int
        """

        self._n_creditos = n_creditos
