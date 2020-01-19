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


class BankingProductV2CardArt(object):
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
        'title': 'str',
        'image_uri': 'str'
    }

    attribute_map = {
        'title': 'title',
        'image_uri': 'imageUri'
    }

    def __init__(self, title=None, image_uri=None):  # noqa: E501
        """BankingProductV2CardArt - a model defined in Swagger"""  # noqa: E501

        self._title = None
        self._image_uri = None
        self.discriminator = None

        if title is not None:
            self.title = title
        self.image_uri = image_uri

    @property
    def title(self):
        """Gets the title of this BankingProductV2CardArt.  # noqa: E501

        Display label for the specific image  # noqa: E501

        :return: The title of this BankingProductV2CardArt.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this BankingProductV2CardArt.

        Display label for the specific image  # noqa: E501

        :param title: The title of this BankingProductV2CardArt.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def image_uri(self):
        """Gets the image_uri of this BankingProductV2CardArt.  # noqa: E501

        Link to a PNG, JPG or GIF image with proportions defined by ISO 7810 ID-1 and width no greater than 512 pixels  # noqa: E501

        :return: The image_uri of this BankingProductV2CardArt.  # noqa: E501
        :rtype: str
        """
        return self._image_uri

    @image_uri.setter
    def image_uri(self, image_uri):
        """Sets the image_uri of this BankingProductV2CardArt.

        Link to a PNG, JPG or GIF image with proportions defined by ISO 7810 ID-1 and width no greater than 512 pixels  # noqa: E501

        :param image_uri: The image_uri of this BankingProductV2CardArt.  # noqa: E501
        :type: str
        """
        if image_uri is None:
            raise ValueError("Invalid value for `image_uri`, must not be `None`")  # noqa: E501

        self._image_uri = image_uri

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
        if issubclass(BankingProductV2CardArt, dict):
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
        if not isinstance(other, BankingProductV2CardArt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
