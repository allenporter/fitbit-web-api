# NutritionTimeSeriesDatapoint

## Properties

| Name          | Type     | Description                               | Notes      |
| ------------- | -------- | ----------------------------------------- | ---------- |
| **date_time** | **date** | The date of the recorded resource.        | [optional] |
| **value**     | **str**  | The specified resource&#39;s daily total. | [optional] |

## Example

```python
from fitbit_web_api.models.nutrition_time_series_datapoint import NutritionTimeSeriesDatapoint

# TODO update the JSON string below
json = "{}"
# create an instance of NutritionTimeSeriesDatapoint from a JSON string
nutrition_time_series_datapoint_instance = NutritionTimeSeriesDatapoint.from_json(json)
# print the JSON string representation of the object
print(NutritionTimeSeriesDatapoint.to_json())

# convert the object into a dict
nutrition_time_series_datapoint_dict = nutrition_time_series_datapoint_instance.to_dict()
# create an instance of NutritionTimeSeriesDatapoint from a dict
nutrition_time_series_datapoint_from_dict = NutritionTimeSeriesDatapoint.from_dict(nutrition_time_series_datapoint_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
