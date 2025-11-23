# GetActivityGoalsResponse

## Properties

| Name      | Type                                  | Description | Notes      |
| --------- | ------------------------------------- | ----------- | ---------- |
| **goals** | [**ActivityGoals**](ActivityGoals.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_activity_goals_response import GetActivityGoalsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetActivityGoalsResponse from a JSON string
get_activity_goals_response_instance = GetActivityGoalsResponse.from_json(json)
# print the JSON string representation of the object
print(GetActivityGoalsResponse.to_json())

# convert the object into a dict
get_activity_goals_response_dict = get_activity_goals_response_instance.to_dict()
# create an instance of GetActivityGoalsResponse from a dict
get_activity_goals_response_from_dict = GetActivityGoalsResponse.from_dict(get_activity_goals_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
