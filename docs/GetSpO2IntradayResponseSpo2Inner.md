# GetSpO2IntradayResponseSpo2Inner

## Properties

| Name          | Type                                                  | Description                                            | Notes      |
| ------------- | ----------------------------------------------------- | ------------------------------------------------------ | ---------- |
| **date_time** | **date**                                              | The sleep log date specified in the format YYYY-MM-DD. | [optional] |
| **minutes**   | [**List[SpO2IntradayMinute]**](SpO2IntradayMinute.md) |                                                        | [optional] |

## Example

```python
from fitbit_web_api.models.get_sp_o2_intraday_response_spo2_inner import GetSpO2IntradayResponseSpo2Inner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSpO2IntradayResponseSpo2Inner from a JSON string
get_sp_o2_intraday_response_spo2_inner_instance = GetSpO2IntradayResponseSpo2Inner.from_json(json)
# print the JSON string representation of the object
print(GetSpO2IntradayResponseSpo2Inner.to_json())

# convert the object into a dict
get_sp_o2_intraday_response_spo2_inner_dict = get_sp_o2_intraday_response_spo2_inner_instance.to_dict()
# create an instance of GetSpO2IntradayResponseSpo2Inner from a dict
get_sp_o2_intraday_response_spo2_inner_from_dict = GetSpO2IntradayResponseSpo2Inner.from_dict(get_sp_o2_intraday_response_spo2_inner_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
