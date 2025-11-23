# BodyGoal

## Properties

| Name                 | Type      | Description                                                                      | Notes      |
| -------------------- | --------- | -------------------------------------------------------------------------------- | ---------- | -------- | ---------- |
| **goal_type**        | **str**   | The goal type. Supported: LOSE                                                   | GAIN       | MAINTAIN | [optional] |
| **start_date**       | **date**  | The goal start date.                                                             | [optional] |
| **start_weight**     | **float** | User&#39;s weight when goal was established.                                     | [optional] |
| **weight**           | **float** | The weight goal to achieve.                                                      | [optional] |
| **weight_threshold** | **float** | The recommended amount of weight to lose each week to achieve and maintain goal. | [optional] |
| **fat**              | **float** | The body fat goal to achieve.                                                    | [optional] |

## Example

```python
from fitbit_web_api.models.body_goal import BodyGoal

# TODO update the JSON string below
json = "{}"
# create an instance of BodyGoal from a JSON string
body_goal_instance = BodyGoal.from_json(json)
# print the JSON string representation of the object
print(BodyGoal.to_json())

# convert the object into a dict
body_goal_dict = body_goal_instance.to_dict()
# create an instance of BodyGoal from a dict
body_goal_from_dict = BodyGoal.from_dict(body_goal_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
