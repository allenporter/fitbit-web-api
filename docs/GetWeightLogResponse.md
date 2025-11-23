# GetWeightLogResponse

## Properties

| Name       | Type                                | Description | Notes      |
| ---------- | ----------------------------------- | ----------- | ---------- |
| **weight** | [**List[WeightLog]**](WeightLog.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_weight_log_response import GetWeightLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWeightLogResponse from a JSON string
get_weight_log_response_instance = GetWeightLogResponse.from_json(json)
# print the JSON string representation of the object
print(GetWeightLogResponse.to_json())

# convert the object into a dict
get_weight_log_response_dict = get_weight_log_response_instance.to_dict()
# create an instance of GetWeightLogResponse from a dict
get_weight_log_response_from_dict = GetWeightLogResponse.from_dict(get_weight_log_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
