# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.actualizacion_matricula import ActualizacionMatricula
from swagger_server.models.matricula import Matricula
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestMatriculaController(BaseTestCase):
    """ MatriculaController integration test stubs """

    def test_actualizar_matricula(self):
        """
        Test case for actualizar_matricula

        Actualiza la matricula
        """
        dni = ActualizacionMatricula()
        response = self.client.open('/cobros/matricula',
                                    method='PUT',
                                    data=json.dumps(dni),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_borra_matricula(self):
        """
        Test case for borra_matricula

        Borra una matricula
        """
        response = self.client.open('/cobros/delete-matricula/{dni}'.format(dni=56),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_crear_matricula(self):
        """
        Test case for crear_matricula

        Crea matricula
        """
        matricula = Matricula()
        response = self.client.open('/cobros/matricula',
                                    method='POST',
                                    data=json.dumps(matricula),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_matricula(self):
        """
        Test case for get_matricula

        Consulta la matricula del alumno
        """
        response = self.client.open('/cobros/get-matricula/{dni}'.format(dni=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
