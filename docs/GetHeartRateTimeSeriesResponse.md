# GetHeartRateTimeSeriesResponse

## Properties

| Name                 | Type                                                                      | Description | Notes      |
| -------------------- | ------------------------------------------------------------------------- | ----------- | ---------- |
| **activities_heart** | [**List[HeartRateTimeSeriesDatapoint]**](HeartRateTimeSeriesDatapoint.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_heart_rate_time_series_response import GetHeartRateTimeSeriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetHeartRateTimeSeriesResponse from a JSON string
get_heart_rate_time_series_response_instance = GetHeartRateTimeSeriesResponse.from_json(json)
# print the JSON string representation of the object
print(GetHeartRateTimeSeriesResponse.to_json())

# convert the object into a dict
get_heart_rate_time_series_response_dict = get_heart_rate_time_series_response_instance.to_dict()
# create an instance of GetHeartRateTimeSeriesResponse from a dict
get_heart_rate_time_series_response_from_dict = GetHeartRateTimeSeriesResponse.from_dict(get_heart_rate_time_series_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
