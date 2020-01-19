# BankingTransactionDetailExtendedData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payer** | **str** | Label of the originating payer. Mandatory for inbound payment | [optional] 
**payee** | **str** | Label of the target PayID.  Mandatory for an outbound payment. The name assigned to the BSB/Account Number or PayID (by the owner of the PayID) | [optional] 
**extension_u_type** | **str** | Optional extended data provided specific to transaction originated via NPP | [optional] 
**x2p101_payload** | [**BankingTransactionDetailExtendedDataX2p101Payload**](BankingTransactionDetailExtendedDataX2p101Payload.md) |  | [optional] 
**service** | **str** | Identifier of the applicable overlay service. Valid values are: X2P1.01 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


