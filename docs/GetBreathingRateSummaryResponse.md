# GetBreathingRateSummaryResponse

## Properties

| Name   | Type                                                      | Description | Notes      |
| ------ | --------------------------------------------------------- | ----------- | ---------- |
| **br** | [**List[BreathingRateSummary]**](BreathingRateSummary.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_breathing_rate_summary_response import GetBreathingRateSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBreathingRateSummaryResponse from a JSON string
get_breathing_rate_summary_response_instance = GetBreathingRateSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(GetBreathingRateSummaryResponse.to_json())

# convert the object into a dict
get_breathing_rate_summary_response_dict = get_breathing_rate_summary_response_instance.to_dict()
# create an instance of GetBreathingRateSummaryResponse from a dict
get_breathing_rate_summary_response_from_dict = GetBreathingRateSummaryResponse.from_dict(get_breathing_rate_summary_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
