# LeaderboardFriendAttributes

## Properties

| Name             | Type     | Description                                         | Notes      |
| ---------------- | -------- | --------------------------------------------------- | ---------- |
| **avatar**       | **str**  | Link to user&#39;s avatar picture.                  | [optional] |
| **child**        | **bool** | Boolean value describing friend as a child account. | [optional] |
| **friend**       | **bool** | Supported: true                                     | [optional] |
| **name**         | **str**  | Person&#39;s display name.                          | [optional] |
| **step_rank**    | **int**  | Ranking among the user&#39;s friends.               | [optional] |
| **step_summary** | **int**  | Weekly step count.                                  | [optional] |

## Example

```python
from fitbit_web_api.models.leaderboard_friend_attributes import LeaderboardFriendAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of LeaderboardFriendAttributes from a JSON string
leaderboard_friend_attributes_instance = LeaderboardFriendAttributes.from_json(json)
# print the JSON string representation of the object
print(LeaderboardFriendAttributes.to_json())

# convert the object into a dict
leaderboard_friend_attributes_dict = leaderboard_friend_attributes_instance.to_dict()
# create an instance of LeaderboardFriendAttributes from a dict
leaderboard_friend_attributes_from_dict = LeaderboardFriendAttributes.from_dict(leaderboard_friend_attributes_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
