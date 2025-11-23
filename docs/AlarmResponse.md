# AlarmResponse

## Properties

| Name              | Type                  | Description | Notes      |
| ----------------- | --------------------- | ----------- | ---------- |
| **tracker_alarm** | [**Alarm**](Alarm.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.alarm_response import AlarmResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmResponse from a JSON string
alarm_response_instance = AlarmResponse.from_json(json)
# print the JSON string representation of the object
print(AlarmResponse.to_json())

# convert the object into a dict
alarm_response_dict = alarm_response_instance.to_dict()
# create an instance of AlarmResponse from a dict
alarm_response_from_dict = AlarmResponse.from_dict(alarm_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
