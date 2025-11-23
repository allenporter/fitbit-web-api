# GetNutritionTimeSeriesResponse

## Properties

| Name                      | Type                                                                      | Description | Notes      |
| ------------------------- | ------------------------------------------------------------------------- | ----------- | ---------- |
| **foods_log_calories_in** | [**List[NutritionTimeSeriesDatapoint]**](NutritionTimeSeriesDatapoint.md) |             | [optional] |
| **foods_log_water**       | [**List[NutritionTimeSeriesDatapoint]**](NutritionTimeSeriesDatapoint.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_nutrition_time_series_response import GetNutritionTimeSeriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetNutritionTimeSeriesResponse from a JSON string
get_nutrition_time_series_response_instance = GetNutritionTimeSeriesResponse.from_json(json)
# print the JSON string representation of the object
print(GetNutritionTimeSeriesResponse.to_json())

# convert the object into a dict
get_nutrition_time_series_response_dict = get_nutrition_time_series_response_instance.to_dict()
# create an instance of GetNutritionTimeSeriesResponse from a dict
get_nutrition_time_series_response_from_dict = GetNutritionTimeSeriesResponse.from_dict(get_nutrition_time_series_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
