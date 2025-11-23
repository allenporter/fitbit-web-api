# BreathingRateValue

## Properties

| Name               | Type      | Description                                     | Notes      |
| ------------------ | --------- | ----------------------------------------------- | ---------- |
| **breathing_rate** | **float** | The average number of breaths taken per minute. | [optional] |

## Example

```python
from fitbit_web_api.models.breathing_rate_value import BreathingRateValue

# TODO update the JSON string below
json = "{}"
# create an instance of BreathingRateValue from a JSON string
breathing_rate_value_instance = BreathingRateValue.from_json(json)
# print the JSON string representation of the object
print(BreathingRateValue.to_json())

# convert the object into a dict
breathing_rate_value_dict = breathing_rate_value_instance.to_dict()
# create an instance of BreathingRateValue from a dict
breathing_rate_value_from_dict = BreathingRateValue.from_dict(breathing_rate_value_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
