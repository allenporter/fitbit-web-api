# TemperatureCoreLog

## Properties

| Name          | Type         | Description            | Notes      |
| ------------- | ------------ | ---------------------- | ---------- |
| **date_time** | **datetime** | The log timestamp.     | [optional] |
| **value**     | **float**    | The temperature value. | [optional] |

## Example

```python
from fitbit_web_api.models.temperature_core_log import TemperatureCoreLog

# TODO update the JSON string below
json = "{}"
# create an instance of TemperatureCoreLog from a JSON string
temperature_core_log_instance = TemperatureCoreLog.from_json(json)
# print the JSON string representation of the object
print(TemperatureCoreLog.to_json())

# convert the object into a dict
temperature_core_log_dict = temperature_core_log_instance.to_dict()
# create an instance of TemperatureCoreLog from a dict
temperature_core_log_from_dict = TemperatureCoreLog.from_dict(temperature_core_log_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
