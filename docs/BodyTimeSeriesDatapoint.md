# BodyTimeSeriesDatapoint

## Properties

| Name          | Type     | Description                                   | Notes      |
| ------------- | -------- | --------------------------------------------- | ---------- |
| **date_time** | **date** | The datetime which the resource was recorded. | [optional] |
| **value**     | **str**  | The value of the resource.                    | [optional] |

## Example

```python
from fitbit_web_api.models.body_time_series_datapoint import BodyTimeSeriesDatapoint

# TODO update the JSON string below
json = "{}"
# create an instance of BodyTimeSeriesDatapoint from a JSON string
body_time_series_datapoint_instance = BodyTimeSeriesDatapoint.from_json(json)
# print the JSON string representation of the object
print(BodyTimeSeriesDatapoint.to_json())

# convert the object into a dict
body_time_series_datapoint_dict = body_time_series_datapoint_instance.to_dict()
# create an instance of BodyTimeSeriesDatapoint from a dict
body_time_series_datapoint_from_dict = BodyTimeSeriesDatapoint.from_dict(body_time_series_datapoint_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
