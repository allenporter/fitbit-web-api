# MealFood

## Properties

| Name             | Type                        | Description                                       | Notes      |
| ---------------- | --------------------------- | ------------------------------------------------- | ---------- |
| **access_level** | **str**                     | The access level of the food (PUBLIC or PRIVATE). | [optional] |
| **amount**       | **float**                   | The amount of the food.                           | [optional] |
| **brand**        | **str**                     | The brand of the food.                            | [optional] |
| **calories**     | **int**                     | The number of calories in the food.               | [optional] |
| **food_id**      | **int**                     | The ID of the food.                               | [optional] |
| **locale**       | **str**                     | The locale of the food.                           | [optional] |
| **meal_type_id** | **int**                     | The meal type ID.                                 | [optional] |
| **name**         | **str**                     | The name of the food.                             | [optional] |
| **unit**         | [**FoodUnit**](FoodUnit.md) |                                                   | [optional] |
| **units**        | **List[int]**               | List of unit IDs available for this food.         | [optional] |

## Example

```python
from fitbit_web_api.models.meal_food import MealFood

# TODO update the JSON string below
json = "{}"
# create an instance of MealFood from a JSON string
meal_food_instance = MealFood.from_json(json)
# print the JSON string representation of the object
print(MealFood.to_json())

# convert the object into a dict
meal_food_dict = meal_food_instance.to_dict()
# create an instance of MealFood from a dict
meal_food_from_dict = MealFood.from_dict(meal_food_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
