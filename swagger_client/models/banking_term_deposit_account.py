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


class BankingTermDepositAccount(object):
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
        'lodgement_date': 'str',
        'maturity_date': 'str',
        'maturity_amount': 'str',
        'maturity_currency': 'str',
        'maturity_instructions': 'str'
    }

    attribute_map = {
        'lodgement_date': 'lodgementDate',
        'maturity_date': 'maturityDate',
        'maturity_amount': 'maturityAmount',
        'maturity_currency': 'maturityCurrency',
        'maturity_instructions': 'maturityInstructions'
    }

    def __init__(self, lodgement_date=None, maturity_date=None, maturity_amount=None, maturity_currency=None, maturity_instructions=None):  # noqa: E501
        """BankingTermDepositAccount - a model defined in Swagger"""  # noqa: E501

        self._lodgement_date = None
        self._maturity_date = None
        self._maturity_amount = None
        self._maturity_currency = None
        self._maturity_instructions = None
        self.discriminator = None

        self.lodgement_date = lodgement_date
        self.maturity_date = maturity_date
        if maturity_amount is not None:
            self.maturity_amount = maturity_amount
        if maturity_currency is not None:
            self.maturity_currency = maturity_currency
        self.maturity_instructions = maturity_instructions

    @property
    def lodgement_date(self):
        """Gets the lodgement_date of this BankingTermDepositAccount.  # noqa: E501

        The lodgement date of the original deposit  # noqa: E501

        :return: The lodgement_date of this BankingTermDepositAccount.  # noqa: E501
        :rtype: str
        """
        return self._lodgement_date

    @lodgement_date.setter
    def lodgement_date(self, lodgement_date):
        """Sets the lodgement_date of this BankingTermDepositAccount.

        The lodgement date of the original deposit  # noqa: E501

        :param lodgement_date: The lodgement_date of this BankingTermDepositAccount.  # noqa: E501
        :type: str
        """
        if lodgement_date is None:
            raise ValueError("Invalid value for `lodgement_date`, must not be `None`")  # noqa: E501

        self._lodgement_date = lodgement_date

    @property
    def maturity_date(self):
        """Gets the maturity_date of this BankingTermDepositAccount.  # noqa: E501

        Maturity date for the term deposit  # noqa: E501

        :return: The maturity_date of this BankingTermDepositAccount.  # noqa: E501
        :rtype: str
        """
        return self._maturity_date

    @maturity_date.setter
    def maturity_date(self, maturity_date):
        """Sets the maturity_date of this BankingTermDepositAccount.

        Maturity date for the term deposit  # noqa: E501

        :param maturity_date: The maturity_date of this BankingTermDepositAccount.  # noqa: E501
        :type: str
        """
        if maturity_date is None:
            raise ValueError("Invalid value for `maturity_date`, must not be `None`")  # noqa: E501

        self._maturity_date = maturity_date

    @property
    def maturity_amount(self):
        """Gets the maturity_amount of this BankingTermDepositAccount.  # noqa: E501

        Amount to be paid upon maturity. If absent it implies the amount to paid is variable and cannot currently be calculated  # noqa: E501

        :return: The maturity_amount of this BankingTermDepositAccount.  # noqa: E501
        :rtype: str
        """
        return self._maturity_amount

    @maturity_amount.setter
    def maturity_amount(self, maturity_amount):
        """Sets the maturity_amount of this BankingTermDepositAccount.

        Amount to be paid upon maturity. If absent it implies the amount to paid is variable and cannot currently be calculated  # noqa: E501

        :param maturity_amount: The maturity_amount of this BankingTermDepositAccount.  # noqa: E501
        :type: str
        """

        self._maturity_amount = maturity_amount

    @property
    def maturity_currency(self):
        """Gets the maturity_currency of this BankingTermDepositAccount.  # noqa: E501

        If absent assumes AUD  # noqa: E501

        :return: The maturity_currency of this BankingTermDepositAccount.  # noqa: E501
        :rtype: str
        """
        return self._maturity_currency

    @maturity_currency.setter
    def maturity_currency(self, maturity_currency):
        """Sets the maturity_currency of this BankingTermDepositAccount.

        If absent assumes AUD  # noqa: E501

        :param maturity_currency: The maturity_currency of this BankingTermDepositAccount.  # noqa: E501
        :type: str
        """

        self._maturity_currency = maturity_currency

    @property
    def maturity_instructions(self):
        """Gets the maturity_instructions of this BankingTermDepositAccount.  # noqa: E501

        Current instructions on action to be taken at maturity  # noqa: E501

        :return: The maturity_instructions of this BankingTermDepositAccount.  # noqa: E501
        :rtype: str
        """
        return self._maturity_instructions

    @maturity_instructions.setter
    def maturity_instructions(self, maturity_instructions):
        """Sets the maturity_instructions of this BankingTermDepositAccount.

        Current instructions on action to be taken at maturity  # noqa: E501

        :param maturity_instructions: The maturity_instructions of this BankingTermDepositAccount.  # noqa: E501
        :type: str
        """
        if maturity_instructions is None:
            raise ValueError("Invalid value for `maturity_instructions`, must not be `None`")  # noqa: E501
        allowed_values = ["ROLLED_OVER", "PAID_OUT_AT_MATURITY"]  # noqa: E501
        if maturity_instructions not in allowed_values:
            raise ValueError(
                "Invalid value for `maturity_instructions` ({0}), must be one of {1}"  # noqa: E501
                .format(maturity_instructions, allowed_values)
            )

        self._maturity_instructions = maturity_instructions

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
        if issubclass(BankingTermDepositAccount, dict):
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
        if not isinstance(other, BankingTermDepositAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
