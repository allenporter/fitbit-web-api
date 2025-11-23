# TemperatureSkinLogValue

## Properties

| Name                 | Type      | Description                                                  | Notes      |
| -------------------- | --------- | ------------------------------------------------------------ | ---------- |
| **nightly_relative** | **float** | The user&#39;s average temperature during a period of sleep. | [optional] |

## Example

```python
from fitbit_web_api.models.temperature_skin_log_value import TemperatureSkinLogValue

# TODO update the JSON string below
json = "{}"
# create an instance of TemperatureSkinLogValue from a JSON string
temperature_skin_log_value_instance = TemperatureSkinLogValue.from_json(json)
# print the JSON string representation of the object
print(TemperatureSkinLogValue.to_json())

# convert the object into a dict
temperature_skin_log_value_dict = temperature_skin_log_value_instance.to_dict()
# create an instance of TemperatureSkinLogValue from a dict
temperature_skin_log_value_from_dict = TemperatureSkinLogValue.from_dict(temperature_skin_log_value_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
