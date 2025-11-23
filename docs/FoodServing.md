# FoodServing

## Properties

| Name             | Type                        | Description                          | Notes      |
| ---------------- | --------------------------- | ------------------------------------ | ---------- |
| **multiplier**   | **float**                   | The multiplier for the serving size. | [optional] |
| **serving_size** | **float**                   | The serving size.                    | [optional] |
| **unit**         | [**FoodUnit**](FoodUnit.md) |                                      | [optional] |
| **unit_id**      | **int**                     | The ID of the unit.                  | [optional] |

## Example

```python
from fitbit_web_api.models.food_serving import FoodServing

# TODO update the JSON string below
json = "{}"
# create an instance of FoodServing from a JSON string
food_serving_instance = FoodServing.from_json(json)
# print the JSON string representation of the object
print(FoodServing.to_json())

# convert the object into a dict
food_serving_dict = food_serving_instance.to_dict()
# create an instance of FoodServing from a dict
food_serving_from_dict = FoodServing.from_dict(food_serving_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
