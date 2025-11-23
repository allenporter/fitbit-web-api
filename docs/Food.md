# Food

## Properties

| Name                     | Type                                    | Description                   | Notes      |
| ------------------------ | --------------------------------------- | ----------------------------- | ---------- |
| **access_level**         | **str**                                 | The access level of the food. | [optional] |
| **brand**                | **str**                                 | The brand of the food.        | [optional] |
| **calories**             | **int**                                 | The calories in the food.     | [optional] |
| **default_serving_size** | **float**                               | The default serving size.     | [optional] |
| **default_unit**         | [**FoodUnit**](FoodUnit.md)             |                               | [optional] |
| **food_id**              | **int**                                 | The ID of the food.           | [optional] |
| **is_generic**           | **bool**                                | Whether the food is generic.  | [optional] |
| **locale**               | **str**                                 | The locale of the food.       | [optional] |
| **name**                 | **str**                                 | The name of the food.         | [optional] |
| **servings**             | [**List[FoodServing]**](FoodServing.md) | List of servings.             | [optional] |
| **units**                | **List[int]**                           | List of unit IDs.             | [optional] |

## Example

```python
from fitbit_web_api.models.food import Food

# TODO update the JSON string below
json = "{}"
# create an instance of Food from a JSON string
food_instance = Food.from_json(json)
# print the JSON string representation of the object
print(Food.to_json())

# convert the object into a dict
food_dict = food_instance.to_dict()
# create an instance of Food from a dict
food_from_dict = Food.from_dict(food_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
