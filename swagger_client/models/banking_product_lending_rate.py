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


class BankingProductLendingRate(object):
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
        'lending_rate_type': 'str',
        'rate': 'str',
        'comparison_rate': 'str',
        'calculation_frequency': 'str',
        'application_frequency': 'str',
        'interest_payment_due': 'str',
        'tiers': 'list[BankingProductRateTier]',
        'additional_value': 'str',
        'additional_info': 'str',
        'additional_info_uri': 'str'
    }

    attribute_map = {
        'lending_rate_type': 'lendingRateType',
        'rate': 'rate',
        'comparison_rate': 'comparisonRate',
        'calculation_frequency': 'calculationFrequency',
        'application_frequency': 'applicationFrequency',
        'interest_payment_due': 'interestPaymentDue',
        'tiers': 'tiers',
        'additional_value': 'additionalValue',
        'additional_info': 'additionalInfo',
        'additional_info_uri': 'additionalInfoUri'
    }

    def __init__(self, lending_rate_type=None, rate=None, comparison_rate=None, calculation_frequency=None, application_frequency=None, interest_payment_due=None, tiers=None, additional_value=None, additional_info=None, additional_info_uri=None):  # noqa: E501
        """BankingProductLendingRate - a model defined in Swagger"""  # noqa: E501

        self._lending_rate_type = None
        self._rate = None
        self._comparison_rate = None
        self._calculation_frequency = None
        self._application_frequency = None
        self._interest_payment_due = None
        self._tiers = None
        self._additional_value = None
        self._additional_info = None
        self._additional_info_uri = None
        self.discriminator = None

        self.lending_rate_type = lending_rate_type
        self.rate = rate
        if comparison_rate is not None:
            self.comparison_rate = comparison_rate
        if calculation_frequency is not None:
            self.calculation_frequency = calculation_frequency
        if application_frequency is not None:
            self.application_frequency = application_frequency
        if interest_payment_due is not None:
            self.interest_payment_due = interest_payment_due
        if tiers is not None:
            self.tiers = tiers
        if additional_value is not None:
            self.additional_value = additional_value
        if additional_info is not None:
            self.additional_info = additional_info
        if additional_info_uri is not None:
            self.additional_info_uri = additional_info_uri

    @property
    def lending_rate_type(self):
        """Gets the lending_rate_type of this BankingProductLendingRate.  # noqa: E501

        The type of rate (fixed, variable, etc). See the next section for an overview of valid values and their meaning  # noqa: E501

        :return: The lending_rate_type of this BankingProductLendingRate.  # noqa: E501
        :rtype: str
        """
        return self._lending_rate_type

    @lending_rate_type.setter
    def lending_rate_type(self, lending_rate_type):
        """Sets the lending_rate_type of this BankingProductLendingRate.

        The type of rate (fixed, variable, etc). See the next section for an overview of valid values and their meaning  # noqa: E501

        :param lending_rate_type: The lending_rate_type of this BankingProductLendingRate.  # noqa: E501
        :type: str
        """
        if lending_rate_type is None:
            raise ValueError("Invalid value for `lending_rate_type`, must not be `None`")  # noqa: E501
        allowed_values = ["FIXED", "VARIABLE", "INTRODUCTORY", "DISCOUNT", "PENALTY", "FLOATING", "MARKET_LINKED", "CASH_ADVANCE", "PURCHASE", "BUNDLE_DISCOUNT_FIXED", "BUNDLE_DISCOUNT_VARIABLE"]  # noqa: E501
        if lending_rate_type not in allowed_values:
            raise ValueError(
                "Invalid value for `lending_rate_type` ({0}), must be one of {1}"  # noqa: E501
                .format(lending_rate_type, allowed_values)
            )

        self._lending_rate_type = lending_rate_type

    @property
    def rate(self):
        """Gets the rate of this BankingProductLendingRate.  # noqa: E501

        The rate to be applied  # noqa: E501

        :return: The rate of this BankingProductLendingRate.  # noqa: E501
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this BankingProductLendingRate.

        The rate to be applied  # noqa: E501

        :param rate: The rate of this BankingProductLendingRate.  # noqa: E501
        :type: str
        """
        if rate is None:
            raise ValueError("Invalid value for `rate`, must not be `None`")  # noqa: E501

        self._rate = rate

    @property
    def comparison_rate(self):
        """Gets the comparison_rate of this BankingProductLendingRate.  # noqa: E501

        A comparison rate equivalent for this rate  # noqa: E501

        :return: The comparison_rate of this BankingProductLendingRate.  # noqa: E501
        :rtype: str
        """
        return self._comparison_rate

    @comparison_rate.setter
    def comparison_rate(self, comparison_rate):
        """Sets the comparison_rate of this BankingProductLendingRate.

        A comparison rate equivalent for this rate  # noqa: E501

        :param comparison_rate: The comparison_rate of this BankingProductLendingRate.  # noqa: E501
        :type: str
        """

        self._comparison_rate = comparison_rate

    @property
    def calculation_frequency(self):
        """Gets the calculation_frequency of this BankingProductLendingRate.  # noqa: E501

        The period after which the rate is applied to the balance to calculate the amount due for the period. Calculation of the amount is often daily (as balances may change) but accumulated until the total amount is 'applied' to the account (see applicationFrequency). Formatted according to [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations) (excludes recurrence syntax)  # noqa: E501

        :return: The calculation_frequency of this BankingProductLendingRate.  # noqa: E501
        :rtype: str
        """
        return self._calculation_frequency

    @calculation_frequency.setter
    def calculation_frequency(self, calculation_frequency):
        """Sets the calculation_frequency of this BankingProductLendingRate.

        The period after which the rate is applied to the balance to calculate the amount due for the period. Calculation of the amount is often daily (as balances may change) but accumulated until the total amount is 'applied' to the account (see applicationFrequency). Formatted according to [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations) (excludes recurrence syntax)  # noqa: E501

        :param calculation_frequency: The calculation_frequency of this BankingProductLendingRate.  # noqa: E501
        :type: str
        """

        self._calculation_frequency = calculation_frequency

    @property
    def application_frequency(self):
        """Gets the application_frequency of this BankingProductLendingRate.  # noqa: E501

        The period after which the calculated amount(s) (see calculationFrequency) are 'applied' (i.e. debited or credited) to the account. Formatted according to [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations) (excludes recurrence syntax)  # noqa: E501

        :return: The application_frequency of this BankingProductLendingRate.  # noqa: E501
        :rtype: str
        """
        return self._application_frequency

    @application_frequency.setter
    def application_frequency(self, application_frequency):
        """Sets the application_frequency of this BankingProductLendingRate.

        The period after which the calculated amount(s) (see calculationFrequency) are 'applied' (i.e. debited or credited) to the account. Formatted according to [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations) (excludes recurrence syntax)  # noqa: E501

        :param application_frequency: The application_frequency of this BankingProductLendingRate.  # noqa: E501
        :type: str
        """

        self._application_frequency = application_frequency

    @property
    def interest_payment_due(self):
        """Gets the interest_payment_due of this BankingProductLendingRate.  # noqa: E501

        When loan payments are due to be paid within each period. The investment benefit of earlier payments affect the rate that can be offered  # noqa: E501

        :return: The interest_payment_due of this BankingProductLendingRate.  # noqa: E501
        :rtype: str
        """
        return self._interest_payment_due

    @interest_payment_due.setter
    def interest_payment_due(self, interest_payment_due):
        """Sets the interest_payment_due of this BankingProductLendingRate.

        When loan payments are due to be paid within each period. The investment benefit of earlier payments affect the rate that can be offered  # noqa: E501

        :param interest_payment_due: The interest_payment_due of this BankingProductLendingRate.  # noqa: E501
        :type: str
        """
        allowed_values = ["IN_ARREARS", "IN_ADVANCE"]  # noqa: E501
        if interest_payment_due not in allowed_values:
            raise ValueError(
                "Invalid value for `interest_payment_due` ({0}), must be one of {1}"  # noqa: E501
                .format(interest_payment_due, allowed_values)
            )

        self._interest_payment_due = interest_payment_due

    @property
    def tiers(self):
        """Gets the tiers of this BankingProductLendingRate.  # noqa: E501

        Rate tiers applicable for this rate  # noqa: E501

        :return: The tiers of this BankingProductLendingRate.  # noqa: E501
        :rtype: list[BankingProductRateTier]
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """Sets the tiers of this BankingProductLendingRate.

        Rate tiers applicable for this rate  # noqa: E501

        :param tiers: The tiers of this BankingProductLendingRate.  # noqa: E501
        :type: list[BankingProductRateTier]
        """

        self._tiers = tiers

    @property
    def additional_value(self):
        """Gets the additional_value of this BankingProductLendingRate.  # noqa: E501

        Generic field containing additional information relevant to the [lendingRateType](#tocSproductlendingratetypedoc) specified. Whether mandatory or not is dependent on the value of [lendingRateType](#tocSproductlendingratetypedoc)  # noqa: E501

        :return: The additional_value of this BankingProductLendingRate.  # noqa: E501
        :rtype: str
        """
        return self._additional_value

    @additional_value.setter
    def additional_value(self, additional_value):
        """Sets the additional_value of this BankingProductLendingRate.

        Generic field containing additional information relevant to the [lendingRateType](#tocSproductlendingratetypedoc) specified. Whether mandatory or not is dependent on the value of [lendingRateType](#tocSproductlendingratetypedoc)  # noqa: E501

        :param additional_value: The additional_value of this BankingProductLendingRate.  # noqa: E501
        :type: str
        """

        self._additional_value = additional_value

    @property
    def additional_info(self):
        """Gets the additional_info of this BankingProductLendingRate.  # noqa: E501

        Display text providing more information on the rate.  # noqa: E501

        :return: The additional_info of this BankingProductLendingRate.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this BankingProductLendingRate.

        Display text providing more information on the rate.  # noqa: E501

        :param additional_info: The additional_info of this BankingProductLendingRate.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def additional_info_uri(self):
        """Gets the additional_info_uri of this BankingProductLendingRate.  # noqa: E501

        Link to a web page with more information on this rate  # noqa: E501

        :return: The additional_info_uri of this BankingProductLendingRate.  # noqa: E501
        :rtype: str
        """
        return self._additional_info_uri

    @additional_info_uri.setter
    def additional_info_uri(self, additional_info_uri):
        """Sets the additional_info_uri of this BankingProductLendingRate.

        Link to a web page with more information on this rate  # noqa: E501

        :param additional_info_uri: The additional_info_uri of this BankingProductLendingRate.  # noqa: E501
        :type: str
        """

        self._additional_info_uri = additional_info_uri

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
        if issubclass(BankingProductLendingRate, dict):
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
        if not isinstance(other, BankingProductLendingRate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
