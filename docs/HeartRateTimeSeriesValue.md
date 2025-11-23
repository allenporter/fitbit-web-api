# HeartRateTimeSeriesValue

## Properties

| Name                        | Type                                        | Description                               | Notes      |
| --------------------------- | ------------------------------------------- | ----------------------------------------- | ---------- |
| **custom_heart_rate_zones** | [**List[HeartRateZone]**](HeartRateZone.md) |                                           | [optional] |
| **heart_rate_zones**        | [**List[HeartRateZone]**](HeartRateZone.md) |                                           | [optional] |
| **resting_heart_rate**      | **int**                                     | The user’s calculated resting heart rate. | [optional] |

## Example

```python
from fitbit_web_api.models.heart_rate_time_series_value import HeartRateTimeSeriesValue

# TODO update the JSON string below
json = "{}"
# create an instance of HeartRateTimeSeriesValue from a JSON string
heart_rate_time_series_value_instance = HeartRateTimeSeriesValue.from_json(json)
# print the JSON string representation of the object
print(HeartRateTimeSeriesValue.to_json())

# convert the object into a dict
heart_rate_time_series_value_dict = heart_rate_time_series_value_instance.to_dict()
# create an instance of HeartRateTimeSeriesValue from a dict
heart_rate_time_series_value_from_dict = HeartRateTimeSeriesValue.from_dict(heart_rate_time_series_value_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
