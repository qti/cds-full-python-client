# BankingScheduledPaymentRecurrenceLastWeekday

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**final_payment_date** | **str** | The limit date after which no more payments should be made using this schedule. If both finalPaymentDate and paymentsRemaining are present then payments will stop according to the most constraining value. If neither field is present the payments will continue indefinitely | [optional] 
**payments_remaining** | **int** | Indicates the number of payments remaining in the schedule. If both finalPaymentDate and paymentsRemaining are present then payments will stop according to the most constraining value. If neither field is present the payments will continue indefinitely | [optional] 
**interval** | **str** | The interval for the payment. Formatted according to [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations) (excludes recurrence syntax) with components less than a day in length ignored. This duration defines the period between payments starting with nextPaymentDate | 
**last_week_day** | **str** | The weekDay specified. The payment will occur on the last occurrence of this weekday in the interval. | 
**non_business_day_treatment** | **str** | Enumerated field giving the treatment where a scheduled payment date is not a business day. If absent assumed to be ON.&lt;br/&gt;**AFTER** - If a scheduled payment date is a non-business day the payment will be made on the first business day after the scheduled payment date.&lt;br/&gt;**BEFORE** - If a scheduled payment date is a non-business day the payment will be made on the first business day before the scheduled payment date.&lt;br/&gt;**ON** - If a scheduled payment date is a non-business day the payment will be made on that day regardless.&lt;br/&gt;**ONLY** - Payments only occur on business days. If a scheduled payment date is a non-business day the payment will be ignored | [optional] [default to 'ON']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


