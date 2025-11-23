# ActivityGoals

## Properties

| Name                    | Type      | Description                               | Notes      |
| ----------------------- | --------- | ----------------------------------------- | ---------- |
| **active_minutes**      | **int**   | Daily active minutes goal.                | [optional] |
| **active_zone_minutes** | **int**   | Daily or weekly active zone minutes goal. | [optional] |
| **calories_out**        | **int**   | Daily calories burned goal.               | [optional] |
| **distance**            | **float** | Daily or weekly distance goal.            | [optional] |
| **floors**              | **int**   | Daily or weekly floors climbed goal.      | [optional] |
| **steps**               | **int**   | Daily or weekly steps taken goal.         | [optional] |

## Example

```python
from fitbit_web_api.models.activity_goals import ActivityGoals

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityGoals from a JSON string
activity_goals_instance = ActivityGoals.from_json(json)
# print the JSON string representation of the object
print(ActivityGoals.to_json())

# convert the object into a dict
activity_goals_dict = activity_goals_instance.to_dict()
# create an instance of ActivityGoals from a dict
activity_goals_from_dict = ActivityGoals.from_dict(activity_goals_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
