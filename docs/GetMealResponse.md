# GetMealResponse

## Properties

| Name     | Type                | Description | Notes      |
| -------- | ------------------- | ----------- | ---------- |
| **meal** | [**Meal**](Meal.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_meal_response import GetMealResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMealResponse from a JSON string
get_meal_response_instance = GetMealResponse.from_json(json)
# print the JSON string representation of the object
print(GetMealResponse.to_json())

# convert the object into a dict
get_meal_response_dict = get_meal_response_instance.to_dict()
# create an instance of GetMealResponse from a dict
get_meal_response_from_dict = GetMealResponse.from_dict(get_meal_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
