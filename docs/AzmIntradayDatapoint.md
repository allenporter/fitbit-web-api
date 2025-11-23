# AzmIntradayDatapoint

## Properties

| Name      | Type                        | Description                        | Notes      |
| --------- | --------------------------- | ---------------------------------- | ---------- |
| **time**  | **str**                     | The time of the recorded resource. | [optional] |
| **value** | [**AzmValue**](AzmValue.md) |                                    | [optional] |

## Example

```python
from fitbit_web_api.models.azm_intraday_datapoint import AzmIntradayDatapoint

# TODO update the JSON string below
json = "{}"
# create an instance of AzmIntradayDatapoint from a JSON string
azm_intraday_datapoint_instance = AzmIntradayDatapoint.from_json(json)
# print the JSON string representation of the object
print(AzmIntradayDatapoint.to_json())

# convert the object into a dict
azm_intraday_datapoint_dict = azm_intraday_datapoint_instance.to_dict()
# create an instance of AzmIntradayDatapoint from a dict
azm_intraday_datapoint_from_dict = AzmIntradayDatapoint.from_dict(azm_intraday_datapoint_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
