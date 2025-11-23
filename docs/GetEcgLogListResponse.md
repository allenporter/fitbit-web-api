# GetEcgLogListResponse

## Properties

| Name             | Type                                                                      | Description           | Notes      |
| ---------------- | ------------------------------------------------------------------------- | --------------------- | ---------- |
| **ecg_readings** | [**List[EcgReading]**](EcgReading.md)                                     | List of ECG readings. | [optional] |
| **pagination**   | [**GetEcgLogListResponsePagination**](GetEcgLogListResponsePagination.md) |                       | [optional] |

## Example

```python
from fitbit_web_api.models.get_ecg_log_list_response import GetEcgLogListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEcgLogListResponse from a JSON string
get_ecg_log_list_response_instance = GetEcgLogListResponse.from_json(json)
# print the JSON string representation of the object
print(GetEcgLogListResponse.to_json())

# convert the object into a dict
get_ecg_log_list_response_dict = get_ecg_log_list_response_instance.to_dict()
# create an instance of GetEcgLogListResponse from a dict
get_ecg_log_list_response_from_dict = GetEcgLogListResponse.from_dict(get_ecg_log_list_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
