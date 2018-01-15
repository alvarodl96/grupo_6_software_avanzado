# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestCerrarController(BaseTestCase):
    """ CerrarController integration test stubs """

    def test_cerrar_post(self):
        """
        Test case for cerrar_post

        Cierra el proceso de matriculacion
        """
        response = self.client.open('/matriculacion/Cerrar',
                                    method='POST')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
