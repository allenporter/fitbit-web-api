# GetTemperatureCoreSummaryResponse

## Properties

| Name          | Type                                                  | Description | Notes      |
| ------------- | ----------------------------------------------------- | ----------- | ---------- |
| **temp_core** | [**List[TemperatureCoreLog]**](TemperatureCoreLog.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_temperature_core_summary_response import GetTemperatureCoreSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTemperatureCoreSummaryResponse from a JSON string
get_temperature_core_summary_response_instance = GetTemperatureCoreSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(GetTemperatureCoreSummaryResponse.to_json())

# convert the object into a dict
get_temperature_core_summary_response_dict = get_temperature_core_summary_response_instance.to_dict()
# create an instance of GetTemperatureCoreSummaryResponse from a dict
get_temperature_core_summary_response_from_dict = GetTemperatureCoreSummaryResponse.from_dict(get_temperature_core_summary_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
