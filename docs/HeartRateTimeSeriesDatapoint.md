# HeartRateTimeSeriesDatapoint

## Properties

| Name          | Type                                                        | Description                 | Notes      |
| ------------- | ----------------------------------------------------------- | --------------------------- | ---------- |
| **date_time** | **date**                                                    | Date of the heart rate log. | [optional] |
| **value**     | [**HeartRateTimeSeriesValue**](HeartRateTimeSeriesValue.md) |                             | [optional] |

## Example

```python
from fitbit_web_api.models.heart_rate_time_series_datapoint import HeartRateTimeSeriesDatapoint

# TODO update the JSON string below
json = "{}"
# create an instance of HeartRateTimeSeriesDatapoint from a JSON string
heart_rate_time_series_datapoint_instance = HeartRateTimeSeriesDatapoint.from_json(json)
# print the JSON string representation of the object
print(HeartRateTimeSeriesDatapoint.to_json())

# convert the object into a dict
heart_rate_time_series_datapoint_dict = heart_rate_time_series_datapoint_instance.to_dict()
# create an instance of HeartRateTimeSeriesDatapoint from a dict
heart_rate_time_series_datapoint_from_dict = HeartRateTimeSeriesDatapoint.from_dict(heart_rate_time_series_datapoint_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
