# LeaderboardFriendRelationshipsUserData

## Properties

| Name     | Type    | Description       | Notes      |
| -------- | ------- | ----------------- | ---------- |
| **id**   | **str** | Fitbit user id.   | [optional] |
| **type** | **str** | Supported: person | [optional] |

## Example

```python
from fitbit_web_api.models.leaderboard_friend_relationships_user_data import LeaderboardFriendRelationshipsUserData

# TODO update the JSON string below
json = "{}"
# create an instance of LeaderboardFriendRelationshipsUserData from a JSON string
leaderboard_friend_relationships_user_data_instance = LeaderboardFriendRelationshipsUserData.from_json(json)
# print the JSON string representation of the object
print(LeaderboardFriendRelationshipsUserData.to_json())

# convert the object into a dict
leaderboard_friend_relationships_user_data_dict = leaderboard_friend_relationships_user_data_instance.to_dict()
# create an instance of LeaderboardFriendRelationshipsUserData from a dict
leaderboard_friend_relationships_user_data_from_dict = LeaderboardFriendRelationshipsUserData.from_dict(leaderboard_friend_relationships_user_data_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
