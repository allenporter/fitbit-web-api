# WaterLog

## Properties

| Name       | Type    | Description                                          | Notes      |
| ---------- | ------- | ---------------------------------------------------- | ---------- |
| **amount** | **int** | Amount of water consumed for each period of the day. | [optional] |
| **log_id** | **int** | The water log ID.                                    | [optional] |

## Example

```python
from fitbit_web_api.models.water_log import WaterLog

# TODO update the JSON string below
json = "{}"
# create an instance of WaterLog from a JSON string
water_log_instance = WaterLog.from_json(json)
# print the JSON string representation of the object
print(WaterLog.to_json())

# convert the object into a dict
water_log_dict = water_log_instance.to_dict()
# create an instance of WaterLog from a dict
water_log_from_dict = WaterLog.from_dict(water_log_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
