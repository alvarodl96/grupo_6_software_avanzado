# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.departamento import Departamento
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDepartamentoController(BaseTestCase):
    """ DepartamentoController integration test stubs """

    def test_crea_departamento(self):
        """
        Test case for crea_departamento

        Crea Departamento
        """
        codigo = Departamento()
        response = self.client.open('/espacios/Departamento',
                                    method='POST',
                                    data=json.dumps(codigo),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
