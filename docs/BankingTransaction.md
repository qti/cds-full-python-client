# BankingTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ID of the account for which transactions are provided | 
**transaction_id** | **str** | A unique ID of the transaction adhering to the standards for ID permanence.  This is mandatory (through hashing if necessary) unless there are specific and justifiable technical reasons why a transaction cannot be uniquely identified for a particular account type | [optional] 
**is_detail_available** | **bool** | True if extended information is available using the transaction detail end point. False if extended data is not available | 
**type** | **str** | The type of the transaction | 
**status** | **str** | Status of the transaction whether pending or posted. Note that there is currently no provision in the standards to guarantee the ability to correlate a pending transaction with an associated posted transaction | 
**description** | **str** | The transaction description as applied by the financial institution | 
**posting_date_time** | **str** | The time the transaction was posted. This field is Mandatory if the transaction has status POSTED.  This is the time that appears on a standard statement | [optional] 
**value_date_time** | **str** | Date and time at which assets become available to the account owner in case of a credit entry, or cease to be available to the account owner in case of a debit transaction entry | [optional] 
**execution_date_time** | **str** | The time the transaction was executed by the originating customer, if available | [optional] 
**amount** | **str** | The value of the transaction. Negative values mean money was outgoing from the account | 
**currency** | **str** | The currency for the transaction amount. AUD assumed if not present | [optional] 
**reference** | **str** | The reference for the transaction provided by the originating institution. Empty string if no data provided | 
**merchant_name** | **str** | Name of the merchant for an outgoing payment to a merchant | [optional] 
**merchant_category_code** | **str** | The merchant category code (or MCC) for an outgoing payment to a merchant | [optional] 
**biller_code** | **str** | BPAY Biller Code for the transaction (if available) | [optional] 
**biller_name** | **str** | Name of the BPAY biller for the transaction (if available) | [optional] 
**crn** | **str** | BPAY CRN for the transaction (if available) | [optional] 
**apca_number** | **str** | 6 Digit APCA number for the initiating institution | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


