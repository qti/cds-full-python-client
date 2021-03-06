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


class BankingBalance(object):
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
        'account_id': 'str',
        'current_balance': 'str',
        'available_balance': 'str',
        'credit_limit': 'str',
        'amortised_limit': 'str',
        'currency': 'str',
        'purses': 'list[BankingBalancePurse]'
    }

    attribute_map = {
        'account_id': 'accountId',
        'current_balance': 'currentBalance',
        'available_balance': 'availableBalance',
        'credit_limit': 'creditLimit',
        'amortised_limit': 'amortisedLimit',
        'currency': 'currency',
        'purses': 'purses'
    }

    def __init__(self, account_id=None, current_balance=None, available_balance=None, credit_limit=None, amortised_limit=None, currency=None, purses=None):  # noqa: E501
        """BankingBalance - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._current_balance = None
        self._available_balance = None
        self._credit_limit = None
        self._amortised_limit = None
        self._currency = None
        self._purses = None
        self.discriminator = None

        self.account_id = account_id
        self.current_balance = current_balance
        self.available_balance = available_balance
        if credit_limit is not None:
            self.credit_limit = credit_limit
        if amortised_limit is not None:
            self.amortised_limit = amortised_limit
        if currency is not None:
            self.currency = currency
        if purses is not None:
            self.purses = purses

    @property
    def account_id(self):
        """Gets the account_id of this BankingBalance.  # noqa: E501

        A unique ID of the account adhering to the standards for ID permanence  # noqa: E501

        :return: The account_id of this BankingBalance.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this BankingBalance.

        A unique ID of the account adhering to the standards for ID permanence  # noqa: E501

        :param account_id: The account_id of this BankingBalance.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def current_balance(self):
        """Gets the current_balance of this BankingBalance.  # noqa: E501

        The balance of the account at this time. Should align to the balance available via other channels such as Internet Banking. Assumed to be negative if the customer has money owing  # noqa: E501

        :return: The current_balance of this BankingBalance.  # noqa: E501
        :rtype: str
        """
        return self._current_balance

    @current_balance.setter
    def current_balance(self, current_balance):
        """Sets the current_balance of this BankingBalance.

        The balance of the account at this time. Should align to the balance available via other channels such as Internet Banking. Assumed to be negative if the customer has money owing  # noqa: E501

        :param current_balance: The current_balance of this BankingBalance.  # noqa: E501
        :type: str
        """
        if current_balance is None:
            raise ValueError("Invalid value for `current_balance`, must not be `None`")  # noqa: E501

        self._current_balance = current_balance

    @property
    def available_balance(self):
        """Gets the available_balance of this BankingBalance.  # noqa: E501

        Balance representing the amount of funds available for transfer. Assumed to be zero or positive  # noqa: E501

        :return: The available_balance of this BankingBalance.  # noqa: E501
        :rtype: str
        """
        return self._available_balance

    @available_balance.setter
    def available_balance(self, available_balance):
        """Sets the available_balance of this BankingBalance.

        Balance representing the amount of funds available for transfer. Assumed to be zero or positive  # noqa: E501

        :param available_balance: The available_balance of this BankingBalance.  # noqa: E501
        :type: str
        """
        if available_balance is None:
            raise ValueError("Invalid value for `available_balance`, must not be `None`")  # noqa: E501

        self._available_balance = available_balance

    @property
    def credit_limit(self):
        """Gets the credit_limit of this BankingBalance.  # noqa: E501

        Object representing the maximum amount of credit that is available for this account. Assumed to be zero if absent  # noqa: E501

        :return: The credit_limit of this BankingBalance.  # noqa: E501
        :rtype: str
        """
        return self._credit_limit

    @credit_limit.setter
    def credit_limit(self, credit_limit):
        """Sets the credit_limit of this BankingBalance.

        Object representing the maximum amount of credit that is available for this account. Assumed to be zero if absent  # noqa: E501

        :param credit_limit: The credit_limit of this BankingBalance.  # noqa: E501
        :type: str
        """

        self._credit_limit = credit_limit

    @property
    def amortised_limit(self):
        """Gets the amortised_limit of this BankingBalance.  # noqa: E501

        Object representing the available limit amortised according to payment schedule. Assumed to be zero if absent  # noqa: E501

        :return: The amortised_limit of this BankingBalance.  # noqa: E501
        :rtype: str
        """
        return self._amortised_limit

    @amortised_limit.setter
    def amortised_limit(self, amortised_limit):
        """Sets the amortised_limit of this BankingBalance.

        Object representing the available limit amortised according to payment schedule. Assumed to be zero if absent  # noqa: E501

        :param amortised_limit: The amortised_limit of this BankingBalance.  # noqa: E501
        :type: str
        """

        self._amortised_limit = amortised_limit

    @property
    def currency(self):
        """Gets the currency of this BankingBalance.  # noqa: E501

        The currency for the balance amounts. If absent assumed to be AUD  # noqa: E501

        :return: The currency of this BankingBalance.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this BankingBalance.

        The currency for the balance amounts. If absent assumed to be AUD  # noqa: E501

        :param currency: The currency of this BankingBalance.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def purses(self):
        """Gets the purses of this BankingBalance.  # noqa: E501

        Optional array of balances for the account in other currencies. Included to support accounts that support multi-currency purses such as Travel Cards  # noqa: E501

        :return: The purses of this BankingBalance.  # noqa: E501
        :rtype: list[BankingBalancePurse]
        """
        return self._purses

    @purses.setter
    def purses(self, purses):
        """Sets the purses of this BankingBalance.

        Optional array of balances for the account in other currencies. Included to support accounts that support multi-currency purses such as Travel Cards  # noqa: E501

        :param purses: The purses of this BankingBalance.  # noqa: E501
        :type: list[BankingBalancePurse]
        """

        self._purses = purses

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
        if issubclass(BankingBalance, dict):
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
        if not isinstance(other, BankingBalance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
