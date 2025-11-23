# GetFriendsLeaderboardResponse

## Properties

| Name     | Type                                                | Description | Notes      |
| -------- | --------------------------------------------------- | ----------- | ---------- |
| **data** | [**List[LeaderboardFriend]**](LeaderboardFriend.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_friends_leaderboard_response import GetFriendsLeaderboardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFriendsLeaderboardResponse from a JSON string
get_friends_leaderboard_response_instance = GetFriendsLeaderboardResponse.from_json(json)
# print the JSON string representation of the object
print(GetFriendsLeaderboardResponse.to_json())

# convert the object into a dict
get_friends_leaderboard_response_dict = get_friends_leaderboard_response_instance.to_dict()
# create an instance of GetFriendsLeaderboardResponse from a dict
get_friends_leaderboard_response_from_dict = GetFriendsLeaderboardResponse.from_dict(get_friends_leaderboard_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
