# LifetimeStatsBestTotalFloors

## Properties

| Name         | Type      | Description                                       | Notes      |
| ------------ | --------- | ------------------------------------------------- | ---------- |
| **var_date** | **date**  | The date the user&#39;s best floors was achieved. | [optional] |
| **value**    | **float** | The user&#39;s best floors achieved.              | [optional] |

## Example

```python
from fitbit_web_api.models.lifetime_stats_best_total_floors import LifetimeStatsBestTotalFloors

# TODO update the JSON string below
json = "{}"
# create an instance of LifetimeStatsBestTotalFloors from a JSON string
lifetime_stats_best_total_floors_instance = LifetimeStatsBestTotalFloors.from_json(json)
# print the JSON string representation of the object
print(LifetimeStatsBestTotalFloors.to_json())

# convert the object into a dict
lifetime_stats_best_total_floors_dict = lifetime_stats_best_total_floors_instance.to_dict()
# create an instance of LifetimeStatsBestTotalFloors from a dict
lifetime_stats_best_total_floors_from_dict = LifetimeStatsBestTotalFloors.from_dict(lifetime_stats_best_total_floors_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
