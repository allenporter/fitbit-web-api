# GetAzmTimeSeriesResponse

## Properties

| Name                               | Type                                                          | Description | Notes      |
| ---------------------------------- | ------------------------------------------------------------- | ----------- | ---------- |
| **activities_active_zone_minutes** | [**List[AzmTimeSeriesDatapoint]**](AzmTimeSeriesDatapoint.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_azm_time_series_response import GetAzmTimeSeriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAzmTimeSeriesResponse from a JSON string
get_azm_time_series_response_instance = GetAzmTimeSeriesResponse.from_json(json)
# print the JSON string representation of the object
print(GetAzmTimeSeriesResponse.to_json())

# convert the object into a dict
get_azm_time_series_response_dict = get_azm_time_series_response_instance.to_dict()
# create an instance of GetAzmTimeSeriesResponse from a dict
get_azm_time_series_response_from_dict = GetAzmTimeSeriesResponse.from_dict(get_azm_time_series_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
