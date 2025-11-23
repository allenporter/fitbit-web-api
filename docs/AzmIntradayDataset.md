# AzmIntradayDataset

## Properties

| Name                 | Type                                                      | Description                                   | Notes      |
| -------------------- | --------------------------------------------------------- | --------------------------------------------- | ---------- |
| **dataset**          | [**List[AzmIntradayDatapoint]**](AzmIntradayDatapoint.md) |                                               | [optional] |
| **dataset_interval** | **int**                                                   | The requested detail-level numerical interval | [optional] |
| **dataset_type**     | **str**                                                   | The requested detail-level unit of measure    | [optional] |

## Example

```python
from fitbit_web_api.models.azm_intraday_dataset import AzmIntradayDataset

# TODO update the JSON string below
json = "{}"
# create an instance of AzmIntradayDataset from a JSON string
azm_intraday_dataset_instance = AzmIntradayDataset.from_json(json)
# print the JSON string representation of the object
print(AzmIntradayDataset.to_json())

# convert the object into a dict
azm_intraday_dataset_dict = azm_intraday_dataset_instance.to_dict()
# create an instance of AzmIntradayDataset from a dict
azm_intraday_dataset_from_dict = AzmIntradayDataset.from_dict(azm_intraday_dataset_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
