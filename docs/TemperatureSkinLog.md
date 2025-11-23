# TemperatureSkinLog

## Properties

| Name          | Type                                                      | Description                               | Notes      |
| ------------- | --------------------------------------------------------- | ----------------------------------------- | ---------- |
| **date_time** | **date**                                                  | The log date.                             | [optional] |
| **log_type**  | **str**                                                   | The type of skin temperature log created. | [optional] |
| **value**     | [**TemperatureSkinLogValue**](TemperatureSkinLogValue.md) |                                           | [optional] |

## Example

```python
from fitbit_web_api.models.temperature_skin_log import TemperatureSkinLog

# TODO update the JSON string below
json = "{}"
# create an instance of TemperatureSkinLog from a JSON string
temperature_skin_log_instance = TemperatureSkinLog.from_json(json)
# print the JSON string representation of the object
print(TemperatureSkinLog.to_json())

# convert the object into a dict
temperature_skin_log_dict = temperature_skin_log_instance.to_dict()
# create an instance of TemperatureSkinLog from a dict
temperature_skin_log_from_dict = TemperatureSkinLog.from_dict(temperature_skin_log_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
