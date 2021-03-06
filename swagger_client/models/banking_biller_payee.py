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


class BankingBillerPayee(object):
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
        'biller_code': 'str',
        'crn': 'str',
        'biller_name': 'str'
    }

    attribute_map = {
        'biller_code': 'billerCode',
        'crn': 'crn',
        'biller_name': 'billerName'
    }

    def __init__(self, biller_code=None, crn=None, biller_name=None):  # noqa: E501
        """BankingBillerPayee - a model defined in Swagger"""  # noqa: E501

        self._biller_code = None
        self._crn = None
        self._biller_name = None
        self.discriminator = None

        self.biller_code = biller_code
        if crn is not None:
            self.crn = crn
        self.biller_name = biller_name

    @property
    def biller_code(self):
        """Gets the biller_code of this BankingBillerPayee.  # noqa: E501

        BPAY Biller Code of the Biller  # noqa: E501

        :return: The biller_code of this BankingBillerPayee.  # noqa: E501
        :rtype: str
        """
        return self._biller_code

    @biller_code.setter
    def biller_code(self, biller_code):
        """Sets the biller_code of this BankingBillerPayee.

        BPAY Biller Code of the Biller  # noqa: E501

        :param biller_code: The biller_code of this BankingBillerPayee.  # noqa: E501
        :type: str
        """
        if biller_code is None:
            raise ValueError("Invalid value for `biller_code`, must not be `None`")  # noqa: E501

        self._biller_code = biller_code

    @property
    def crn(self):
        """Gets the crn of this BankingBillerPayee.  # noqa: E501

        BPAY CRN of the Biller. If the contents of the CRN match the format of a Credit Card PAN then it should be masked using the rules applicable for the MaskedPANString common type  # noqa: E501

        :return: The crn of this BankingBillerPayee.  # noqa: E501
        :rtype: str
        """
        return self._crn

    @crn.setter
    def crn(self, crn):
        """Sets the crn of this BankingBillerPayee.

        BPAY CRN of the Biller. If the contents of the CRN match the format of a Credit Card PAN then it should be masked using the rules applicable for the MaskedPANString common type  # noqa: E501

        :param crn: The crn of this BankingBillerPayee.  # noqa: E501
        :type: str
        """

        self._crn = crn

    @property
    def biller_name(self):
        """Gets the biller_name of this BankingBillerPayee.  # noqa: E501

        Name of the Biller  # noqa: E501

        :return: The biller_name of this BankingBillerPayee.  # noqa: E501
        :rtype: str
        """
        return self._biller_name

    @biller_name.setter
    def biller_name(self, biller_name):
        """Sets the biller_name of this BankingBillerPayee.

        Name of the Biller  # noqa: E501

        :param biller_name: The biller_name of this BankingBillerPayee.  # noqa: E501
        :type: str
        """
        if biller_name is None:
            raise ValueError("Invalid value for `biller_name`, must not be `None`")  # noqa: E501

        self._biller_name = biller_name

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
        if issubclass(BankingBillerPayee, dict):
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
        if not isinstance(other, BankingBillerPayee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
