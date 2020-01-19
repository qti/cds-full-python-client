# ResponseCommonDiscoveryStatusData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Enumeration with values. OK (implementation is fully functional). PARTIAL_FAILURE (one or more end points are unexpectedly unavailable). UNAVAILABLE (the full implementation is unexpectedly unavailable). SCHEDULED_OUTAGE (an advertised outage is in effect) | 
**explanation** | **str** | Provides an explanation of the current outage that can be displayed to an end customer. Mandatory if the status property is any value other than OK | [optional] 
**detection_time** | **str** | The date and time that the current outage was detected. Should only be present if the status property is PARTIAL_FAILURE or UNAVAILABLE | [optional] 
**expected_resolution_time** | **str** | The date and time that full service is expected to resume (if known). Should not be present if the status property has a value of OK. | [optional] 
**update_time** | **str** | The date and time that this status was last updated by the Data Holder. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


