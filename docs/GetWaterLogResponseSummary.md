# GetWaterLogResponseSummary

## Properties

| Name      | Type    | Description                                 | Notes      |
| --------- | ------- | ------------------------------------------- | ---------- |
| **water** | **int** | Total amount of water consumed for the day. | [optional] |

## Example

```python
from fitbit_web_api.models.get_water_log_response_summary import GetWaterLogResponseSummary

# TODO update the JSON string below
json = "{}"
# create an instance of GetWaterLogResponseSummary from a JSON string
get_water_log_response_summary_instance = GetWaterLogResponseSummary.from_json(json)
# print the JSON string representation of the object
print(GetWaterLogResponseSummary.to_json())

# convert the object into a dict
get_water_log_response_summary_dict = get_water_log_response_summary_instance.to_dict()
# create an instance of GetWaterLogResponseSummary from a dict
get_water_log_response_summary_from_dict = GetWaterLogResponseSummary.from_dict(get_water_log_response_summary_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
