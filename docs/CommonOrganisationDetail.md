# CommonOrganisationDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_update_time** | **str** | The date and time that this record was last updated by the customer. If no update has occurred then this date should reflect the initial creation date for the data | [optional] 
**agent_first_name** | **str** | The first name of the individual providing access on behalf of the organisation. For people with single names this field need not be present.  The single name should be in the lastName field | [optional] 
**agent_last_name** | **str** | The last name of the individual providing access on behalf of the organisation. For people with single names the single name should be in this field | 
**agent_role** | **str** | The role of the individual identified as the agent who is providing authorisation.  Expected to be used for display. Default to Unspecified if the role is not known | 
**business_name** | **str** | Name of the organisation | 
**legal_name** | **str** | Legal name, if different to the business name | [optional] 
**short_name** | **str** | Short name used for communication, if different to the business name | [optional] 
**abn** | **str** | Australian Business Number for the organisation | [optional] 
**acn** | **str** | Australian Company Number for the organisation. Required only if an ACN is applicable for the organisation type | [optional] 
**is_acnc_registered** | **bool** | True if registered with the ACNC.  False if not. Absent or null if not confirmed. | [optional] 
**industry_code** | **str** | [ANZSIC (2006)](http://www.abs.gov.au/anzsic) code for the organisation. | [optional] 
**organisation_type** | **str** | Legal organisation type | 
**registered_country** | **str** | Enumeration with values from [ISO 3166 Alpha-3](https://www.iso.org/iso-3166-country-codes.html) country codes.  Assumed to be AUS if absent | [optional] 
**establishment_date** | **str** | The date the organisation described was established | [optional] 
**physical_addresses** | [**list[CommonPhysicalAddressWithPurpose]**](CommonPhysicalAddressWithPurpose.md) | Must contain at least one address. One and only one address may have the purpose of REGISTERED. Zero or one, and no more than one, record may have the purpose of MAIL. If zero then the REGISTERED address is to be used for mail | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


