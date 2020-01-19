# coding: utf-8

"""
    Consumer Data Standards

    API sets created by the Australian Consumer Data Standards to meet the needs of the Consumer Data Right  # noqa: E501

    OpenAPI spec version: 1.1.1
    Contact: cdr-data61@csiro.au
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ResponseBankingDirectDebitAuthorisationListData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'direct_debit_authorisations': 'list[BankingDirectDebit]'
    }

    attribute_map = {
        'direct_debit_authorisations': 'directDebitAuthorisations'
    }

    def __init__(self, direct_debit_authorisations=None):  # noqa: E501
        """ResponseBankingDirectDebitAuthorisationListData - a model defined in Swagger"""  # noqa: E501

        self._direct_debit_authorisations = None
        self.discriminator = None

        self.direct_debit_authorisations = direct_debit_authorisations

    @property
    def direct_debit_authorisations(self):
        """Gets the direct_debit_authorisations of this ResponseBankingDirectDebitAuthorisationListData.  # noqa: E501

        The list of authorisations returned  # noqa: E501

        :return: The direct_debit_authorisations of this ResponseBankingDirectDebitAuthorisationListData.  # noqa: E501
        :rtype: list[BankingDirectDebit]
        """
        return self._direct_debit_authorisations

    @direct_debit_authorisations.setter
    def direct_debit_authorisations(self, direct_debit_authorisations):
        """Sets the direct_debit_authorisations of this ResponseBankingDirectDebitAuthorisationListData.

        The list of authorisations returned  # noqa: E501

        :param direct_debit_authorisations: The direct_debit_authorisations of this ResponseBankingDirectDebitAuthorisationListData.  # noqa: E501
        :type: list[BankingDirectDebit]
        """
        if direct_debit_authorisations is None:
            raise ValueError("Invalid value for `direct_debit_authorisations`, must not be `None`")  # noqa: E501

        self._direct_debit_authorisations = direct_debit_authorisations

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ResponseBankingDirectDebitAuthorisationListData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResponseBankingDirectDebitAuthorisationListData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
