# LeaderboardFriendRelationshipsUser

## Properties

| Name     | Type                                                                                    | Description | Notes      |
| -------- | --------------------------------------------------------------------------------------- | ----------- | ---------- |
| **data** | [**LeaderboardFriendRelationshipsUserData**](LeaderboardFriendRelationshipsUserData.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.leaderboard_friend_relationships_user import LeaderboardFriendRelationshipsUser

# TODO update the JSON string below
json = "{}"
# create an instance of LeaderboardFriendRelationshipsUser from a JSON string
leaderboard_friend_relationships_user_instance = LeaderboardFriendRelationshipsUser.from_json(json)
# print the JSON string representation of the object
print(LeaderboardFriendRelationshipsUser.to_json())

# convert the object into a dict
leaderboard_friend_relationships_user_dict = leaderboard_friend_relationships_user_instance.to_dict()
# create an instance of LeaderboardFriendRelationshipsUser from a dict
leaderboard_friend_relationships_user_from_dict = LeaderboardFriendRelationshipsUser.from_dict(leaderboard_friend_relationships_user_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
