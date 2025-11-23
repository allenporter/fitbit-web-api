# Device

## Properties

| Name               | Type          | Description                                                                                        | Notes      |
| ------------------ | ------------- | -------------------------------------------------------------------------------------------------- | ---------- |
| **battery**        | **str**       | Returns the battery level of the device.                                                           | [optional] |
| **battery_level**  | **int**       | Returns the battery level percentage of the device.                                                | [optional] |
| **device_version** | **str**       | The product name of the device.                                                                    | [optional] |
| **features**       | **List[str]** | Lists any unique features supported by the device.                                                 | [optional] |
| **id**             | **str**       | The device ID.                                                                                     | [optional] |
| **last_sync_time** | **datetime**  | Timestamp representing the last time the device was sync&#39;d with the Fitbit mobile application. | [optional] |
| **mac**            | **str**       | Mac ID number                                                                                      | [optional] |
| **type**           | **str**       | The type of device.                                                                                | [optional] |

## Example

```python
from fitbit_web_api.models.device import Device

# TODO update the JSON string below
json = "{}"
# create an instance of Device from a JSON string
device_instance = Device.from_json(json)
# print the JSON string representation of the object
print(Device.to_json())

# convert the object into a dict
device_dict = device_instance.to_dict()
# create an instance of Device from a dict
device_from_dict = Device.from_dict(device_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
