# BreathingRateIntradayValue

## Properties

| Name                    | Type                                                                | Description | Notes      |
| ----------------------- | ------------------------------------------------------------------- | ----------- | ---------- |
| **light_sleep_summary** | [**BreathingRateIntradaySummary**](BreathingRateIntradaySummary.md) |             | [optional] |
| **deep_sleep_summary**  | [**BreathingRateIntradaySummary**](BreathingRateIntradaySummary.md) |             | [optional] |
| **rem_sleep_summary**   | [**BreathingRateIntradaySummary**](BreathingRateIntradaySummary.md) |             | [optional] |
| **full_sleep_summary**  | [**BreathingRateIntradaySummary**](BreathingRateIntradaySummary.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.breathing_rate_intraday_value import BreathingRateIntradayValue

# TODO update the JSON string below
json = "{}"
# create an instance of BreathingRateIntradayValue from a JSON string
breathing_rate_intraday_value_instance = BreathingRateIntradayValue.from_json(json)
# print the JSON string representation of the object
print(BreathingRateIntradayValue.to_json())

# convert the object into a dict
breathing_rate_intraday_value_dict = breathing_rate_intraday_value_instance.to_dict()
# create an instance of BreathingRateIntradayValue from a dict
breathing_rate_intraday_value_from_dict = BreathingRateIntradayValue.from_dict(breathing_rate_intraday_value_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
