# BankingScheduledPaymentTo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_u_type** | **str** | The type of object provided that specifies the destination of the funds for the payment. | 
**account_id** | **str** | Present if toUType is set to accountId. Indicates that the payment is to another account that is accessible under the current consent | [optional] 
**payee_id** | **str** | Present if toUType is set to payeeId. Indicates that the payment is to registered payee that can be accessed using the payee end point. If the Bank Payees scope has not been consented to then a payeeId should not be provided and the full payee details should be provided instead | [optional] 
**domestic** | [**BankingDomesticPayee**](BankingDomesticPayee.md) |  | [optional] 
**biller** | [**BankingBillerPayee**](BankingBillerPayee.md) |  | [optional] 
**international** | [**BankingInternationalPayee**](BankingInternationalPayee.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


