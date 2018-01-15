# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.asignatura import Asignatura
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAsignaturaController(BaseTestCase):
    """ AsignaturaController integration test stubs """

    def test_borra_asignatura(self):
        """
        Test case for borra_asignatura

        Borra una asignatura
        """
        response = self.client.open('/espacios/delete-asignatura/{codigo}'.format(codigo=56),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_crea_asignatura(self):
        """
        Test case for crea_asignatura

        Crea asignatura
        """
        asignatura = Asignatura()
        response = self.client.open('/espacios/Asignatura',
                                    method='POST',
                                    data=json.dumps(asignatura),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_devuelve_asignatura(self):
        """
        Test case for devuelve_asignatura

        Devuelve una asignatura
        """
        response = self.client.open('/espacios/get-asignatura/{codigo}'.format(codigo=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
