# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.aula import Aula
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAulaController(BaseTestCase):
    """ AulaController integration test stubs """

    def test_crea_aula(self):
        """
        Test case for crea_aula

        Crea un aula
        """
        numero_aula = Aula()
        response = self.client.open('/espacios/Aula',
                                    method='POST',
                                    data=json.dumps(numero_aula),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
