# GetBodyFatLogResponse

## Properties

| Name    | Type                                  | Description | Notes      |
| ------- | ------------------------------------- | ----------- | ---------- |
| **fat** | [**List[BodyFatLog]**](BodyFatLog.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_body_fat_log_response import GetBodyFatLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBodyFatLogResponse from a JSON string
get_body_fat_log_response_instance = GetBodyFatLogResponse.from_json(json)
# print the JSON string representation of the object
print(GetBodyFatLogResponse.to_json())

# convert the object into a dict
get_body_fat_log_response_dict = get_body_fat_log_response_instance.to_dict()
# create an instance of GetBodyFatLogResponse from a dict
get_body_fat_log_response_from_dict = GetBodyFatLogResponse.from_dict(get_body_fat_log_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
