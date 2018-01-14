# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.dni1 import Dni1
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestProfesorController(BaseTestCase):
    """ ProfesorController integration test stubs """

    def test_profesor_post(self):
        """
        Test case for profesor_post

        Crea un profesor
        """
        dni = Dni1()
        response = self.client.open('/cobros/profesor',
                                    method='POST',
                                    data=json.dumps(dni),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
