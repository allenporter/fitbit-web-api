# ActivitySummaryDistancesInner

## Properties

| Name         | Type      | Description                        | Notes      |
| ------------ | --------- | ---------------------------------- | ---------- |
| **activity** | **str**   | The activity name.                 | [optional] |
| **distance** | **float** | The distance traveled for the day. | [optional] |

## Example

```python
from fitbit_web_api.models.activity_summary_distances_inner import ActivitySummaryDistancesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ActivitySummaryDistancesInner from a JSON string
activity_summary_distances_inner_instance = ActivitySummaryDistancesInner.from_json(json)
# print the JSON string representation of the object
print(ActivitySummaryDistancesInner.to_json())

# convert the object into a dict
activity_summary_distances_inner_dict = activity_summary_distances_inner_instance.to_dict()
# create an instance of ActivitySummaryDistancesInner from a dict
activity_summary_distances_inner_from_dict = ActivitySummaryDistancesInner.from_dict(activity_summary_distances_inner_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
