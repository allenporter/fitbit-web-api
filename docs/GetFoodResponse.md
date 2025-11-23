# GetFoodResponse

## Properties

| Name     | Type                | Description | Notes      |
| -------- | ------------------- | ----------- | ---------- |
| **food** | [**Food**](Food.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_food_response import GetFoodResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFoodResponse from a JSON string
get_food_response_instance = GetFoodResponse.from_json(json)
# print the JSON string representation of the object
print(GetFoodResponse.to_json())

# convert the object into a dict
get_food_response_dict = get_food_response_instance.to_dict()
# create an instance of GetFoodResponse from a dict
get_food_response_from_dict = GetFoodResponse.from_dict(get_food_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
