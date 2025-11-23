# HrvIntradayValue

## Properties

| Name            | Type      | Description                                                                                     | Notes      |
| --------------- | --------- | ----------------------------------------------------------------------------------------------- | ---------- |
| **rmssd**       | **float** | The Root Mean Square of Successive Differences (RMSSD) between heart beats.                     | [optional] |
| **coverage**    | **float** | Data completeness in terms of the number of interbeat intervals.                                | [optional] |
| **hf**          | **float** | The power in interbeat interval fluctuations within the high frequency band (0.15 Hz - 0.4 Hz). | [optional] |
| **lf**          | **float** | The power in interbeat interval fluctuations within the low frequency band (0.04 Hz - 0.15 Hz). | [optional] |
| **daily_rmssd** | **float** | The Root Mean Square of Successive Differences (RMSSD) between heart beats. (Interval response) | [optional] |

## Example

```python
from fitbit_web_api.models.hrv_intraday_value import HrvIntradayValue

# TODO update the JSON string below
json = "{}"
# create an instance of HrvIntradayValue from a JSON string
hrv_intraday_value_instance = HrvIntradayValue.from_json(json)
# print the JSON string representation of the object
print(HrvIntradayValue.to_json())

# convert the object into a dict
hrv_intraday_value_dict = hrv_intraday_value_instance.to_dict()
# create an instance of HrvIntradayValue from a dict
hrv_intraday_value_from_dict = HrvIntradayValue.from_dict(hrv_intraday_value_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
