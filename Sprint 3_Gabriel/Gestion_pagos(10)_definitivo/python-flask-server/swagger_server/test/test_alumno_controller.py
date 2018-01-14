# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.alumno import Alumno
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAlumnoController(BaseTestCase):
    """ AlumnoController integration test stubs """

    def test_borrar_alumno(self):
        """
        Test case for borrar_alumno

        Borra alumno
        """
        response = self.client.open('/cobros/delete-alumnos/{dni}'.format(dni=56),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_crea_alumno(self):
        """
        Test case for crea_alumno

        Crea un alumno
        """
        alumno = Alumno()
        response = self.client.open('/cobros/alumno',
                                    method='POST',
                                    data=json.dumps(alumno),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_alumno(self):
        """
        Test case for get_alumno

        Consulta un alumno
        """
        response = self.client.open('/cobros/get-alumnos/{dni}'.format(dni=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
