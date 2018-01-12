# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.gestion_eym import GestionEYM
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestGestionEYMController(BaseTestCase):
    """ GestionEYMController integration test stubs """

    def test_devuelve_boolean_aula(self):
        """
        Test case for devuelve_boolean_aula

        Devuelve aula
        """
        response = self.client.open('/espacios/GestionEYM'.format(id=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_devuelve_factura(self):
        """
        Test case for devuelve_factura

        Devuelve factura
        """
        response = self.client.open('/espacios/GestionEYM/DevolverFactura'.format(id=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_reserva_aula(self):
        """
        Test case for reserva_aula

        Reserva aula
        """
        id = GestionEYM()
        response = self.client.open('/espacios/GestionEYM/ReservarAula',
                                    method='PUT',
                                    data=json.dumps(id),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
