# LoggedFood

## Properties

| Name             | Type                                    | Description                   | Notes      |
| ---------------- | --------------------------------------- | ----------------------------- | ---------- |
| **access_level** | **str**                                 | The access level of the food. | [optional] |
| **amount**       | **float**                               | The amount of food consumed.  | [optional] |
| **brand**        | **str**                                 | The brand of the food.        | [optional] |
| **calories**     | **int**                                 | The calories in the food.     | [optional] |
| **food_id**      | **int**                                 | The ID of the food.           | [optional] |
| **locale**       | **str**                                 | The locale of the food.       | [optional] |
| **meal_type_id** | **int**                                 | The meal type ID.             | [optional] |
| **name**         | **str**                                 | The name of the food.         | [optional] |
| **unit**         | [**LoggedFoodUnit**](LoggedFoodUnit.md) |                               | [optional] |
| **units**        | **List[int]**                           | List of unit IDs.             | [optional] |

## Example

```python
from fitbit_web_api.models.logged_food import LoggedFood

# TODO update the JSON string below
json = "{}"
# create an instance of LoggedFood from a JSON string
logged_food_instance = LoggedFood.from_json(json)
# print the JSON string representation of the object
print(LoggedFood.to_json())

# convert the object into a dict
logged_food_dict = logged_food_instance.to_dict()
# create an instance of LoggedFood from a dict
logged_food_from_dict = LoggedFood.from_dict(logged_food_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
