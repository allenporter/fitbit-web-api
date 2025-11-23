# LifetimeStatsBest

The user's best achievements.

## Properties

| Name        | Type                                                        | Description | Notes      |
| ----------- | ----------------------------------------------------------- | ----------- | ---------- |
| **total**   | [**LifetimeStatsBestTotal**](LifetimeStatsBestTotal.md)     |             | [optional] |
| **tracker** | [**LifetimeStatsBestTracker**](LifetimeStatsBestTracker.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.lifetime_stats_best import LifetimeStatsBest

# TODO update the JSON string below
json = "{}"
# create an instance of LifetimeStatsBest from a JSON string
lifetime_stats_best_instance = LifetimeStatsBest.from_json(json)
# print the JSON string representation of the object
print(LifetimeStatsBest.to_json())

# convert the object into a dict
lifetime_stats_best_dict = lifetime_stats_best_instance.to_dict()
# create an instance of LifetimeStatsBest from a dict
lifetime_stats_best_from_dict = LifetimeStatsBest.from_dict(lifetime_stats_best_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
