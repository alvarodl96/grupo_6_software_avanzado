# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.actualizacion_pago import ActualizacionPago
from swagger_server.models.pagos import Pagos
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestPagosController(BaseTestCase):
    """ PagosController integration test stubs """

    def test_actualizar_pago(self):
        """
        Test case for actualizar_pago

        Actualiza el pago a profesor
        """
        dni = ActualizacionPago()
        response = self.client.open('/cobros/pagos',
                                    method='PUT',
                                    data=json.dumps(dni),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_borrar_pago(self):
        """
        Test case for borrar_pago

        Borra un pago
        """
        response = self.client.open('/cobros/delete-pagos/{id}'.format(id=56),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_crea_pago(self):
        """
        Test case for crea_pago

        Inserta un pago
        """
        pago = Pagos()
        response = self.client.open('/cobros/pagos',
                                    method='POST',
                                    data=json.dumps(pago),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_pago_profesor(self):
        """
        Test case for pago_profesor

        Consulta la nomina del profesor
        """
        response = self.client.open('/cobros/get-pagos/{dni}'.format(dni=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
