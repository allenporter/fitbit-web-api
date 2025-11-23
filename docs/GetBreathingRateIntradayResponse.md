# GetBreathingRateIntradayResponse

## Properties

| Name   | Type                                                                                            | Description | Notes      |
| ------ | ----------------------------------------------------------------------------------------------- | ----------- | ---------- |
| **br** | [**List[GetBreathingRateIntradayResponseBrInner]**](GetBreathingRateIntradayResponseBrInner.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_breathing_rate_intraday_response import GetBreathingRateIntradayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBreathingRateIntradayResponse from a JSON string
get_breathing_rate_intraday_response_instance = GetBreathingRateIntradayResponse.from_json(json)
# print the JSON string representation of the object
print(GetBreathingRateIntradayResponse.to_json())

# convert the object into a dict
get_breathing_rate_intraday_response_dict = get_breathing_rate_intraday_response_instance.to_dict()
# create an instance of GetBreathingRateIntradayResponse from a dict
get_breathing_rate_intraday_response_from_dict = GetBreathingRateIntradayResponse.from_dict(get_breathing_rate_intraday_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
