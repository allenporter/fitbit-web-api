# Friend

## Properties

| Name           | Type                                        | Description       | Notes      |
| -------------- | ------------------------------------------- | ----------------- | ---------- |
| **type**       | **str**                                     | Supported: person | [optional] |
| **id**         | **str**                                     | Fitbit user id.   | [optional] |
| **attributes** | [**FriendAttributes**](FriendAttributes.md) |                   | [optional] |

## Example

```python
from fitbit_web_api.models.friend import Friend

# TODO update the JSON string below
json = "{}"
# create an instance of Friend from a JSON string
friend_instance = Friend.from_json(json)
# print the JSON string representation of the object
print(Friend.to_json())

# convert the object into a dict
friend_dict = friend_instance.to_dict()
# create an instance of Friend from a dict
friend_from_dict = Friend.from_dict(friend_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
