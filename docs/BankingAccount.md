# BankingAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | A unique ID of the account adhering to the standards for ID permanence | 
**creation_date** | **str** | Date that the account was created (if known) | [optional] 
**display_name** | **str** | The display name of the account as defined by the bank. This should not incorporate account numbers or PANs. If it does the values should be masked according to the rules of the MaskedAccountString common type. | 
**nickname** | **str** | A customer supplied nick name for the account | [optional] 
**open_status** | **str** | Open or closed status for the account. If not present then OPEN is assumed | [optional] [default to 'OPEN']
**is_owned** | **bool** | Flag indicating that the customer associated with the authorisation is an owner of the account. Does not indicate sole ownership, however. If not present then &#39;true&#39; is assumed | [optional] [default to True]
**masked_number** | **str** | A masked version of the account. Whether BSB/Account Number, Credit Card PAN or another number | 
**product_category** | [**BankingProductCategory**](BankingProductCategory.md) |  | 
**product_name** | **str** | The unique identifier of the account as defined by the data holder (akin to model number for the account) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


