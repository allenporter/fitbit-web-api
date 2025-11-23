# GetFoodLogResponse

## Properties

| Name        | Type                                          | Description               | Notes      |
| ----------- | --------------------------------------------- | ------------------------- | ---------- |
| **foods**   | [**List[FoodLogEntry]**](FoodLogEntry.md)     | List of food log entries. | [optional] |
| **goals**   | [**FoodGoals**](FoodGoals.md)                 |                           | [optional] |
| **summary** | [**NutritionalValues**](NutritionalValues.md) |                           | [optional] |

## Example

```python
from fitbit_web_api.models.get_food_log_response import GetFoodLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFoodLogResponse from a JSON string
get_food_log_response_instance = GetFoodLogResponse.from_json(json)
# print the JSON string representation of the object
print(GetFoodLogResponse.to_json())

# convert the object into a dict
get_food_log_response_dict = get_food_log_response_instance.to_dict()
# create an instance of GetFoodLogResponse from a dict
get_food_log_response_from_dict = GetFoodLogResponse.from_dict(get_food_log_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
