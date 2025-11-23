# GetAlarmsResponse

## Properties

| Name               | Type                        | Description     | Notes      |
| ------------------ | --------------------------- | --------------- | ---------- |
| **tracker_alarms** | [**List[Alarm]**](Alarm.md) | List of alarms. | [optional] |

## Example

```python
from fitbit_web_api.models.get_alarms_response import GetAlarmsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAlarmsResponse from a JSON string
get_alarms_response_instance = GetAlarmsResponse.from_json(json)
# print the JSON string representation of the object
print(GetAlarmsResponse.to_json())

# convert the object into a dict
get_alarms_response_dict = get_alarms_response_instance.to_dict()
# create an instance of GetAlarmsResponse from a dict
get_alarms_response_from_dict = GetAlarmsResponse.from_dict(get_alarms_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
