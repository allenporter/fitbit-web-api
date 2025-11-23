# AzmTimeSeriesDatapointValue

## Properties

| Name                             | Type    | Description                                                        | Notes      |
| -------------------------------- | ------- | ------------------------------------------------------------------ | ---------- |
| **active_zone_minutes**          | **int** | Total count of active zone minutes.                                | [optional] |
| **fat_burn_active_zone_minutes** | **int** | The number of active zone minutes in the fat burn heart rate zone. | [optional] |
| **cardio_active_zone_minutes**   | **int** | The number of active zone minutes in the cardio heart rate zone.   | [optional] |
| **peak_active_zone_minutes**     | **int** | The number of active zone minutes in the peak heart rate zone.     | [optional] |

## Example

```python
from fitbit_web_api.models.azm_time_series_datapoint_value import AzmTimeSeriesDatapointValue

# TODO update the JSON string below
json = "{}"
# create an instance of AzmTimeSeriesDatapointValue from a JSON string
azm_time_series_datapoint_value_instance = AzmTimeSeriesDatapointValue.from_json(json)
# print the JSON string representation of the object
print(AzmTimeSeriesDatapointValue.to_json())

# convert the object into a dict
azm_time_series_datapoint_value_dict = azm_time_series_datapoint_value_instance.to_dict()
# create an instance of AzmTimeSeriesDatapointValue from a dict
azm_time_series_datapoint_value_from_dict = AzmTimeSeriesDatapointValue.from_dict(azm_time_series_datapoint_value_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
