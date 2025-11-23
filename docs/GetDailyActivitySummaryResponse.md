# GetDailyActivitySummaryResponse

## Properties

| Name           | Type                                      | Description                   | Notes      |
| -------------- | ----------------------------------------- | ----------------------------- | ---------- |
| **activities** | [**List[ActivityLog]**](ActivityLog.md)   | List of activity log entries. | [optional] |
| **goals**      | [**ActivityGoals**](ActivityGoals.md)     |                               | [optional] |
| **summary**    | [**ActivitySummary**](ActivitySummary.md) |                               | [optional] |

## Example

```python
from fitbit_web_api.models.get_daily_activity_summary_response import GetDailyActivitySummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDailyActivitySummaryResponse from a JSON string
get_daily_activity_summary_response_instance = GetDailyActivitySummaryResponse.from_json(json)
# print the JSON string representation of the object
print(GetDailyActivitySummaryResponse.to_json())

# convert the object into a dict
get_daily_activity_summary_response_dict = get_daily_activity_summary_response_instance.to_dict()
# create an instance of GetDailyActivitySummaryResponse from a dict
get_daily_activity_summary_response_from_dict = GetDailyActivitySummaryResponse.from_dict(get_daily_activity_summary_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
