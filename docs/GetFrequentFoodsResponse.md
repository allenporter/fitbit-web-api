# GetFrequentFoodsResponse

## Properties

| Name      | Type                      | Description | Notes      |
| --------- | ------------------------- | ----------- | ---------- |
| **foods** | [**List[Food]**](Food.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_frequent_foods_response import GetFrequentFoodsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFrequentFoodsResponse from a JSON string
get_frequent_foods_response_instance = GetFrequentFoodsResponse.from_json(json)
# print the JSON string representation of the object
print(GetFrequentFoodsResponse.to_json())

# convert the object into a dict
get_frequent_foods_response_dict = get_frequent_foods_response_instance.to_dict()
# create an instance of GetFrequentFoodsResponse from a dict
get_frequent_foods_response_from_dict = GetFrequentFoodsResponse.from_dict(get_frequent_foods_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
