# GetHeartRateIntradayResponse

## Properties

| Name                          | Type                                                                      | Description | Notes      |
| ----------------------------- | ------------------------------------------------------------------------- | ----------- | ---------- |
| **activities_heart**          | [**List[HeartRateTimeSeriesDatapoint]**](HeartRateTimeSeriesDatapoint.md) |             | [optional] |
| **activities_heart_intraday** | [**HeartRateIntradayDataset**](HeartRateIntradayDataset.md)               |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_heart_rate_intraday_response import GetHeartRateIntradayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetHeartRateIntradayResponse from a JSON string
get_heart_rate_intraday_response_instance = GetHeartRateIntradayResponse.from_json(json)
# print the JSON string representation of the object
print(GetHeartRateIntradayResponse.to_json())

# convert the object into a dict
get_heart_rate_intraday_response_dict = get_heart_rate_intraday_response_instance.to_dict()
# create an instance of GetHeartRateIntradayResponse from a dict
get_heart_rate_intraday_response_from_dict = GetHeartRateIntradayResponse.from_dict(get_heart_rate_intraday_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
