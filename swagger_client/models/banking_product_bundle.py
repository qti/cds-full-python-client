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


class BankingProductBundle(object):
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
        'name': 'str',
        'description': 'str',
        'additional_info': 'str',
        'additional_info_uri': 'str',
        'product_ids': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'additional_info': 'additionalInfo',
        'additional_info_uri': 'additionalInfoUri',
        'product_ids': 'productIds'
    }

    def __init__(self, name=None, description=None, additional_info=None, additional_info_uri=None, product_ids=None):  # noqa: E501
        """BankingProductBundle - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._additional_info = None
        self._additional_info_uri = None
        self._product_ids = None
        self.discriminator = None

        self.name = name
        self.description = description
        if additional_info is not None:
            self.additional_info = additional_info
        if additional_info_uri is not None:
            self.additional_info_uri = additional_info_uri
        if product_ids is not None:
            self.product_ids = product_ids

    @property
    def name(self):
        """Gets the name of this BankingProductBundle.  # noqa: E501

        Name of the bundle  # noqa: E501

        :return: The name of this BankingProductBundle.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BankingProductBundle.

        Name of the bundle  # noqa: E501

        :param name: The name of this BankingProductBundle.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this BankingProductBundle.  # noqa: E501

        Description of the bundle  # noqa: E501

        :return: The description of this BankingProductBundle.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BankingProductBundle.

        Description of the bundle  # noqa: E501

        :param description: The description of this BankingProductBundle.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def additional_info(self):
        """Gets the additional_info of this BankingProductBundle.  # noqa: E501

        Display text providing more information on the bundle  # noqa: E501

        :return: The additional_info of this BankingProductBundle.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this BankingProductBundle.

        Display text providing more information on the bundle  # noqa: E501

        :param additional_info: The additional_info of this BankingProductBundle.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def additional_info_uri(self):
        """Gets the additional_info_uri of this BankingProductBundle.  # noqa: E501

        Link to a web page with more information on the bundle criteria and benefits  # noqa: E501

        :return: The additional_info_uri of this BankingProductBundle.  # noqa: E501
        :rtype: str
        """
        return self._additional_info_uri

    @additional_info_uri.setter
    def additional_info_uri(self, additional_info_uri):
        """Sets the additional_info_uri of this BankingProductBundle.

        Link to a web page with more information on the bundle criteria and benefits  # noqa: E501

        :param additional_info_uri: The additional_info_uri of this BankingProductBundle.  # noqa: E501
        :type: str
        """

        self._additional_info_uri = additional_info_uri

    @property
    def product_ids(self):
        """Gets the product_ids of this BankingProductBundle.  # noqa: E501

        Array of product IDs for products included in the bundle that are available via the product end points.  Note that this array is not intended to represent a comprehensive model of the products included in the bundle and some products available for the bundle may not be available via the product reference end points  # noqa: E501

        :return: The product_ids of this BankingProductBundle.  # noqa: E501
        :rtype: list[str]
        """
        return self._product_ids

    @product_ids.setter
    def product_ids(self, product_ids):
        """Sets the product_ids of this BankingProductBundle.

        Array of product IDs for products included in the bundle that are available via the product end points.  Note that this array is not intended to represent a comprehensive model of the products included in the bundle and some products available for the bundle may not be available via the product reference end points  # noqa: E501

        :param product_ids: The product_ids of this BankingProductBundle.  # noqa: E501
        :type: list[str]
        """

        self._product_ids = product_ids

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
        if issubclass(BankingProductBundle, dict):
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
        if not isinstance(other, BankingProductBundle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
