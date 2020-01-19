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


class BankingCreditCardAccount(object):
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
        'min_payment_amount': 'str',
        'payment_due_amount': 'str',
        'payment_currency': 'str',
        'payment_due_date': 'str'
    }

    attribute_map = {
        'min_payment_amount': 'minPaymentAmount',
        'payment_due_amount': 'paymentDueAmount',
        'payment_currency': 'paymentCurrency',
        'payment_due_date': 'paymentDueDate'
    }

    def __init__(self, min_payment_amount=None, payment_due_amount=None, payment_currency=None, payment_due_date=None):  # noqa: E501
        """BankingCreditCardAccount - a model defined in Swagger"""  # noqa: E501

        self._min_payment_amount = None
        self._payment_due_amount = None
        self._payment_currency = None
        self._payment_due_date = None
        self.discriminator = None

        self.min_payment_amount = min_payment_amount
        self.payment_due_amount = payment_due_amount
        if payment_currency is not None:
            self.payment_currency = payment_currency
        self.payment_due_date = payment_due_date

    @property
    def min_payment_amount(self):
        """Gets the min_payment_amount of this BankingCreditCardAccount.  # noqa: E501

        The minimum payment amount due for the next card payment  # noqa: E501

        :return: The min_payment_amount of this BankingCreditCardAccount.  # noqa: E501
        :rtype: str
        """
        return self._min_payment_amount

    @min_payment_amount.setter
    def min_payment_amount(self, min_payment_amount):
        """Sets the min_payment_amount of this BankingCreditCardAccount.

        The minimum payment amount due for the next card payment  # noqa: E501

        :param min_payment_amount: The min_payment_amount of this BankingCreditCardAccount.  # noqa: E501
        :type: str
        """
        if min_payment_amount is None:
            raise ValueError("Invalid value for `min_payment_amount`, must not be `None`")  # noqa: E501

        self._min_payment_amount = min_payment_amount

    @property
    def payment_due_amount(self):
        """Gets the payment_due_amount of this BankingCreditCardAccount.  # noqa: E501

        The amount due for the next card payment  # noqa: E501

        :return: The payment_due_amount of this BankingCreditCardAccount.  # noqa: E501
        :rtype: str
        """
        return self._payment_due_amount

    @payment_due_amount.setter
    def payment_due_amount(self, payment_due_amount):
        """Sets the payment_due_amount of this BankingCreditCardAccount.

        The amount due for the next card payment  # noqa: E501

        :param payment_due_amount: The payment_due_amount of this BankingCreditCardAccount.  # noqa: E501
        :type: str
        """
        if payment_due_amount is None:
            raise ValueError("Invalid value for `payment_due_amount`, must not be `None`")  # noqa: E501

        self._payment_due_amount = payment_due_amount

    @property
    def payment_currency(self):
        """Gets the payment_currency of this BankingCreditCardAccount.  # noqa: E501

        If absent assumes AUD  # noqa: E501

        :return: The payment_currency of this BankingCreditCardAccount.  # noqa: E501
        :rtype: str
        """
        return self._payment_currency

    @payment_currency.setter
    def payment_currency(self, payment_currency):
        """Sets the payment_currency of this BankingCreditCardAccount.

        If absent assumes AUD  # noqa: E501

        :param payment_currency: The payment_currency of this BankingCreditCardAccount.  # noqa: E501
        :type: str
        """

        self._payment_currency = payment_currency

    @property
    def payment_due_date(self):
        """Gets the payment_due_date of this BankingCreditCardAccount.  # noqa: E501

        Date that the next payment for the card is due  # noqa: E501

        :return: The payment_due_date of this BankingCreditCardAccount.  # noqa: E501
        :rtype: str
        """
        return self._payment_due_date

    @payment_due_date.setter
    def payment_due_date(self, payment_due_date):
        """Sets the payment_due_date of this BankingCreditCardAccount.

        Date that the next payment for the card is due  # noqa: E501

        :param payment_due_date: The payment_due_date of this BankingCreditCardAccount.  # noqa: E501
        :type: str
        """
        if payment_due_date is None:
            raise ValueError("Invalid value for `payment_due_date`, must not be `None`")  # noqa: E501

        self._payment_due_date = payment_due_date

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
        if issubclass(BankingCreditCardAccount, dict):
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
        if not isinstance(other, BankingCreditCardAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
