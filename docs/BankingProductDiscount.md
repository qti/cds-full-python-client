# BankingProductDiscount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the discount | 
**discount_type** | **str** | The type of discount. See the next section for an overview of valid values and their meaning | 
**amount** | **str** | Value of the discount. When following properties include one of amount, balanceRate, transactionRate, accruedRate and feeRate is mandatory | [optional] 
**balance_rate** | **str** | A discount rate calculated based on a proportion of the balance. Note that the currency of the fee discount is expected to be the same as the currency of the fee itself. One of amount, balanceRate, transactionRate, accruedRate and feeRate is mandatory. Unless noted in additionalInfo, assumes the application and calculation frequency are the same as the corresponding fee | [optional] 
**transaction_rate** | **str** | A discount rate calculated based on a proportion of a transaction. Note that the currency of the fee discount is expected to be the same as the currency of the fee itself. One of amount, balanceRate, transactionRate, accruedRate and feeRate is mandatory | [optional] 
**accrued_rate** | **str** | A discount rate calculated based on a proportion of the calculated interest accrued on the account. Note that the currency of the fee discount is expected to be the same as the currency of the fee itself. One of amount, balanceRate, transactionRate, accruedRate and feeRate is mandatory. Unless noted in additionalInfo, assumes the application and calculation frequency are the same as the corresponding fee | [optional] 
**fee_rate** | **str** | A discount rate calculated based on a proportion of the fee to which this discount is attached. Note that the currency of the fee discount is expected to be the same as the currency of the fee itself. One of amount, balanceRate, transactionRate, accruedRate and feeRate is mandatory. Unless noted in additionalInfo, assumes the application and calculation frequency are the same as the corresponding fee | [optional] 
**additional_value** | **str** | Generic field containing additional information relevant to the [discountType](#tocSproductdiscounttypedoc) specified. Whether mandatory or not is dependent on the value of [discountType](#tocSproductdiscounttypedoc) | [optional] 
**additional_info** | **str** | Display text providing more information on the discount | [optional] 
**additional_info_uri** | **str** | Link to a web page with more information on this discount | [optional] 
**eligibility** | [**list[BankingProductDiscountEligibility]**](BankingProductDiscountEligibility.md) | Eligibility constraints that apply to this discount | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


