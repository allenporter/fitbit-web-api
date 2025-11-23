# LifetimeStatsLifetimeTracker

The total lifetime stats including tracker data only.

## Properties

| Name             | Type      | Description                                                                             | Notes      |
| ---------------- | --------- | --------------------------------------------------------------------------------------- | ---------- |
| **active_score** | **int**   | Functionality removed. A response is returned for backward compatibility.               | [optional] |
| **calories_out** | **int**   | Functionality removed. A response is returned for backward compatibility.               | [optional] |
| **distance**     | **float** | The total distance recorded by the tracker over the lifetime of the user&#39;s account. | [optional] |
| **floors**       | **int**   | The total floors recorded by the tracker over the lifetime of the user&#39;s account.   | [optional] |
| **steps**        | **int**   | The total steps recorded by the tracker over the lifetime of the user&#39;s account.    | [optional] |

## Example

```python
from fitbit_web_api.models.lifetime_stats_lifetime_tracker import LifetimeStatsLifetimeTracker

# TODO update the JSON string below
json = "{}"
# create an instance of LifetimeStatsLifetimeTracker from a JSON string
lifetime_stats_lifetime_tracker_instance = LifetimeStatsLifetimeTracker.from_json(json)
# print the JSON string representation of the object
print(LifetimeStatsLifetimeTracker.to_json())

# convert the object into a dict
lifetime_stats_lifetime_tracker_dict = lifetime_stats_lifetime_tracker_instance.to_dict()
# create an instance of LifetimeStatsLifetimeTracker from a dict
lifetime_stats_lifetime_tracker_from_dict = LifetimeStatsLifetimeTracker.from_dict(lifetime_stats_lifetime_tracker_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
