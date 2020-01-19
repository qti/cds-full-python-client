# BankingProductRateTier

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A display name for the tier | 
**unit_of_measure** | **str** | The unit of measure that applies to the tierValueMinimum and tierValueMaximum values e.g. a **DOLLAR** amount. **PERCENT** (in the case of loan-to-value ratio or LVR). Tier term period representing a discrete number of **MONTH**&#39;s or **DAY**&#39;s (in the case of term deposit tiers) | 
**minimum_value** | **float** | The number of tierUnitOfMeasure units that form the lower bound of the tier. The tier should be inclusive of this value | 
**maximum_value** | **float** | The number of tierUnitOfMeasure units that form the upper bound of the tier or band. For a tier with a discrete value (as opposed to a range of values e.g. 1 month) this must be the same as tierValueMinimum. Where this is the same as the tierValueMinimum value of the next-higher tier the referenced tier should be exclusive of this value. For example a term deposit of 2 months falls into the upper tier of the following tiers: (1 – 2 months, 2 – 3 months). If absent the tier&#39;s range has no upper bound. | [optional] 
**rate_application_method** | **str** | The method used to calculate the amount to be applied using one or more tiers. A single rate may be applied to the entire balance or each applicable tier rate is applied to the portion of the balance that falls into that tier (referred to as &#39;bands&#39; or &#39;steps&#39;) | [optional] 
**applicability_conditions** | [**BankingProductRateCondition**](BankingProductRateCondition.md) |  | [optional] 
**sub_tier** | [**BankingProductRateTierSubTier**](BankingProductRateTierSubTier.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


