# GetBodyGoalsResponse

## Properties

| Name     | Type                        | Description | Notes      |
| -------- | --------------------------- | ----------- | ---------- |
| **goal** | [**BodyGoal**](BodyGoal.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_body_goals_response import GetBodyGoalsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBodyGoalsResponse from a JSON string
get_body_goals_response_instance = GetBodyGoalsResponse.from_json(json)
# print the JSON string representation of the object
print(GetBodyGoalsResponse.to_json())

# convert the object into a dict
get_body_goals_response_dict = get_body_goals_response_instance.to_dict()
# create an instance of GetBodyGoalsResponse from a dict
get_body_goals_response_from_dict = GetBodyGoalsResponse.from_dict(get_body_goals_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
