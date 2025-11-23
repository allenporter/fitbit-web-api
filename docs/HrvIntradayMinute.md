# HrvIntradayMinute

## Properties

| Name       | Type                                        | Description                          | Notes      |
| ---------- | ------------------------------------------- | ------------------------------------ | ---------- |
| **minute** | **str**                                     | A measurement taken at a given time. | [optional] |
| **value**  | [**HrvIntradayValue**](HrvIntradayValue.md) |                                      | [optional] |

## Example

```python
from fitbit_web_api.models.hrv_intraday_minute import HrvIntradayMinute

# TODO update the JSON string below
json = "{}"
# create an instance of HrvIntradayMinute from a JSON string
hrv_intraday_minute_instance = HrvIntradayMinute.from_json(json)
# print the JSON string representation of the object
print(HrvIntradayMinute.to_json())

# convert the object into a dict
hrv_intraday_minute_dict = hrv_intraday_minute_instance.to_dict()
# create an instance of HrvIntradayMinute from a dict
hrv_intraday_minute_from_dict = HrvIntradayMinute.from_dict(hrv_intraday_minute_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
