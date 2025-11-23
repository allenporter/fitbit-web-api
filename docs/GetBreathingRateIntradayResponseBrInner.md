# GetBreathingRateIntradayResponseBrInner

## Properties

| Name          | Type                                                            | Description | Notes      |
| ------------- | --------------------------------------------------------------- | ----------- | ---------- |
| **date_time** | **date**                                                        |             | [optional] |
| **value**     | [**BreathingRateIntradayValue**](BreathingRateIntradayValue.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_breathing_rate_intraday_response_br_inner import GetBreathingRateIntradayResponseBrInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetBreathingRateIntradayResponseBrInner from a JSON string
get_breathing_rate_intraday_response_br_inner_instance = GetBreathingRateIntradayResponseBrInner.from_json(json)
# print the JSON string representation of the object
print(GetBreathingRateIntradayResponseBrInner.to_json())

# convert the object into a dict
get_breathing_rate_intraday_response_br_inner_dict = get_breathing_rate_intraday_response_br_inner_instance.to_dict()
# create an instance of GetBreathingRateIntradayResponseBrInner from a dict
get_breathing_rate_intraday_response_br_inner_from_dict = GetBreathingRateIntradayResponseBrInner.from_dict(get_breathing_rate_intraday_response_br_inner_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
