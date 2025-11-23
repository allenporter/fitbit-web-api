# GetHrvSummaryResponse

## Properties

| Name    | Type                                  | Description | Notes      |
| ------- | ------------------------------------- | ----------- | ---------- |
| **hrv** | [**List[HrvSummary]**](HrvSummary.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_hrv_summary_response import GetHrvSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetHrvSummaryResponse from a JSON string
get_hrv_summary_response_instance = GetHrvSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(GetHrvSummaryResponse.to_json())

# convert the object into a dict
get_hrv_summary_response_dict = get_hrv_summary_response_instance.to_dict()
# create an instance of GetHrvSummaryResponse from a dict
get_hrv_summary_response_from_dict = GetHrvSummaryResponse.from_dict(get_hrv_summary_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
