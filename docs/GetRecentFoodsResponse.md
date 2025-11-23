# GetRecentFoodsResponse

## Properties

| Name      | Type                      | Description | Notes      |
| --------- | ------------------------- | ----------- | ---------- |
| **foods** | [**List[Food]**](Food.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_recent_foods_response import GetRecentFoodsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecentFoodsResponse from a JSON string
get_recent_foods_response_instance = GetRecentFoodsResponse.from_json(json)
# print the JSON string representation of the object
print(GetRecentFoodsResponse.to_json())

# convert the object into a dict
get_recent_foods_response_dict = get_recent_foods_response_instance.to_dict()
# create an instance of GetRecentFoodsResponse from a dict
get_recent_foods_response_from_dict = GetRecentFoodsResponse.from_dict(get_recent_foods_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
