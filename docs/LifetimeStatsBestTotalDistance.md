# LifetimeStatsBestTotalDistance

## Properties

| Name         | Type      | Description                                         | Notes      |
| ------------ | --------- | --------------------------------------------------- | ---------- |
| **var_date** | **date**  | The date the user&#39;s best distance was achieved. | [optional] |
| **value**    | **float** | The user&#39;s best distance achieved.              | [optional] |

## Example

```python
from fitbit_web_api.models.lifetime_stats_best_total_distance import LifetimeStatsBestTotalDistance

# TODO update the JSON string below
json = "{}"
# create an instance of LifetimeStatsBestTotalDistance from a JSON string
lifetime_stats_best_total_distance_instance = LifetimeStatsBestTotalDistance.from_json(json)
# print the JSON string representation of the object
print(LifetimeStatsBestTotalDistance.to_json())

# convert the object into a dict
lifetime_stats_best_total_distance_dict = lifetime_stats_best_total_distance_instance.to_dict()
# create an instance of LifetimeStatsBestTotalDistance from a dict
lifetime_stats_best_total_distance_from_dict = LifetimeStatsBestTotalDistance.from_dict(lifetime_stats_best_total_distance_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
