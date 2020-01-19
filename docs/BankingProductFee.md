# BankingProductFee

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the fee | 
**fee_type** | **str** | The type of fee | 
**amount** | **str** | The amount charged for the fee. One of amount, balanceRate, transactionRate and accruedRate is mandatory | [optional] 
**balance_rate** | **str** | A fee rate calculated based on a proportion of the balance. One of amount, balanceRate, transactionRate and accruedRate is mandatory | [optional] 
**transaction_rate** | **str** | A fee rate calculated based on a proportion of a transaction. One of amount, balanceRate, transactionRate and accruedRate is mandatory | [optional] 
**accrued_rate** | **str** | A fee rate calculated based on a proportion of the calculated interest accrued on the account. One of amount, balanceRate, transactionRate and accruedRate is mandatory | [optional] 
**accrual_frequency** | **str** | The indicative frequency with which the fee is calculated on the account. Only applies if balanceRate or accruedRate is also present. Formatted according to [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations) (excludes recurrence syntax) | [optional] 
**currency** | **str** | The currency the fee will be charged in. Assumes AUD if absent | [optional] 
**additional_value** | **str** | Generic field containing additional information relevant to the [feeType](#tocSproductfeetypedoc) specified. Whether mandatory or not is dependent on the value of [feeType](#tocSproductfeetypedoc) | [optional] 
**additional_info** | **str** | Display text providing more information on the fee | [optional] 
**additional_info_uri** | **str** | Link to a web page with more information on this fee | [optional] 
**discounts** | [**list[BankingProductDiscount]**](BankingProductDiscount.md) | An optional list of discounts to this fee that may be available | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


