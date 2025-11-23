# LeaderboardFriendRelationships

## Properties

| Name     | Type                                                                            | Description | Notes      |
| -------- | ------------------------------------------------------------------------------- | ----------- | ---------- |
| **user** | [**LeaderboardFriendRelationshipsUser**](LeaderboardFriendRelationshipsUser.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.leaderboard_friend_relationships import LeaderboardFriendRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of LeaderboardFriendRelationships from a JSON string
leaderboard_friend_relationships_instance = LeaderboardFriendRelationships.from_json(json)
# print the JSON string representation of the object
print(LeaderboardFriendRelationships.to_json())

# convert the object into a dict
leaderboard_friend_relationships_dict = leaderboard_friend_relationships_instance.to_dict()
# create an instance of LeaderboardFriendRelationships from a dict
leaderboard_friend_relationships_from_dict = LeaderboardFriendRelationships.from_dict(leaderboard_friend_relationships_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
