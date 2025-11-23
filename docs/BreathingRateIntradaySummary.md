# BreathingRateIntradaySummary

## Properties

| Name               | Type      | Description                                 | Notes      |
| ------------------ | --------- | ------------------------------------------- | ---------- |
| **breathing_rate** | **float** | Average number of breaths taken per minute. | [optional] |

## Example

```python
from fitbit_web_api.models.breathing_rate_intraday_summary import BreathingRateIntradaySummary

# TODO update the JSON string below
json = "{}"
# create an instance of BreathingRateIntradaySummary from a JSON string
breathing_rate_intraday_summary_instance = BreathingRateIntradaySummary.from_json(json)
# print the JSON string representation of the object
print(BreathingRateIntradaySummary.to_json())

# convert the object into a dict
breathing_rate_intraday_summary_dict = breathing_rate_intraday_summary_instance.to_dict()
# create an instance of BreathingRateIntradaySummary from a dict
breathing_rate_intraday_summary_from_dict = BreathingRateIntradaySummary.from_dict(breathing_rate_intraday_summary_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
