# AzmValue

## Properties

| Name                             | Type    | Description                                                        | Notes      |
| -------------------------------- | ------- | ------------------------------------------------------------------ | ---------- |
| **active_zone_minutes**          | **int** | Total count of active zone minutes earned.                         | [optional] |
| **fat_burn_active_zone_minutes** | **int** | The number of active zone minutes in the fat burn heart rate zone. | [optional] |
| **cardio_active_zone_minutes**   | **int** | The number of active zone minutes in the cardio heart rate zone.   | [optional] |
| **peak_active_zone_minutes**     | **int** | The number of active zone minutes in the peak heart rate zone.     | [optional] |

## Example

```python
from fitbit_web_api.models.azm_value import AzmValue

# TODO update the JSON string below
json = "{}"
# create an instance of AzmValue from a JSON string
azm_value_instance = AzmValue.from_json(json)
# print the JSON string representation of the object
print(AzmValue.to_json())

# convert the object into a dict
azm_value_dict = azm_value_instance.to_dict()
# create an instance of AzmValue from a dict
azm_value_from_dict = AzmValue.from_dict(azm_value_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
