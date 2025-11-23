# HeartRateIntradayDataset

## Properties

| Name                 | Type                                                                  | Description                                   | Notes      |
| -------------------- | --------------------------------------------------------------------- | --------------------------------------------- | ---------- |
| **dataset**          | [**List[HeartRateIntradayDatapoint]**](HeartRateIntradayDatapoint.md) |                                               | [optional] |
| **dataset_interval** | **int**                                                               | The requested detail-level numerical interval | [optional] |
| **dataset_type**     | **str**                                                               | The requested detail-level unit of measure    | [optional] |

## Example

```python
from fitbit_web_api.models.heart_rate_intraday_dataset import HeartRateIntradayDataset

# TODO update the JSON string below
json = "{}"
# create an instance of HeartRateIntradayDataset from a JSON string
heart_rate_intraday_dataset_instance = HeartRateIntradayDataset.from_json(json)
# print the JSON string representation of the object
print(HeartRateIntradayDataset.to_json())

# convert the object into a dict
heart_rate_intraday_dataset_dict = heart_rate_intraday_dataset_instance.to_dict()
# create an instance of HeartRateIntradayDataset from a dict
heart_rate_intraday_dataset_from_dict = HeartRateIntradayDataset.from_dict(heart_rate_intraday_dataset_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
