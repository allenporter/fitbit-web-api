# LifetimeStats

## Properties

| Name         | Type                                                  | Description | Notes      |
| ------------ | ----------------------------------------------------- | ----------- | ---------- |
| **best**     | [**LifetimeStatsBest**](LifetimeStatsBest.md)         |             | [optional] |
| **lifetime** | [**LifetimeStatsLifetime**](LifetimeStatsLifetime.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.lifetime_stats import LifetimeStats

# TODO update the JSON string below
json = "{}"
# create an instance of LifetimeStats from a JSON string
lifetime_stats_instance = LifetimeStats.from_json(json)
# print the JSON string representation of the object
print(LifetimeStats.to_json())

# convert the object into a dict
lifetime_stats_dict = lifetime_stats_instance.to_dict()
# create an instance of LifetimeStats from a dict
lifetime_stats_from_dict = LifetimeStats.from_dict(lifetime_stats_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
