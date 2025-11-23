# GetHrvIntradayResponseHrvInner

## Properties

| Name          | Type                                                | Description | Notes      |
| ------------- | --------------------------------------------------- | ----------- | ---------- |
| **date_time** | **date**                                            |             | [optional] |
| **minutes**   | [**List[HrvIntradayMinute]**](HrvIntradayMinute.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_hrv_intraday_response_hrv_inner import GetHrvIntradayResponseHrvInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetHrvIntradayResponseHrvInner from a JSON string
get_hrv_intraday_response_hrv_inner_instance = GetHrvIntradayResponseHrvInner.from_json(json)
# print the JSON string representation of the object
print(GetHrvIntradayResponseHrvInner.to_json())

# convert the object into a dict
get_hrv_intraday_response_hrv_inner_dict = get_hrv_intraday_response_hrv_inner_instance.to_dict()
# create an instance of GetHrvIntradayResponseHrvInner from a dict
get_hrv_intraday_response_hrv_inner_from_dict = GetHrvIntradayResponseHrvInner.from_dict(get_hrv_intraday_response_hrv_inner_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
