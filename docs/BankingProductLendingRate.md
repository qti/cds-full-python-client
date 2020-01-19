# BankingProductLendingRate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lending_rate_type** | **str** | The type of rate (fixed, variable, etc). See the next section for an overview of valid values and their meaning | 
**rate** | **str** | The rate to be applied | 
**comparison_rate** | **str** | A comparison rate equivalent for this rate | [optional] 
**calculation_frequency** | **str** | The period after which the rate is applied to the balance to calculate the amount due for the period. Calculation of the amount is often daily (as balances may change) but accumulated until the total amount is &#39;applied&#39; to the account (see applicationFrequency). Formatted according to [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations) (excludes recurrence syntax) | [optional] 
**application_frequency** | **str** | The period after which the calculated amount(s) (see calculationFrequency) are &#39;applied&#39; (i.e. debited or credited) to the account. Formatted according to [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations) (excludes recurrence syntax) | [optional] 
**interest_payment_due** | **str** | When loan payments are due to be paid within each period. The investment benefit of earlier payments affect the rate that can be offered | [optional] 
**tiers** | [**list[BankingProductRateTier]**](BankingProductRateTier.md) | Rate tiers applicable for this rate | [optional] 
**additional_value** | **str** | Generic field containing additional information relevant to the [lendingRateType](#tocSproductlendingratetypedoc) specified. Whether mandatory or not is dependent on the value of [lendingRateType](#tocSproductlendingratetypedoc) | [optional] 
**additional_info** | **str** | Display text providing more information on the rate. | [optional] 
**additional_info_uri** | **str** | Link to a web page with more information on this rate | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


