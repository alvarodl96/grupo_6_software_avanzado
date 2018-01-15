# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.profesor import Profesor
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestProfesorController(BaseTestCase):
    """ ProfesorController integration test stubs """

    def test_borra_profesor(self):
        """
        Test case for borra_profesor

        Borra un profesor
        """
        response = self.client.open('/espacios/delete-profesor/{dni}'.format(dni=56),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_crea_profesor(self):
        """
        Test case for crea_profesor

        Crea un profesor
        """
        dni = Profesor()
        response = self.client.open('/espacios/Profesor',
                                    method='POST',
                                    data=json.dumps(dni),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_devuelve_profesor(self):
        """
        Test case for devuelve_profesor

        Devuelve un profesor
        """
        response = self.client.open('/espacios/get-profesor/{dni}'.format(dni=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
