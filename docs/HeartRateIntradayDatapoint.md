# HeartRateIntradayDatapoint

## Properties

| Name      | Type      | Description                                         | Notes      |
| --------- | --------- | --------------------------------------------------- | ---------- |
| **time**  | **str**   | The time the intraday heart rate value was recorded | [optional] |
| **value** | **float** | The intraday heart rate value                       | [optional] |

## Example

```python
from fitbit_web_api.models.heart_rate_intraday_datapoint import HeartRateIntradayDatapoint

# TODO update the JSON string below
json = "{}"
# create an instance of HeartRateIntradayDatapoint from a JSON string
heart_rate_intraday_datapoint_instance = HeartRateIntradayDatapoint.from_json(json)
# print the JSON string representation of the object
print(HeartRateIntradayDatapoint.to_json())

# convert the object into a dict
heart_rate_intraday_datapoint_dict = heart_rate_intraday_datapoint_instance.to_dict()
# create an instance of HeartRateIntradayDatapoint from a dict
heart_rate_intraday_datapoint_from_dict = HeartRateIntradayDatapoint.from_dict(heart_rate_intraday_datapoint_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
