# SpO2Summary

## Properties

| Name          | Type                                        | Description                                            | Notes      |
| ------------- | ------------------------------------------- | ------------------------------------------------------ | ---------- |
| **date_time** | **date**                                    | The sleep log date specified in the format YYYY-MM-DD. | [optional] |
| **value**     | [**SpO2SummaryValue**](SpO2SummaryValue.md) |                                                        | [optional] |

## Example

```python
from fitbit_web_api.models.sp_o2_summary import SpO2Summary

# TODO update the JSON string below
json = "{}"
# create an instance of SpO2Summary from a JSON string
sp_o2_summary_instance = SpO2Summary.from_json(json)
# print the JSON string representation of the object
print(SpO2Summary.to_json())

# convert the object into a dict
sp_o2_summary_dict = sp_o2_summary_instance.to_dict()
# create an instance of SpO2Summary from a dict
sp_o2_summary_from_dict = SpO2Summary.from_dict(sp_o2_summary_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
