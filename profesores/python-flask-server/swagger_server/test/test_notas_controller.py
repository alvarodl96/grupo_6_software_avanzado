# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.calificacion import Calificacion
from swagger_server.models.nota import Nota
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestNotasController(BaseTestCase):
    """ NotasController integration test stubs """

    def test_actualiza_nota(self):
        """
        Test case for actualiza_nota

        Actualiza una nota
        """
        calificacion = Nota()
        response = self.client.open('/profesores/nota',
                                    method='PUT',
                                    data=json.dumps(calificacion),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_cerrar_acta(self):
        """
        Test case for cerrar_acta

        Cierra el acta de una asignatura
        """
        response = self.client.open('/profesores/cerrar-acta/{idAsignatura}'.format(idAsignatura=56),
                                    method='PUT')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_notas_dni_alumno_get(self):
        """
        Test case for notas_dni_alumno_get

        Devuelve las notas
        """
        response = self.client.open('/profesores/notas/by-alumno/{dni}'.format(dni=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_notas_dni_profesor_get(self):
        """
        Test case for notas_dni_profesor_get

        Devuelve las notas
        """
        response = self.client.open('/profesores/notas/by-profesor/{dni}'.format(dni=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_notas_id_asignatura_get(self):
        """
        Test case for notas_id_asignatura_get

        Devuelve las notas
        """
        response = self.client.open('/profesores/notas/by-asignatura/{id}'.format(id=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_notas_user_profesor_get(self):
        """
        Test case for notas_user_profesor_get

        Devuelve las notas
        """
        response = self.client.open('/profesores/notas/by-user-profesor/{nombreUsuario}'.format(nombreUsuario='nombreUsuario_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
