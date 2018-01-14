# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.actualizacion_pago import ActualizacionPago
from swagger_server.models.profesor import Profesor
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestProfesorController(BaseTestCase):
    """ ProfesorController integration test stubs """

    def test_actualizar_pago_profesor(self):
        """
        Test case for actualizar_pago_profesor

        Actualiza el pago a profesor
        """
        dni = ActualizacionPago()
        response = self.client.open('/cobros/profesor',
                                    method='PUT',
                                    data=json.dumps(dni),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_borrar_profesor(self):
        """
        Test case for borrar_profesor

        Borra un profesor
        """
        response = self.client.open('/cobros/delete-profesores/{dni}'.format(dni=56),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_crea_profesor(self):
        """
        Test case for crea_profesor

        Crea un profesor
        """
        profesor = Profesor()
        response = self.client.open('/cobros/profesor',
                                    method='POST',
                                    data=json.dumps(profesor),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_profesor(self):
        """
        Test case for get_profesor

        consulta un profesor
        """
        response = self.client.open('/cobros/get-profesores/{dni}'.format(dni=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
