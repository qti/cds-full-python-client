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


class BankingScheduledPaymentSet(object):
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
        'to': 'BankingScheduledPaymentTo',
        'is_amount_calculated': 'bool',
        'amount': 'str',
        'currency': 'str'
    }

    attribute_map = {
        'to': 'to',
        'is_amount_calculated': 'isAmountCalculated',
        'amount': 'amount',
        'currency': 'currency'
    }

    def __init__(self, to=None, is_amount_calculated=None, amount=None, currency=None):  # noqa: E501
        """BankingScheduledPaymentSet - a model defined in Swagger"""  # noqa: E501

        self._to = None
        self._is_amount_calculated = None
        self._amount = None
        self._currency = None
        self.discriminator = None

        self.to = to
        if is_amount_calculated is not None:
            self.is_amount_calculated = is_amount_calculated
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency

    @property
    def to(self):
        """Gets the to of this BankingScheduledPaymentSet.  # noqa: E501


        :return: The to of this BankingScheduledPaymentSet.  # noqa: E501
        :rtype: BankingScheduledPaymentTo
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this BankingScheduledPaymentSet.


        :param to: The to of this BankingScheduledPaymentSet.  # noqa: E501
        :type: BankingScheduledPaymentTo
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def is_amount_calculated(self):
        """Gets the is_amount_calculated of this BankingScheduledPaymentSet.  # noqa: E501

        Flag indicating whether the amount of the payment is calculated based on the context of the event. For instance a payment to reduce the balance of a credit card to zero. If absent then false is assumed  # noqa: E501

        :return: The is_amount_calculated of this BankingScheduledPaymentSet.  # noqa: E501
        :rtype: bool
        """
        return self._is_amount_calculated

    @is_amount_calculated.setter
    def is_amount_calculated(self, is_amount_calculated):
        """Sets the is_amount_calculated of this BankingScheduledPaymentSet.

        Flag indicating whether the amount of the payment is calculated based on the context of the event. For instance a payment to reduce the balance of a credit card to zero. If absent then false is assumed  # noqa: E501

        :param is_amount_calculated: The is_amount_calculated of this BankingScheduledPaymentSet.  # noqa: E501
        :type: bool
        """

        self._is_amount_calculated = is_amount_calculated

    @property
    def amount(self):
        """Gets the amount of this BankingScheduledPaymentSet.  # noqa: E501

        The amount of the next payment if known. Mandatory unless the isAmountCalculated field is set to true. Must be zero or positive if present  # noqa: E501

        :return: The amount of this BankingScheduledPaymentSet.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this BankingScheduledPaymentSet.

        The amount of the next payment if known. Mandatory unless the isAmountCalculated field is set to true. Must be zero or positive if present  # noqa: E501

        :param amount: The amount of this BankingScheduledPaymentSet.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this BankingScheduledPaymentSet.  # noqa: E501

        The currency for the payment. AUD assumed if not present  # noqa: E501

        :return: The currency of this BankingScheduledPaymentSet.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this BankingScheduledPaymentSet.

        The currency for the payment. AUD assumed if not present  # noqa: E501

        :param currency: The currency of this BankingScheduledPaymentSet.  # noqa: E501
        :type: str
        """

        self._currency = currency

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
        if issubclass(BankingScheduledPaymentSet, dict):
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
        if not isinstance(other, BankingScheduledPaymentSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
