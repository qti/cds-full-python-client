# BankingBalance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | A unique ID of the account adhering to the standards for ID permanence | 
**current_balance** | **str** | The balance of the account at this time. Should align to the balance available via other channels such as Internet Banking. Assumed to be negative if the customer has money owing | 
**available_balance** | **str** | Balance representing the amount of funds available for transfer. Assumed to be zero or positive | 
**credit_limit** | **str** | Object representing the maximum amount of credit that is available for this account. Assumed to be zero if absent | [optional] 
**amortised_limit** | **str** | Object representing the available limit amortised according to payment schedule. Assumed to be zero if absent | [optional] 
**currency** | **str** | The currency for the balance amounts. If absent assumed to be AUD | [optional] 
**purses** | [**list[BankingBalancePurse]**](BankingBalancePurse.md) | Optional array of balances for the account in other currencies. Included to support accounts that support multi-currency purses such as Travel Cards | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


