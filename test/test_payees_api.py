# coding: utf-8

"""
    Consumer Data Standards

    API sets created by the Australian Consumer Data Standards to meet the needs of the Consumer Data Right  # noqa: E501

    OpenAPI spec version: 1.1.1
    Contact: cdr-data61@csiro.au
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.payees_api import PayeesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPayeesApi(unittest.TestCase):
    """PayeesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.payees_api.PayeesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_payee_detail(self):
        """Test case for get_payee_detail

        Get Payee Detail  # noqa: E501
        """
        pass

    def test_list_payees(self):
        """Test case for list_payees

        Get Payees  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
