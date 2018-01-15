# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.asignatura import Asignatura
from swagger_server.models.inline_response2002 import InlineResponse2002
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAsignaturaController(BaseTestCase):
    """ AsignaturaController integration test stubs """

    def test_asignatura_id_delete(self):
        """
        Test case for asignatura_id_delete

        Borra una asignatura
        """
        response = self.client.open('/matriculacion/Asignatura/{id}'.format(id=56),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_asignatura_id_get(self):
        """
        Test case for asignatura_id_get

        Obtiene la asignatura
        """
        query_string = [('id', 56)]
        response = self.client.open('/matriculacion/Asignatura/id',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_asignatura_id_post(self):
        """
        Test case for asignatura_id_post

        Crea una asignatura
        """
        asignatura = Asignatura()
        response = self.client.open('/matriculacion/Asignatura/id',
                                    method='POST',
                                    data=json.dumps(asignatura),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
