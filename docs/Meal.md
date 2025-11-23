# Meal

## Properties

| Name            | Type                              | Description                  | Notes      |
| --------------- | --------------------------------- | ---------------------------- | ---------- |
| **description** | **str**                           | The description of the meal. | [optional] |
| **id**          | **int**                           | The ID of the meal.          | [optional] |
| **meal_foods**  | [**List[MealFood]**](MealFood.md) |                              | [optional] |
| **name**        | **str**                           | The name of the meal.        | [optional] |

## Example

```python
from fitbit_web_api.models.meal import Meal

# TODO update the JSON string below
json = "{}"
# create an instance of Meal from a JSON string
meal_instance = Meal.from_json(json)
# print the JSON string representation of the object
print(Meal.to_json())

# convert the object into a dict
meal_dict = meal_instance.to_dict()
# create an instance of Meal from a dict
meal_from_dict = Meal.from_dict(meal_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
