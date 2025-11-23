# LifetimeStatsBestTracker

The user's best achievements including tracker data only.

## Properties

| Name         | Type                                                                    | Description | Notes      |
| ------------ | ----------------------------------------------------------------------- | ----------- | ---------- |
| **distance** | [**LifetimeStatsBestTotalDistance**](LifetimeStatsBestTotalDistance.md) |             | [optional] |
| **floors**   | [**LifetimeStatsBestTotalFloors**](LifetimeStatsBestTotalFloors.md)     |             | [optional] |
| **steps**    | [**LifetimeStatsBestTotalSteps**](LifetimeStatsBestTotalSteps.md)       |             | [optional] |

## Example

```python
from fitbit_web_api.models.lifetime_stats_best_tracker import LifetimeStatsBestTracker

# TODO update the JSON string below
json = "{}"
# create an instance of LifetimeStatsBestTracker from a JSON string
lifetime_stats_best_tracker_instance = LifetimeStatsBestTracker.from_json(json)
# print the JSON string representation of the object
print(LifetimeStatsBestTracker.to_json())

# convert the object into a dict
lifetime_stats_best_tracker_dict = lifetime_stats_best_tracker_instance.to_dict()
# create an instance of LifetimeStatsBestTracker from a dict
lifetime_stats_best_tracker_from_dict = LifetimeStatsBestTracker.from_dict(lifetime_stats_best_tracker_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
