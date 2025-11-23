# GetSpO2IntradayResponse

## Properties

| Name     | Type                                                                              | Description | Notes      |
| -------- | --------------------------------------------------------------------------------- | ----------- | ---------- |
| **spo2** | [**List[GetSpO2IntradayResponseSpo2Inner]**](GetSpO2IntradayResponseSpo2Inner.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_sp_o2_intraday_response import GetSpO2IntradayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSpO2IntradayResponse from a JSON string
get_sp_o2_intraday_response_instance = GetSpO2IntradayResponse.from_json(json)
# print the JSON string representation of the object
print(GetSpO2IntradayResponse.to_json())

# convert the object into a dict
get_sp_o2_intraday_response_dict = get_sp_o2_intraday_response_instance.to_dict()
# create an instance of GetSpO2IntradayResponse from a dict
get_sp_o2_intraday_response_from_dict = GetSpO2IntradayResponse.from_dict(get_sp_o2_intraday_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
