# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.inline_response200 import InlineResponse200
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestPagosController(BaseTestCase):
    """ PagosController integration test stubs """

    def test_pagos_get(self):
        """
        Test case for pagos_get

        Consulta la nomina del profesor
        """
        query_string = [('dni', 56)]
        response = self.client.open('/cobros/pagos',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
