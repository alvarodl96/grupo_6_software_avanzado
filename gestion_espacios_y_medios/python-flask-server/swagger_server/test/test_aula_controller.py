# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.aula import Aula
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAulaController(BaseTestCase):
    """ AulaController integration test stubs """

    def test_borra_aula(self):
        """
        Test case for borra_aula

        Borra un aula
        """
        response = self.client.open('/espacios/delete-aula/{numero}'.format(numero=56),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_crea_aula(self):
        """
        Test case for crea_aula

        Crea un aula
        """
        aula = Aula()
        response = self.client.open('/espacios/post-aula/',
                                    method='POST',
                                    data=json.dumps(aula),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_devuelve_aula(self):
        """
        Test case for devuelve_aula

        Devuelve un aula
        """
        response = self.client.open('/espacios/get-aula/{numero}'.format(numero=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_reserva_aula(self):
        """
        Test case for reserva_aula

        Reserva aula y genera factura
        """
        response = self.client.open('/espacios/Aula'.format(numero_aula=56),
                                    method='PUT',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
