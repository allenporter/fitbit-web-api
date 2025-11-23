# GetTemperatureSkinSummaryResponse

## Properties

| Name          | Type                                                  | Description | Notes      |
| ------------- | ----------------------------------------------------- | ----------- | ---------- |
| **temp_skin** | [**List[TemperatureSkinLog]**](TemperatureSkinLog.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_temperature_skin_summary_response import GetTemperatureSkinSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTemperatureSkinSummaryResponse from a JSON string
get_temperature_skin_summary_response_instance = GetTemperatureSkinSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(GetTemperatureSkinSummaryResponse.to_json())

# convert the object into a dict
get_temperature_skin_summary_response_dict = get_temperature_skin_summary_response_instance.to_dict()
# create an instance of GetTemperatureSkinSummaryResponse from a dict
get_temperature_skin_summary_response_from_dict = GetTemperatureSkinSummaryResponse.from_dict(get_temperature_skin_summary_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
