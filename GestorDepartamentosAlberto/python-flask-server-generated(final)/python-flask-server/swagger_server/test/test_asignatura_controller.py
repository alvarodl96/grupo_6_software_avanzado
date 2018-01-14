# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.asignatura import Asignatura
from swagger_server.models.cambio import Cambio
from swagger_server.models.cambio_departa import CambioDeparta
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAsignaturaController(BaseTestCase):
    """ AsignaturaController integration test stubs """

    def test_asigna_departamento(self):
        """
        Test case for asigna_departamento

        Le pasa un departamento a la asignatura
        """
        cambioDeparta = CambioDeparta()
        response = self.client.open('/gestor_departamento/AsignarDepartamento',
                                    method='PUT',
                                    data=json.dumps(cambioDeparta),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_asigna_profesor(self):
        """
        Test case for asigna_profesor

        Le pasa un profesor a la asignatura
        """
        cambio = Cambio()
        response = self.client.open('/gestor_departamento/AsignarProfesor',
                                    method='PUT',
                                    data=json.dumps(cambio),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_delete_asignatura(self):
        """
        Test case for delete_asignatura

        Borra una asignatura
        """
        response = self.client.open('/gestor_departamento/asignatura/{Codigo}'.format(Codigo=56),
                                    method='DELETE',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_asignatura(self):
        """
        Test case for get_asignatura

        Obtiene una asignatura
        """
        query_string = [('Codigo', 56)]
        response = self.client.open('/gestor_departamento/asignatura',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_post_asignatura(self):
        """
        Test case for post_asignatura

        Crea una asignatura
        """
        asignatura = Asignatura()
        response = self.client.open('/gestor_departamento/asignatura',
                                    method='POST',
                                    data=json.dumps(asignatura),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
