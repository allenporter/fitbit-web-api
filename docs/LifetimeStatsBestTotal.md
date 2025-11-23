# LifetimeStatsBestTotal

The user's best achievements including tracker and manual activity log entries.

## Properties

| Name         | Type                                                                    | Description | Notes      |
| ------------ | ----------------------------------------------------------------------- | ----------- | ---------- |
| **distance** | [**LifetimeStatsBestTotalDistance**](LifetimeStatsBestTotalDistance.md) |             | [optional] |
| **floors**   | [**LifetimeStatsBestTotalFloors**](LifetimeStatsBestTotalFloors.md)     |             | [optional] |
| **steps**    | [**LifetimeStatsBestTotalSteps**](LifetimeStatsBestTotalSteps.md)       |             | [optional] |

## Example

```python
from fitbit_web_api.models.lifetime_stats_best_total import LifetimeStatsBestTotal

# TODO update the JSON string below
json = "{}"
# create an instance of LifetimeStatsBestTotal from a JSON string
lifetime_stats_best_total_instance = LifetimeStatsBestTotal.from_json(json)
# print the JSON string representation of the object
print(LifetimeStatsBestTotal.to_json())

# convert the object into a dict
lifetime_stats_best_total_dict = lifetime_stats_best_total_instance.to_dict()
# create an instance of LifetimeStatsBestTotal from a dict
lifetime_stats_best_total_from_dict = LifetimeStatsBestTotal.from_dict(lifetime_stats_best_total_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
