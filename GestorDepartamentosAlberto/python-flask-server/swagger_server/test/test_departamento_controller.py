# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.departamento import Departamento
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDepartamentoController(BaseTestCase):
    """ DepartamentoController integration test stubs """

    def test_delete_departamento(self):
        """
        Test case for delete_departamento

        Borra un departamento
        """
        response = self.client.open('/gestor_departamento/departamento/{Num_Departamento}'.format(Num_Departamento=789),
                                    method='DELETE',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_departamento(self):
        """
        Test case for get_departamento

        Obtiene un departamento
        """
        query_string = [('Codigo', 56)]
        response = self.client.open('/gestor_departamento/departamento',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_post_departamento(self):
        """
        Test case for post_departamento

        Crea departamento
        """
        departamento = Departamento()
        response = self.client.open('/gestor_departamento/departamento',
                                    method='POST',
                                    data=json.dumps(departamento),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
