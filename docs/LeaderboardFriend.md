# LeaderboardFriend

## Properties

| Name              | Type                                                                    | Description                                                                             | Notes         |
| ----------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------- | ---------- |
| **type**          | **str**                                                                 | Describes the user based on the frequency they sync their steps. Supported: ranked-user | inactive-user | [optional] |
| **id**            | **str**                                                                 | Fitbit user id.                                                                         | [optional]    |
| **attributes**    | [**LeaderboardFriendAttributes**](LeaderboardFriendAttributes.md)       |                                                                                         | [optional]    |
| **relationships** | [**LeaderboardFriendRelationships**](LeaderboardFriendRelationships.md) |                                                                                         | [optional]    |

## Example

```python
from fitbit_web_api.models.leaderboard_friend import LeaderboardFriend

# TODO update the JSON string below
json = "{}"
# create an instance of LeaderboardFriend from a JSON string
leaderboard_friend_instance = LeaderboardFriend.from_json(json)
# print the JSON string representation of the object
print(LeaderboardFriend.to_json())

# convert the object into a dict
leaderboard_friend_dict = leaderboard_friend_instance.to_dict()
# create an instance of LeaderboardFriend from a dict
leaderboard_friend_from_dict = LeaderboardFriend.from_dict(leaderboard_friend_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
