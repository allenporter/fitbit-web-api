# WaterGoal

## Properties

| Name           | Type     | Description                       | Notes      |
| -------------- | -------- | --------------------------------- | ---------- |
| **goal**       | **int**  | Amount of water to consume daily. | [optional] |
| **start_date** | **date** | Water goal&#39;s start date.      | [optional] |

## Example

```python
from fitbit_web_api.models.water_goal import WaterGoal

# TODO update the JSON string below
json = "{}"
# create an instance of WaterGoal from a JSON string
water_goal_instance = WaterGoal.from_json(json)
# print the JSON string representation of the object
print(WaterGoal.to_json())

# convert the object into a dict
water_goal_dict = water_goal_instance.to_dict()
# create an instance of WaterGoal from a dict
water_goal_from_dict = WaterGoal.from_dict(water_goal_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
