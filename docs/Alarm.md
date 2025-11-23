# Alarm

## Properties

| Name                 | Type          | Description                                                    | Notes      |
| -------------------- | ------------- | -------------------------------------------------------------- | ---------- |
| **alarm_id**         | **int**       | Numerical value representing the alarm ID.                     | [optional] |
| **deleted**          | **bool**      | Indicates if an alarm has been deleted.                        | [optional] |
| **enabled**          | **bool**      | Indicates if an alarm is enabled.                              | [optional] |
| **recurring**        | **bool**      | Indicates if an alarm is recurring.                            | [optional] |
| **snooze_count**     | **int**       | Indicates the number of times the alarm will snooze.           | [optional] |
| **snooze_length**    | **int**       | Indicates the time in minutes between snooze periods.          | [optional] |
| **synced_to_device** | **bool**      | Indicates if the alarm is synced to the device.                | [optional] |
| **time**             | **str**       | The time and UTC offset for the specified alarm.               | [optional] |
| **vibe**             | **str**       | Returns the type of vibration configured.                      | [optional] |
| **week_days**        | **List[str]** | Returns the recurring days of the week which the alarm is set. | [optional] |
| **label**            | **str**       | Label or name for the alarm.                                   | [optional] |

## Example

```python
from fitbit_web_api.models.alarm import Alarm

# TODO update the JSON string below
json = "{}"
# create an instance of Alarm from a JSON string
alarm_instance = Alarm.from_json(json)
# print the JSON string representation of the object
print(Alarm.to_json())

# convert the object into a dict
alarm_dict = alarm_instance.to_dict()
# create an instance of Alarm from a dict
alarm_from_dict = Alarm.from_dict(alarm_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
