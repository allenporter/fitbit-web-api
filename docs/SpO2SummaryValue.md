# SpO2SummaryValue

The SpO2 value.

## Properties

| Name    | Type      | Description                                                            | Notes      |
| ------- | --------- | ---------------------------------------------------------------------- | ---------- |
| **avg** | **float** | The mean of the 1 minute SpO2 levels calculated as a percentage value. | [optional] |
| **min** | **float** | The minimum daily SpO2 level calculated as a percentage value.         | [optional] |
| **max** | **float** | The maximum daily SpO2 level calculated as a percentage value.         | [optional] |

## Example

```python
from fitbit_web_api.models.sp_o2_summary_value import SpO2SummaryValue

# TODO update the JSON string below
json = "{}"
# create an instance of SpO2SummaryValue from a JSON string
sp_o2_summary_value_instance = SpO2SummaryValue.from_json(json)
# print the JSON string representation of the object
print(SpO2SummaryValue.to_json())

# convert the object into a dict
sp_o2_summary_value_dict = sp_o2_summary_value_instance.to_dict()
# create an instance of SpO2SummaryValue from a dict
sp_o2_summary_value_from_dict = SpO2SummaryValue.from_dict(sp_o2_summary_value_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
