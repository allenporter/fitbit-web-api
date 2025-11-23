# BreathingRateSummary

## Properties

| Name          | Type                                            | Description                                            | Notes      |
| ------------- | ----------------------------------------------- | ------------------------------------------------------ | ---------- |
| **date_time** | **date**                                        | The sleep log date specified in the format YYYY-MM-DD. | [optional] |
| **value**     | [**BreathingRateValue**](BreathingRateValue.md) |                                                        | [optional] |

## Example

```python
from fitbit_web_api.models.breathing_rate_summary import BreathingRateSummary

# TODO update the JSON string below
json = "{}"
# create an instance of BreathingRateSummary from a JSON string
breathing_rate_summary_instance = BreathingRateSummary.from_json(json)
# print the JSON string representation of the object
print(BreathingRateSummary.to_json())

# convert the object into a dict
breathing_rate_summary_dict = breathing_rate_summary_instance.to_dict()
# create an instance of BreathingRateSummary from a dict
breathing_rate_summary_from_dict = BreathingRateSummary.from_dict(breathing_rate_summary_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
