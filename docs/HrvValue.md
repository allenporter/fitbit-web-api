# HrvValue

## Properties

| Name            | Type      | Description                                                                                                                                                                        | Notes      |
| --------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **daily_rmssd** | **float** | The Root Mean Square of Successive Differences (RMSSD) between heart beats. It measures short-term variability in the user’s daily heart rate in milliseconds (ms).                | [optional] |
| **deep_rmssd**  | **float** | The Root Mean Square of Successive Differences (RMSSD) between heart beats. It measures short-term variability in the user’s heart rate while in deep sleep, in milliseconds (ms). | [optional] |

## Example

```python
from fitbit_web_api.models.hrv_value import HrvValue

# TODO update the JSON string below
json = "{}"
# create an instance of HrvValue from a JSON string
hrv_value_instance = HrvValue.from_json(json)
# print the JSON string representation of the object
print(HrvValue.to_json())

# convert the object into a dict
hrv_value_dict = hrv_value_instance.to_dict()
# create an instance of HrvValue from a dict
hrv_value_from_dict = HrvValue.from_dict(hrv_value_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
