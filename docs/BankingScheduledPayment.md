# BankingScheduledPayment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduled_payment_id** | **str** | A unique ID of the scheduled payment adhering to the standards for ID permanence | 
**nickname** | **str** | The short display name of the payee as provided by the customer | [optional] 
**payer_reference** | **str** | The reference for the transaction that will be used by the originating institution for the purposes of constructing a statement narrative on the payer’s account. Empty string if no data provided | 
**payee_reference** | **str** | The reference for the transaction that will be provided by the originating institution. Empty string if no data provided | 
**status** | **str** | Indicates whether the schedule is currently active. The value SKIP is equivalent to ACTIVE except that the customer has requested the next normal occurrence to be skipped. | 
**_from** | [**BankingScheduledPaymentFrom**](BankingScheduledPaymentFrom.md) |  | 
**payment_set** | [**list[BankingScheduledPaymentSet]**](BankingScheduledPaymentSet.md) |  | 
**recurrence** | [**BankingScheduledPaymentRecurrence**](BankingScheduledPaymentRecurrence.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


