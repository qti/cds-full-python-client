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


class BankingProductRateTier(object):
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
        'unit_of_measure': 'str',
        'minimum_value': 'float',
        'maximum_value': 'float',
        'rate_application_method': 'str',
        'applicability_conditions': 'BankingProductRateCondition',
        'sub_tier': 'BankingProductRateTierSubTier'
    }

    attribute_map = {
        'name': 'name',
        'unit_of_measure': 'unitOfMeasure',
        'minimum_value': 'minimumValue',
        'maximum_value': 'maximumValue',
        'rate_application_method': 'rateApplicationMethod',
        'applicability_conditions': 'applicabilityConditions',
        'sub_tier': 'subTier'
    }

    def __init__(self, name=None, unit_of_measure=None, minimum_value=None, maximum_value=None, rate_application_method=None, applicability_conditions=None, sub_tier=None):  # noqa: E501
        """BankingProductRateTier - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._unit_of_measure = None
        self._minimum_value = None
        self._maximum_value = None
        self._rate_application_method = None
        self._applicability_conditions = None
        self._sub_tier = None
        self.discriminator = None

        self.name = name
        self.unit_of_measure = unit_of_measure
        self.minimum_value = minimum_value
        if maximum_value is not None:
            self.maximum_value = maximum_value
        if rate_application_method is not None:
            self.rate_application_method = rate_application_method
        if applicability_conditions is not None:
            self.applicability_conditions = applicability_conditions
        if sub_tier is not None:
            self.sub_tier = sub_tier

    @property
    def name(self):
        """Gets the name of this BankingProductRateTier.  # noqa: E501

        A display name for the tier  # noqa: E501

        :return: The name of this BankingProductRateTier.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BankingProductRateTier.

        A display name for the tier  # noqa: E501

        :param name: The name of this BankingProductRateTier.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def unit_of_measure(self):
        """Gets the unit_of_measure of this BankingProductRateTier.  # noqa: E501

        The unit of measure that applies to the tierValueMinimum and tierValueMaximum values e.g. a **DOLLAR** amount. **PERCENT** (in the case of loan-to-value ratio or LVR). Tier term period representing a discrete number of **MONTH**'s or **DAY**'s (in the case of term deposit tiers)  # noqa: E501

        :return: The unit_of_measure of this BankingProductRateTier.  # noqa: E501
        :rtype: str
        """
        return self._unit_of_measure

    @unit_of_measure.setter
    def unit_of_measure(self, unit_of_measure):
        """Sets the unit_of_measure of this BankingProductRateTier.

        The unit of measure that applies to the tierValueMinimum and tierValueMaximum values e.g. a **DOLLAR** amount. **PERCENT** (in the case of loan-to-value ratio or LVR). Tier term period representing a discrete number of **MONTH**'s or **DAY**'s (in the case of term deposit tiers)  # noqa: E501

        :param unit_of_measure: The unit_of_measure of this BankingProductRateTier.  # noqa: E501
        :type: str
        """
        if unit_of_measure is None:
            raise ValueError("Invalid value for `unit_of_measure`, must not be `None`")  # noqa: E501
        allowed_values = ["DOLLAR", "PERCENT", "MONTH", "DAY"]  # noqa: E501
        if unit_of_measure not in allowed_values:
            raise ValueError(
                "Invalid value for `unit_of_measure` ({0}), must be one of {1}"  # noqa: E501
                .format(unit_of_measure, allowed_values)
            )

        self._unit_of_measure = unit_of_measure

    @property
    def minimum_value(self):
        """Gets the minimum_value of this BankingProductRateTier.  # noqa: E501

        The number of tierUnitOfMeasure units that form the lower bound of the tier. The tier should be inclusive of this value  # noqa: E501

        :return: The minimum_value of this BankingProductRateTier.  # noqa: E501
        :rtype: float
        """
        return self._minimum_value

    @minimum_value.setter
    def minimum_value(self, minimum_value):
        """Sets the minimum_value of this BankingProductRateTier.

        The number of tierUnitOfMeasure units that form the lower bound of the tier. The tier should be inclusive of this value  # noqa: E501

        :param minimum_value: The minimum_value of this BankingProductRateTier.  # noqa: E501
        :type: float
        """
        if minimum_value is None:
            raise ValueError("Invalid value for `minimum_value`, must not be `None`")  # noqa: E501

        self._minimum_value = minimum_value

    @property
    def maximum_value(self):
        """Gets the maximum_value of this BankingProductRateTier.  # noqa: E501

        The number of tierUnitOfMeasure units that form the upper bound of the tier or band. For a tier with a discrete value (as opposed to a range of values e.g. 1 month) this must be the same as tierValueMinimum. Where this is the same as the tierValueMinimum value of the next-higher tier the referenced tier should be exclusive of this value. For example a term deposit of 2 months falls into the upper tier of the following tiers: (1 – 2 months, 2 – 3 months). If absent the tier's range has no upper bound.  # noqa: E501

        :return: The maximum_value of this BankingProductRateTier.  # noqa: E501
        :rtype: float
        """
        return self._maximum_value

    @maximum_value.setter
    def maximum_value(self, maximum_value):
        """Sets the maximum_value of this BankingProductRateTier.

        The number of tierUnitOfMeasure units that form the upper bound of the tier or band. For a tier with a discrete value (as opposed to a range of values e.g. 1 month) this must be the same as tierValueMinimum. Where this is the same as the tierValueMinimum value of the next-higher tier the referenced tier should be exclusive of this value. For example a term deposit of 2 months falls into the upper tier of the following tiers: (1 – 2 months, 2 – 3 months). If absent the tier's range has no upper bound.  # noqa: E501

        :param maximum_value: The maximum_value of this BankingProductRateTier.  # noqa: E501
        :type: float
        """

        self._maximum_value = maximum_value

    @property
    def rate_application_method(self):
        """Gets the rate_application_method of this BankingProductRateTier.  # noqa: E501

        The method used to calculate the amount to be applied using one or more tiers. A single rate may be applied to the entire balance or each applicable tier rate is applied to the portion of the balance that falls into that tier (referred to as 'bands' or 'steps')  # noqa: E501

        :return: The rate_application_method of this BankingProductRateTier.  # noqa: E501
        :rtype: str
        """
        return self._rate_application_method

    @rate_application_method.setter
    def rate_application_method(self, rate_application_method):
        """Sets the rate_application_method of this BankingProductRateTier.

        The method used to calculate the amount to be applied using one or more tiers. A single rate may be applied to the entire balance or each applicable tier rate is applied to the portion of the balance that falls into that tier (referred to as 'bands' or 'steps')  # noqa: E501

        :param rate_application_method: The rate_application_method of this BankingProductRateTier.  # noqa: E501
        :type: str
        """
        allowed_values = ["WHOLE_BALANCE", "PER_TIER"]  # noqa: E501
        if rate_application_method not in allowed_values:
            raise ValueError(
                "Invalid value for `rate_application_method` ({0}), must be one of {1}"  # noqa: E501
                .format(rate_application_method, allowed_values)
            )

        self._rate_application_method = rate_application_method

    @property
    def applicability_conditions(self):
        """Gets the applicability_conditions of this BankingProductRateTier.  # noqa: E501


        :return: The applicability_conditions of this BankingProductRateTier.  # noqa: E501
        :rtype: BankingProductRateCondition
        """
        return self._applicability_conditions

    @applicability_conditions.setter
    def applicability_conditions(self, applicability_conditions):
        """Sets the applicability_conditions of this BankingProductRateTier.


        :param applicability_conditions: The applicability_conditions of this BankingProductRateTier.  # noqa: E501
        :type: BankingProductRateCondition
        """

        self._applicability_conditions = applicability_conditions

    @property
    def sub_tier(self):
        """Gets the sub_tier of this BankingProductRateTier.  # noqa: E501


        :return: The sub_tier of this BankingProductRateTier.  # noqa: E501
        :rtype: BankingProductRateTierSubTier
        """
        return self._sub_tier

    @sub_tier.setter
    def sub_tier(self, sub_tier):
        """Sets the sub_tier of this BankingProductRateTier.


        :param sub_tier: The sub_tier of this BankingProductRateTier.  # noqa: E501
        :type: BankingProductRateTierSubTier
        """

        self._sub_tier = sub_tier

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
        if issubclass(BankingProductRateTier, dict):
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
        if not isinstance(other, BankingProductRateTier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
