# HrvSummary

## Properties

| Name          | Type                        | Description                                            | Notes      |
| ------------- | --------------------------- | ------------------------------------------------------ | ---------- |
| **date_time** | **date**                    | The sleep log date specified in the format YYYY-MM-DD. | [optional] |
| **value**     | [**HrvValue**](HrvValue.md) |                                                        | [optional] |

## Example

```python
from fitbit_web_api.models.hrv_summary import HrvSummary

# TODO update the JSON string below
json = "{}"
# create an instance of HrvSummary from a JSON string
hrv_summary_instance = HrvSummary.from_json(json)
# print the JSON string representation of the object
print(HrvSummary.to_json())

# convert the object into a dict
hrv_summary_dict = hrv_summary_instance.to_dict()
# create an instance of HrvSummary from a dict
hrv_summary_from_dict = HrvSummary.from_dict(hrv_summary_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
