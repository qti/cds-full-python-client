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


class BankingTransactionDetailExtendedDataX2p101Payload(object):
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
        'extended_description': 'str',
        'end_to_end_id': 'str',
        'purpose_code': 'str'
    }

    attribute_map = {
        'extended_description': 'extendedDescription',
        'end_to_end_id': 'endToEndId',
        'purpose_code': 'purposeCode'
    }

    def __init__(self, extended_description=None, end_to_end_id=None, purpose_code=None):  # noqa: E501
        """BankingTransactionDetailExtendedDataX2p101Payload - a model defined in Swagger"""  # noqa: E501

        self._extended_description = None
        self._end_to_end_id = None
        self._purpose_code = None
        self.discriminator = None

        self.extended_description = extended_description
        if end_to_end_id is not None:
            self.end_to_end_id = end_to_end_id
        if purpose_code is not None:
            self.purpose_code = purpose_code

    @property
    def extended_description(self):
        """Gets the extended_description of this BankingTransactionDetailExtendedDataX2p101Payload.  # noqa: E501

        An extended string description. Only present if specified by the extensionUType field  # noqa: E501

        :return: The extended_description of this BankingTransactionDetailExtendedDataX2p101Payload.  # noqa: E501
        :rtype: str
        """
        return self._extended_description

    @extended_description.setter
    def extended_description(self, extended_description):
        """Sets the extended_description of this BankingTransactionDetailExtendedDataX2p101Payload.

        An extended string description. Only present if specified by the extensionUType field  # noqa: E501

        :param extended_description: The extended_description of this BankingTransactionDetailExtendedDataX2p101Payload.  # noqa: E501
        :type: str
        """
        if extended_description is None:
            raise ValueError("Invalid value for `extended_description`, must not be `None`")  # noqa: E501

        self._extended_description = extended_description

    @property
    def end_to_end_id(self):
        """Gets the end_to_end_id of this BankingTransactionDetailExtendedDataX2p101Payload.  # noqa: E501

        An end to end ID for the payment created at initiation  # noqa: E501

        :return: The end_to_end_id of this BankingTransactionDetailExtendedDataX2p101Payload.  # noqa: E501
        :rtype: str
        """
        return self._end_to_end_id

    @end_to_end_id.setter
    def end_to_end_id(self, end_to_end_id):
        """Sets the end_to_end_id of this BankingTransactionDetailExtendedDataX2p101Payload.

        An end to end ID for the payment created at initiation  # noqa: E501

        :param end_to_end_id: The end_to_end_id of this BankingTransactionDetailExtendedDataX2p101Payload.  # noqa: E501
        :type: str
        """

        self._end_to_end_id = end_to_end_id

    @property
    def purpose_code(self):
        """Gets the purpose_code of this BankingTransactionDetailExtendedDataX2p101Payload.  # noqa: E501

        Purpose of the payment.  Format is defined by NPP standards for the x2p1.01 overlay service  # noqa: E501

        :return: The purpose_code of this BankingTransactionDetailExtendedDataX2p101Payload.  # noqa: E501
        :rtype: str
        """
        return self._purpose_code

    @purpose_code.setter
    def purpose_code(self, purpose_code):
        """Sets the purpose_code of this BankingTransactionDetailExtendedDataX2p101Payload.

        Purpose of the payment.  Format is defined by NPP standards for the x2p1.01 overlay service  # noqa: E501

        :param purpose_code: The purpose_code of this BankingTransactionDetailExtendedDataX2p101Payload.  # noqa: E501
        :type: str
        """

        self._purpose_code = purpose_code

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
        if issubclass(BankingTransactionDetailExtendedDataX2p101Payload, dict):
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
        if not isinstance(other, BankingTransactionDetailExtendedDataX2p101Payload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
