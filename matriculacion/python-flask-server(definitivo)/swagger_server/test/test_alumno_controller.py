# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.alumno import Alumno
from swagger_server.models.inline_response200 import InlineResponse200
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAlumnoController(BaseTestCase):
    """ AlumnoController integration test stubs """

    def test_alumno_get(self):
        """
        Test case for alumno_get

        Obtiene un alumno
        """
        query_string = [('dni', 56)]
        response = self.client.open('/matriculacion/Alumno',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_alumno_post(self):
        """
        Test case for alumno_post

        Crea un alumno
        """
        alumno = Alumno()
        response = self.client.open('/matriculacion/Alumno',
                                    method='POST',
                                    data=json.dumps(alumno),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
