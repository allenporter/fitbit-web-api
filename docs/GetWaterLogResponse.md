# GetWaterLogResponse

## Properties

| Name        | Type                                                            | Description                | Notes      |
| ----------- | --------------------------------------------------------------- | -------------------------- | ---------- |
| **summary** | [**GetWaterLogResponseSummary**](GetWaterLogResponseSummary.md) |                            | [optional] |
| **water**   | [**List[WaterLog]**](WaterLog.md)                               | List of water log entries. | [optional] |

## Example

```python
from fitbit_web_api.models.get_water_log_response import GetWaterLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWaterLogResponse from a JSON string
get_water_log_response_instance = GetWaterLogResponse.from_json(json)
# print the JSON string representation of the object
print(GetWaterLogResponse.to_json())

# convert the object into a dict
get_water_log_response_dict = get_water_log_response_instance.to_dict()
# create an instance of GetWaterLogResponse from a dict
get_water_log_response_from_dict = GetWaterLogResponse.from_dict(get_water_log_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
