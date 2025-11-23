# LifetimeStatsBestTotalSteps

## Properties

| Name         | Type     | Description                                           | Notes      |
| ------------ | -------- | ----------------------------------------------------- | ---------- |
| **var_date** | **date** | The date the user&#39;s best step count was achieved. | [optional] |
| **value**    | **int**  | The user&#39;s best step count achieved.              | [optional] |

## Example

```python
from fitbit_web_api.models.lifetime_stats_best_total_steps import LifetimeStatsBestTotalSteps

# TODO update the JSON string below
json = "{}"
# create an instance of LifetimeStatsBestTotalSteps from a JSON string
lifetime_stats_best_total_steps_instance = LifetimeStatsBestTotalSteps.from_json(json)
# print the JSON string representation of the object
print(LifetimeStatsBestTotalSteps.to_json())

# convert the object into a dict
lifetime_stats_best_total_steps_dict = lifetime_stats_best_total_steps_instance.to_dict()
# create an instance of LifetimeStatsBestTotalSteps from a dict
lifetime_stats_best_total_steps_from_dict = LifetimeStatsBestTotalSteps.from_dict(lifetime_stats_best_total_steps_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
