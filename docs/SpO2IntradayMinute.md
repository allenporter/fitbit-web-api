# SpO2IntradayMinute

## Properties

| Name       | Type      | Description                                                                          | Notes      |
| ---------- | --------- | ------------------------------------------------------------------------------------ | ---------- |
| **minute** | **str**   | The date and time at which the SpO2 measurement was taken.                           | [optional] |
| **value**  | **float** | The percentage value of SpO2 calculated at a specific date and time in a single day. | [optional] |

## Example

```python
from fitbit_web_api.models.sp_o2_intraday_minute import SpO2IntradayMinute

# TODO update the JSON string below
json = "{}"
# create an instance of SpO2IntradayMinute from a JSON string
sp_o2_intraday_minute_instance = SpO2IntradayMinute.from_json(json)
# print the JSON string representation of the object
print(SpO2IntradayMinute.to_json())

# convert the object into a dict
sp_o2_intraday_minute_dict = sp_o2_intraday_minute_instance.to_dict()
# create an instance of SpO2IntradayMinute from a dict
sp_o2_intraday_minute_from_dict = SpO2IntradayMinute.from_dict(sp_o2_intraday_minute_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
