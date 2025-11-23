# ActivityIntradayDataset

## Properties

| Name                 | Type                                                                | Description                                   | Notes      |
| -------------------- | ------------------------------------------------------------------- | --------------------------------------------- | ---------- |
| **dataset**          | [**List[ActivityIntradayDatapoint]**](ActivityIntradayDatapoint.md) |                                               | [optional] |
| **dataset_interval** | **int**                                                             | The requested detail-level numerical interval | [optional] |
| **dataset_type**     | **str**                                                             | The requested detail-level unit of measure    | [optional] |

## Example

```python
from fitbit_web_api.models.activity_intraday_dataset import ActivityIntradayDataset

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityIntradayDataset from a JSON string
activity_intraday_dataset_instance = ActivityIntradayDataset.from_json(json)
# print the JSON string representation of the object
print(ActivityIntradayDataset.to_json())

# convert the object into a dict
activity_intraday_dataset_dict = activity_intraday_dataset_instance.to_dict()
# create an instance of ActivityIntradayDataset from a dict
activity_intraday_dataset_from_dict = ActivityIntradayDataset.from_dict(activity_intraday_dataset_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
