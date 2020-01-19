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


class CommonPhysicalAddressWithPurpose(object):
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
        'address_u_type': 'str',
        'simple': 'CommonSimpleAddress',
        'paf': 'CommonPAFAddress',
        'purpose': 'str'
    }

    attribute_map = {
        'address_u_type': 'addressUType',
        'simple': 'simple',
        'paf': 'paf',
        'purpose': 'purpose'
    }

    def __init__(self, address_u_type=None, simple=None, paf=None, purpose=None):  # noqa: E501
        """CommonPhysicalAddressWithPurpose - a model defined in Swagger"""  # noqa: E501

        self._address_u_type = None
        self._simple = None
        self._paf = None
        self._purpose = None
        self.discriminator = None

        self.address_u_type = address_u_type
        if simple is not None:
            self.simple = simple
        if paf is not None:
            self.paf = paf
        self.purpose = purpose

    @property
    def address_u_type(self):
        """Gets the address_u_type of this CommonPhysicalAddressWithPurpose.  # noqa: E501

        The type of address object present  # noqa: E501

        :return: The address_u_type of this CommonPhysicalAddressWithPurpose.  # noqa: E501
        :rtype: str
        """
        return self._address_u_type

    @address_u_type.setter
    def address_u_type(self, address_u_type):
        """Sets the address_u_type of this CommonPhysicalAddressWithPurpose.

        The type of address object present  # noqa: E501

        :param address_u_type: The address_u_type of this CommonPhysicalAddressWithPurpose.  # noqa: E501
        :type: str
        """
        if address_u_type is None:
            raise ValueError("Invalid value for `address_u_type`, must not be `None`")  # noqa: E501
        allowed_values = ["simple", "paf"]  # noqa: E501
        if address_u_type not in allowed_values:
            raise ValueError(
                "Invalid value for `address_u_type` ({0}), must be one of {1}"  # noqa: E501
                .format(address_u_type, allowed_values)
            )

        self._address_u_type = address_u_type

    @property
    def simple(self):
        """Gets the simple of this CommonPhysicalAddressWithPurpose.  # noqa: E501


        :return: The simple of this CommonPhysicalAddressWithPurpose.  # noqa: E501
        :rtype: CommonSimpleAddress
        """
        return self._simple

    @simple.setter
    def simple(self, simple):
        """Sets the simple of this CommonPhysicalAddressWithPurpose.


        :param simple: The simple of this CommonPhysicalAddressWithPurpose.  # noqa: E501
        :type: CommonSimpleAddress
        """

        self._simple = simple

    @property
    def paf(self):
        """Gets the paf of this CommonPhysicalAddressWithPurpose.  # noqa: E501


        :return: The paf of this CommonPhysicalAddressWithPurpose.  # noqa: E501
        :rtype: CommonPAFAddress
        """
        return self._paf

    @paf.setter
    def paf(self, paf):
        """Sets the paf of this CommonPhysicalAddressWithPurpose.


        :param paf: The paf of this CommonPhysicalAddressWithPurpose.  # noqa: E501
        :type: CommonPAFAddress
        """

        self._paf = paf

    @property
    def purpose(self):
        """Gets the purpose of this CommonPhysicalAddressWithPurpose.  # noqa: E501

        Enumeration of values indicating the purpose of the physical address  # noqa: E501

        :return: The purpose of this CommonPhysicalAddressWithPurpose.  # noqa: E501
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this CommonPhysicalAddressWithPurpose.

        Enumeration of values indicating the purpose of the physical address  # noqa: E501

        :param purpose: The purpose of this CommonPhysicalAddressWithPurpose.  # noqa: E501
        :type: str
        """
        if purpose is None:
            raise ValueError("Invalid value for `purpose`, must not be `None`")  # noqa: E501
        allowed_values = ["REGISTERED", "MAIL", "PHYSICAL", "WORK", "OTHER"]  # noqa: E501
        if purpose not in allowed_values:
            raise ValueError(
                "Invalid value for `purpose` ({0}), must be one of {1}"  # noqa: E501
                .format(purpose, allowed_values)
            )

        self._purpose = purpose

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
        if issubclass(CommonPhysicalAddressWithPurpose, dict):
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
        if not isinstance(other, CommonPhysicalAddressWithPurpose):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other