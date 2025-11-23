# GetSpO2SummaryResponse

## Properties

| Name     | Type                                    | Description             | Notes      |
| -------- | --------------------------------------- | ----------------------- | ---------- |
| **spo2** | [**List[SpO2Summary]**](SpO2Summary.md) | List of SpO2 summaries. | [optional] |

## Example

```python
from fitbit_web_api.models.get_sp_o2_summary_response import GetSpO2SummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSpO2SummaryResponse from a JSON string
get_sp_o2_summary_response_instance = GetSpO2SummaryResponse.from_json(json)
# print the JSON string representation of the object
print(GetSpO2SummaryResponse.to_json())

# convert the object into a dict
get_sp_o2_summary_response_dict = get_sp_o2_summary_response_instance.to_dict()
# create an instance of GetSpO2SummaryResponse from a dict
get_sp_o2_summary_response_from_dict = GetSpO2SummaryResponse.from_dict(get_sp_o2_summary_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
