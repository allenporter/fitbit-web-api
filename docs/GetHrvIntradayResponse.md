# GetHrvIntradayResponse

## Properties

| Name    | Type                                                                          | Description | Notes      |
| ------- | ----------------------------------------------------------------------------- | ----------- | ---------- |
| **hrv** | [**List[GetHrvIntradayResponseHrvInner]**](GetHrvIntradayResponseHrvInner.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_hrv_intraday_response import GetHrvIntradayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetHrvIntradayResponse from a JSON string
get_hrv_intraday_response_instance = GetHrvIntradayResponse.from_json(json)
# print the JSON string representation of the object
print(GetHrvIntradayResponse.to_json())

# convert the object into a dict
get_hrv_intraday_response_dict = get_hrv_intraday_response_instance.to_dict()
# create an instance of GetHrvIntradayResponse from a dict
get_hrv_intraday_response_from_dict = GetHrvIntradayResponse.from_dict(get_hrv_intraday_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
