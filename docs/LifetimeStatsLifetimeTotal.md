# LifetimeStatsLifetimeTotal

The total lifetime stats including tracker and manual activity log entries.

## Properties

| Name             | Type      | Description                                                               | Notes      |
| ---------------- | --------- | ------------------------------------------------------------------------- | ---------- |
| **active_score** | **int**   | Functionality removed. A response is returned for backward compatibility. | [optional] |
| **calories_out** | **int**   | Functionality removed. A response is returned for backward compatibility. | [optional] |
| **distance**     | **float** | The total distance recorded over the lifetime of the user&#39;s account.  | [optional] |
| **floors**       | **int**   | The total floors recorded over the lifetime of the user&#39;s account.    | [optional] |
| **steps**        | **int**   | The total steps recorded over the lifetime of the user&#39;s account.     | [optional] |

## Example

```python
from fitbit_web_api.models.lifetime_stats_lifetime_total import LifetimeStatsLifetimeTotal

# TODO update the JSON string below
json = "{}"
# create an instance of LifetimeStatsLifetimeTotal from a JSON string
lifetime_stats_lifetime_total_instance = LifetimeStatsLifetimeTotal.from_json(json)
# print the JSON string representation of the object
print(LifetimeStatsLifetimeTotal.to_json())

# convert the object into a dict
lifetime_stats_lifetime_total_dict = lifetime_stats_lifetime_total_instance.to_dict()
# create an instance of LifetimeStatsLifetimeTotal from a dict
lifetime_stats_lifetime_total_from_dict = LifetimeStatsLifetimeTotal.from_dict(lifetime_stats_lifetime_total_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
