# NutritionalValues

## Properties

| Name         | Type      | Description    | Notes      |
| ------------ | --------- | -------------- | ---------- |
| **calories** | **int**   | Calories.      | [optional] |
| **carbs**    | **float** | Carbohydrates. | [optional] |
| **fat**      | **float** | Fat.           | [optional] |
| **fiber**    | **float** | Fiber.         | [optional] |
| **protein**  | **float** | Protein.       | [optional] |
| **sodium**   | **float** | Sodium.        | [optional] |

## Example

```python
from fitbit_web_api.models.nutritional_values import NutritionalValues

# TODO update the JSON string below
json = "{}"
# create an instance of NutritionalValues from a JSON string
nutritional_values_instance = NutritionalValues.from_json(json)
# print the JSON string representation of the object
print(NutritionalValues.to_json())

# convert the object into a dict
nutritional_values_dict = nutritional_values_instance.to_dict()
# create an instance of NutritionalValues from a dict
nutritional_values_from_dict = NutritionalValues.from_dict(nutritional_values_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
