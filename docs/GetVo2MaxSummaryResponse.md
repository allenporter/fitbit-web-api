# GetVo2MaxSummaryResponse

## Properties

| Name            | Type                                                  | Description | Notes      |
| --------------- | ----------------------------------------------------- | ----------- | ---------- |
| **cardioscore** | [**List[CardioScoreSummary]**](CardioScoreSummary.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_vo2_max_summary_response import GetVo2MaxSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetVo2MaxSummaryResponse from a JSON string
get_vo2_max_summary_response_instance = GetVo2MaxSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(GetVo2MaxSummaryResponse.to_json())

# convert the object into a dict
get_vo2_max_summary_response_dict = get_vo2_max_summary_response_instance.to_dict()
# create an instance of GetVo2MaxSummaryResponse from a dict
get_vo2_max_summary_response_from_dict = GetVo2MaxSummaryResponse.from_dict(get_vo2_max_summary_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
