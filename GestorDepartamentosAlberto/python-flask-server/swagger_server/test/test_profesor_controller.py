# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.profesor import Profesor
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestProfesorController(BaseTestCase):
    """ ProfesorController integration test stubs """

    def test_delete_profesor(self):
        """
        Test case for delete_profesor

        Borra un profesor
        """
        response = self.client.open('/gestor_departamento/Profesor/{DNI_profesor}'.format(DNI_profesor=56),
                                    method='DELETE',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_profesor_get(self):
        """
        Test case for profesor_get

        Obtiene profesor
        """
        query_string = [('DNI_profesor', 56)]
        response = self.client.open('/gestor_departamento/profesor',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_profesor_post(self):
        """
        Test case for profesor_post

        Crea un profesor
        """
        profesor = Profesor()
        response = self.client.open('/gestor_departamento/profesor',
                                    method='POST',
                                    data=json.dumps(profesor),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
