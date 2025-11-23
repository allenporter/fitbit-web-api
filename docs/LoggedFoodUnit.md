# LoggedFoodUnit

## Properties

| Name       | Type    | Description                  | Notes      |
| ---------- | ------- | ---------------------------- | ---------- |
| **id**     | **int** | The ID of the unit.          | [optional] |
| **name**   | **str** | The name of the unit.        | [optional] |
| **plural** | **str** | The plural name of the unit. | [optional] |

## Example

```python
from fitbit_web_api.models.logged_food_unit import LoggedFoodUnit

# TODO update the JSON string below
json = "{}"
# create an instance of LoggedFoodUnit from a JSON string
logged_food_unit_instance = LoggedFoodUnit.from_json(json)
# print the JSON string representation of the object
print(LoggedFoodUnit.to_json())

# convert the object into a dict
logged_food_unit_dict = logged_food_unit_instance.to_dict()
# create an instance of LoggedFoodUnit from a dict
logged_food_unit_from_dict = LoggedFoodUnit.from_dict(logged_food_unit_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
