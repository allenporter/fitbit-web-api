# GetWaterGoalResponse

## Properties

| Name     | Type                          | Description | Notes      |
| -------- | ----------------------------- | ----------- | ---------- |
| **goal** | [**WaterGoal**](WaterGoal.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_water_goal_response import GetWaterGoalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWaterGoalResponse from a JSON string
get_water_goal_response_instance = GetWaterGoalResponse.from_json(json)
# print the JSON string representation of the object
print(GetWaterGoalResponse.to_json())

# convert the object into a dict
get_water_goal_response_dict = get_water_goal_response_instance.to_dict()
# create an instance of GetWaterGoalResponse from a dict
get_water_goal_response_from_dict = GetWaterGoalResponse.from_dict(get_water_goal_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
