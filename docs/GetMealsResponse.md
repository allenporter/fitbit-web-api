# GetMealsResponse

## Properties

| Name      | Type                      | Description | Notes      |
| --------- | ------------------------- | ----------- | ---------- |
| **meals** | [**List[Meal]**](Meal.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_meals_response import GetMealsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMealsResponse from a JSON string
get_meals_response_instance = GetMealsResponse.from_json(json)
# print the JSON string representation of the object
print(GetMealsResponse.to_json())

# convert the object into a dict
get_meals_response_dict = get_meals_response_instance.to_dict()
# create an instance of GetMealsResponse from a dict
get_meals_response_from_dict = GetMealsResponse.from_dict(get_meals_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
