# FoodGoals

## Properties

| Name         | Type    | Description                         | Notes      |
| ------------ | ------- | ----------------------------------- | ---------- |
| **calories** | **int** | The daily calorie consumption goal. | [optional] |

## Example

```python
from fitbit_web_api.models.food_goals import FoodGoals

# TODO update the JSON string below
json = "{}"
# create an instance of FoodGoals from a JSON string
food_goals_instance = FoodGoals.from_json(json)
# print the JSON string representation of the object
print(FoodGoals.to_json())

# convert the object into a dict
food_goals_dict = food_goals_instance.to_dict()
# create an instance of FoodGoals from a dict
food_goals_from_dict = FoodGoals.from_dict(food_goals_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
