# IrnBpmData

## Properties

| Name          | Type         | Description                                                | Notes      |
| ------------- | ------------ | ---------------------------------------------------------- | ---------- |
| **data_time** | **datetime** | The timestamp of the individual heart beat.                | [optional] |
| **value**     | **int**      | The extrapolated bpm value from the individual heart beat. | [optional] |

## Example

```python
from fitbit_web_api.models.irn_bpm_data import IrnBpmData

# TODO update the JSON string below
json = "{}"
# create an instance of IrnBpmData from a JSON string
irn_bpm_data_instance = IrnBpmData.from_json(json)
# print the JSON string representation of the object
print(IrnBpmData.to_json())

# convert the object into a dict
irn_bpm_data_dict = irn_bpm_data_instance.to_dict()
# create an instance of IrnBpmData from a dict
irn_bpm_data_from_dict = IrnBpmData.from_dict(irn_bpm_data_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
