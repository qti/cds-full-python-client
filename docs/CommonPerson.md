# CommonPerson

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_update_time** | **str** | The date and time that this record was last updated by the customer.  If no update has occurred then this date should reflect the initial creation date for the data | [optional] 
**first_name** | **str** | For people with single names this field need not be present.  The single name should be in the lastName field | [optional] 
**last_name** | **str** | For people with single names the single name should be in this field | 
**middle_names** | **list[str]** | Field is mandatory but array may be empty | 
**prefix** | **str** | Also known as title or salutation.  The prefix to the name (e.g. Mr, Mrs, Ms, Miss, Sir, etc) | [optional] 
**suffix** | **str** | Used for a trailing suffix to the name (e.g. Jr) | [optional] 
**occupation_code** | **str** | Value is a valid [ANZSCO v1.2](http://www.abs.gov.au/ANZSCO) Standard Occupation classification. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


