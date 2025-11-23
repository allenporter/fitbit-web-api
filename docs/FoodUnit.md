# FoodUnit

## Properties

| Name       | Type    | Description                  | Notes      |
| ---------- | ------- | ---------------------------- | ---------- |
| **id**     | **int** | The ID of the unit.          | [optional] |
| **name**   | **str** | The name of the unit.        | [optional] |
| **plural** | **str** | The plural name of the unit. | [optional] |

## Example

```python
from fitbit_web_api.models.food_unit import FoodUnit

# TODO update the JSON string below
json = "{}"
# create an instance of FoodUnit from a JSON string
food_unit_instance = FoodUnit.from_json(json)
# print the JSON string representation of the object
print(FoodUnit.to_json())

# convert the object into a dict
food_unit_dict = food_unit_instance.to_dict()
# create an instance of FoodUnit from a dict
food_unit_from_dict = FoodUnit.from_dict(food_unit_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
