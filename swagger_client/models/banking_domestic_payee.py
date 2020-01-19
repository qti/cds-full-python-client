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


class BankingDomesticPayee(object):
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
        'payee_account_u_type': 'str',
        'account': 'BankingDomesticPayeeAccount',
        'card': 'BankingDomesticPayeeCard',
        'pay_id': 'BankingDomesticPayeePayId'
    }

    attribute_map = {
        'payee_account_u_type': 'payeeAccountUType',
        'account': 'account',
        'card': 'card',
        'pay_id': 'payId'
    }

    def __init__(self, payee_account_u_type=None, account=None, card=None, pay_id=None):  # noqa: E501
        """BankingDomesticPayee - a model defined in Swagger"""  # noqa: E501

        self._payee_account_u_type = None
        self._account = None
        self._card = None
        self._pay_id = None
        self.discriminator = None

        self.payee_account_u_type = payee_account_u_type
        if account is not None:
            self.account = account
        if card is not None:
            self.card = card
        if pay_id is not None:
            self.pay_id = pay_id

    @property
    def payee_account_u_type(self):
        """Gets the payee_account_u_type of this BankingDomesticPayee.  # noqa: E501

        Type of account object included. Valid values are: **account** A standard Australian account defined by BSB/Account Number. **card** A credit or charge card to pay to (note that PANs are masked). **payId** A PayID recognised by NPP  # noqa: E501

        :return: The payee_account_u_type of this BankingDomesticPayee.  # noqa: E501
        :rtype: str
        """
        return self._payee_account_u_type

    @payee_account_u_type.setter
    def payee_account_u_type(self, payee_account_u_type):
        """Sets the payee_account_u_type of this BankingDomesticPayee.

        Type of account object included. Valid values are: **account** A standard Australian account defined by BSB/Account Number. **card** A credit or charge card to pay to (note that PANs are masked). **payId** A PayID recognised by NPP  # noqa: E501

        :param payee_account_u_type: The payee_account_u_type of this BankingDomesticPayee.  # noqa: E501
        :type: str
        """
        if payee_account_u_type is None:
            raise ValueError("Invalid value for `payee_account_u_type`, must not be `None`")  # noqa: E501
        allowed_values = ["account", "card", "payId"]  # noqa: E501
        if payee_account_u_type not in allowed_values:
            raise ValueError(
                "Invalid value for `payee_account_u_type` ({0}), must be one of {1}"  # noqa: E501
                .format(payee_account_u_type, allowed_values)
            )

        self._payee_account_u_type = payee_account_u_type

    @property
    def account(self):
        """Gets the account of this BankingDomesticPayee.  # noqa: E501


        :return: The account of this BankingDomesticPayee.  # noqa: E501
        :rtype: BankingDomesticPayeeAccount
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this BankingDomesticPayee.


        :param account: The account of this BankingDomesticPayee.  # noqa: E501
        :type: BankingDomesticPayeeAccount
        """

        self._account = account

    @property
    def card(self):
        """Gets the card of this BankingDomesticPayee.  # noqa: E501


        :return: The card of this BankingDomesticPayee.  # noqa: E501
        :rtype: BankingDomesticPayeeCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """Sets the card of this BankingDomesticPayee.


        :param card: The card of this BankingDomesticPayee.  # noqa: E501
        :type: BankingDomesticPayeeCard
        """

        self._card = card

    @property
    def pay_id(self):
        """Gets the pay_id of this BankingDomesticPayee.  # noqa: E501


        :return: The pay_id of this BankingDomesticPayee.  # noqa: E501
        :rtype: BankingDomesticPayeePayId
        """
        return self._pay_id

    @pay_id.setter
    def pay_id(self, pay_id):
        """Sets the pay_id of this BankingDomesticPayee.


        :param pay_id: The pay_id of this BankingDomesticPayee.  # noqa: E501
        :type: BankingDomesticPayeePayId
        """

        self._pay_id = pay_id

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
        if issubclass(BankingDomesticPayee, dict):
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
        if not isinstance(other, BankingDomesticPayee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other