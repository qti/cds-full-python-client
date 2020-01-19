# BankingInternationalPayeeBankDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | Country of the recipient institution. A valid [ISO 3166 Alpha-3](https://www.iso.org/iso-3166-country-codes.html) country code | 
**account_number** | **str** | Account Targeted for payment | 
**bank_address** | [**BankingInternationalPayeeBankDetailsBankAddress**](BankingInternationalPayeeBankDetailsBankAddress.md) |  | [optional] 
**beneficiary_bank_bic** | **str** | Swift bank code.  Aligns with standard [ISO 9362](https://www.iso.org/standard/60390.html) | [optional] 
**fed_wire_number** | **str** | Number for Fedwire payment (Federal Reserve Wire Network) | [optional] 
**sort_code** | **str** | Sort code used for account identification in some jurisdictions | [optional] 
**chip_number** | **str** | Number for the Clearing House Interbank Payments System | [optional] 
**routing_number** | **str** | International bank routing number | [optional] 
**legal_entity_identifier** | **str** | The legal entity identifier (LEI) for the beneficiary.  Aligns with [ISO 17442](https://www.iso.org/standard/59771.html) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


