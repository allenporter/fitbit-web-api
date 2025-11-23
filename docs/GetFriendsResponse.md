# GetFriendsResponse

## Properties

| Name     | Type                          | Description | Notes      |
| -------- | ----------------------------- | ----------- | ---------- |
| **data** | [**List[Friend]**](Friend.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_friends_response import GetFriendsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFriendsResponse from a JSON string
get_friends_response_instance = GetFriendsResponse.from_json(json)
# print the JSON string representation of the object
print(GetFriendsResponse.to_json())

# convert the object into a dict
get_friends_response_dict = get_friends_response_instance.to_dict()
# create an instance of GetFriendsResponse from a dict
get_friends_response_from_dict = GetFriendsResponse.from_dict(get_friends_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
