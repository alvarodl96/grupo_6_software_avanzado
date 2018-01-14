# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.dni2 import Dni2
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestMatriculaController(BaseTestCase):
    """ MatriculaController integration test stubs """

    def test_matricula_post(self):
        """
        Test case for matricula_post

        Crea matricula
        """
        dni = Dni2()
        response = self.client.open('/cobros/matricula',
                                    method='POST',
                                    data=json.dumps(dni),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
