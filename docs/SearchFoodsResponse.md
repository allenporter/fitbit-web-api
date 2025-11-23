# SearchFoodsResponse

## Properties

| Name      | Type                      | Description | Notes      |
| --------- | ------------------------- | ----------- | ---------- |
| **foods** | [**List[Food]**](Food.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.search_foods_response import SearchFoodsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFoodsResponse from a JSON string
search_foods_response_instance = SearchFoodsResponse.from_json(json)
# print the JSON string representation of the object
print(SearchFoodsResponse.to_json())

# convert the object into a dict
search_foods_response_dict = search_foods_response_instance.to_dict()
# create an instance of SearchFoodsResponse from a dict
search_foods_response_from_dict = SearchFoodsResponse.from_dict(search_foods_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
