# GetActivityLogListResponse

## Properties

| Name           | Type                                                                                | Description                   | Notes      |
| -------------- | ----------------------------------------------------------------------------------- | ----------------------------- | ---------- |
| **activities** | [**List[ActivityLog]**](ActivityLog.md)                                             | List of activity log entries. | [optional] |
| **pagination** | [**GetActivityLogListResponsePagination**](GetActivityLogListResponsePagination.md) |                               | [optional] |

## Example

```python
from fitbit_web_api.models.get_activity_log_list_response import GetActivityLogListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetActivityLogListResponse from a JSON string
get_activity_log_list_response_instance = GetActivityLogListResponse.from_json(json)
# print the JSON string representation of the object
print(GetActivityLogListResponse.to_json())

# convert the object into a dict
get_activity_log_list_response_dict = get_activity_log_list_response_instance.to_dict()
# create an instance of GetActivityLogListResponse from a dict
get_activity_log_list_response_from_dict = GetActivityLogListResponse.from_dict(get_activity_log_list_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
