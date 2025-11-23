# LifetimeStatsLifetime

The user's lifetime stats.

## Properties

| Name        | Type                                                                | Description | Notes      |
| ----------- | ------------------------------------------------------------------- | ----------- | ---------- |
| **total**   | [**LifetimeStatsLifetimeTotal**](LifetimeStatsLifetimeTotal.md)     |             | [optional] |
| **tracker** | [**LifetimeStatsLifetimeTracker**](LifetimeStatsLifetimeTracker.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.lifetime_stats_lifetime import LifetimeStatsLifetime

# TODO update the JSON string below
json = "{}"
# create an instance of LifetimeStatsLifetime from a JSON string
lifetime_stats_lifetime_instance = LifetimeStatsLifetime.from_json(json)
# print the JSON string representation of the object
print(LifetimeStatsLifetime.to_json())

# convert the object into a dict
lifetime_stats_lifetime_dict = lifetime_stats_lifetime_instance.to_dict()
# create an instance of LifetimeStatsLifetime from a dict
lifetime_stats_lifetime_from_dict = LifetimeStatsLifetime.from_dict(lifetime_stats_lifetime_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
