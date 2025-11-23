# GetFoodGoalsResponse

## Properties

| Name      | Type                          | Description | Notes      |
| --------- | ----------------------------- | ----------- | ---------- |
| **goals** | [**FoodGoals**](FoodGoals.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_food_goals_response import GetFoodGoalsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFoodGoalsResponse from a JSON string
get_food_goals_response_instance = GetFoodGoalsResponse.from_json(json)
# print the JSON string representation of the object
print(GetFoodGoalsResponse.to_json())

# convert the object into a dict
get_food_goals_response_dict = get_food_goals_response_instance.to_dict()
# create an instance of GetFoodGoalsResponse from a dict
get_food_goals_response_from_dict = GetFoodGoalsResponse.from_dict(get_food_goals_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
