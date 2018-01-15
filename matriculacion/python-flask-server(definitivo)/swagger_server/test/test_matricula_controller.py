# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.inline_response2001 import InlineResponse2001
from swagger_server.models.matricula import Matricula
from swagger_server.models.matricula1 import Matricula1
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestMatriculaController(BaseTestCase):
    """ MatriculaController integration test stubs """

    def test_matricula_get(self):
        """
        Test case for matricula_get

        Obtiene las asignaturas de un alumno
        """
        query_string = [('dni', 56)]
        response = self.client.open('/matriculacion/Matricula',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_matricula_post(self):
        """
        Test case for matricula_post

        Crea una matricula
        """
        matricula = Matricula1()
        response = self.client.open('/matriculacion/Matricula',
                                    method='POST',
                                    data=json.dumps(matricula),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_matricula_put(self):
        """
        Test case for matricula_put

        Crea una matricula
        """
        matricula = Matricula()
        response = self.client.open('/matriculacion/Matricula',
                                    method='PUT',
                                    data=json.dumps(matricula),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
