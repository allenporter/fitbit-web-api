# FriendAttributes

## Properties

| Name       | Type     | Description                                         | Notes      |
| ---------- | -------- | --------------------------------------------------- | ---------- |
| **avatar** | **str**  | Link to user&#39;s avatar picture.                  | [optional] |
| **child**  | **bool** | Boolean value describing friend as a child account. | [optional] |
| **friend** | **bool** | Boolean value describing user as a friend.          | [optional] |
| **name**   | **str**  | Person&#39;s display name.                          | [optional] |

## Example

```python
from fitbit_web_api.models.friend_attributes import FriendAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of FriendAttributes from a JSON string
friend_attributes_instance = FriendAttributes.from_json(json)
# print the JSON string representation of the object
print(FriendAttributes.to_json())

# convert the object into a dict
friend_attributes_dict = friend_attributes_instance.to_dict()
# create an instance of FriendAttributes from a dict
friend_attributes_from_dict = FriendAttributes.from_dict(friend_attributes_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
