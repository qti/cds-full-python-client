# BankingScheduledPaymentSet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | [**BankingScheduledPaymentTo**](BankingScheduledPaymentTo.md) |  | 
**is_amount_calculated** | **bool** | Flag indicating whether the amount of the payment is calculated based on the context of the event. For instance a payment to reduce the balance of a credit card to zero. If absent then false is assumed | [optional] 
**amount** | **str** | The amount of the next payment if known. Mandatory unless the isAmountCalculated field is set to true. Must be zero or positive if present | [optional] 
**currency** | **str** | The currency for the payment. AUD assumed if not present | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


