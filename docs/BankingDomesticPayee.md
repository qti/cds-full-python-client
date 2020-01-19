# BankingDomesticPayee

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_account_u_type** | **str** | Type of account object included. Valid values are: **account** A standard Australian account defined by BSB/Account Number. **card** A credit or charge card to pay to (note that PANs are masked). **payId** A PayID recognised by NPP | 
**account** | [**BankingDomesticPayeeAccount**](BankingDomesticPayeeAccount.md) |  | [optional] 
**card** | [**BankingDomesticPayeeCard**](BankingDomesticPayeeCard.md) |  | [optional] 
**pay_id** | [**BankingDomesticPayeePayId**](BankingDomesticPayeePayId.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


