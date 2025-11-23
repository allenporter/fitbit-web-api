# AzmTimeSeriesDatapoint

## Properties

| Name          | Type                                                              | Description                                           | Notes      |
| ------------- | ----------------------------------------------------------------- | ----------------------------------------------------- | ---------- |
| **date_time** | **date**                                                          | The date specified in the format YYYY-MM-DD or today. | [optional] |
| **value**     | [**AzmTimeSeriesDatapointValue**](AzmTimeSeriesDatapointValue.md) |                                                       | [optional] |

## Example

```python
from fitbit_web_api.models.azm_time_series_datapoint import AzmTimeSeriesDatapoint

# TODO update the JSON string below
json = "{}"
# create an instance of AzmTimeSeriesDatapoint from a JSON string
azm_time_series_datapoint_instance = AzmTimeSeriesDatapoint.from_json(json)
# print the JSON string representation of the object
print(AzmTimeSeriesDatapoint.to_json())

# convert the object into a dict
azm_time_series_datapoint_dict = azm_time_series_datapoint_instance.to_dict()
# create an instance of AzmTimeSeriesDatapoint from a dict
azm_time_series_datapoint_from_dict = AzmTimeSeriesDatapoint.from_dict(azm_time_series_datapoint_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
