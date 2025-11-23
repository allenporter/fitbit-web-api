# FoodLogEntry

## Properties

| Name                   | Type                                          | Description                     | Notes      |
| ---------------------- | --------------------------------------------- | ------------------------------- | ---------- |
| **is_favorite**        | **bool**                                      | Whether the food is a favorite. | [optional] |
| **log_date**           | **date**                                      | The date of the log entry.      | [optional] |
| **log_id**             | **int**                                       | The ID of the log entry.        | [optional] |
| **logged_food**        | [**LoggedFood**](LoggedFood.md)               |                                 | [optional] |
| **nutritional_values** | [**NutritionalValues**](NutritionalValues.md) |                                 | [optional] |

## Example

```python
from fitbit_web_api.models.food_log_entry import FoodLogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of FoodLogEntry from a JSON string
food_log_entry_instance = FoodLogEntry.from_json(json)
# print the JSON string representation of the object
print(FoodLogEntry.to_json())

# convert the object into a dict
food_log_entry_dict = food_log_entry_instance.to_dict()
# create an instance of FoodLogEntry from a dict
food_log_entry_from_dict = FoodLogEntry.from_dict(food_log_entry_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
