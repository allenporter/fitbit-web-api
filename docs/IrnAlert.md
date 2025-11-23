# IrnAlert

## Properties

| Name                | Type                                | Description                                                       | Notes      |
| ------------------- | ----------------------------------- | ----------------------------------------------------------------- | ---------- |
| **alert_time**      | **datetime**                        | The start time for the irregular rhythm detection.                | [optional] |
| **detected_time**   | **datetime**                        | The end time for the irregular rhythm detection.                  | [optional] |
| **service_version** | **str**                             | The version of the service running when the alert was produced.   | [optional] |
| **algo_version**    | **str**                             | The version of the algorithm running when the alert was produced. | [optional] |
| **device_type**     | **str**                             | The name of the device who generated the alert.                   | [optional] |
| **windows**         | [**List[IrnWindow]**](IrnWindow.md) | List of analyzable windows.                                       | [optional] |

## Example

```python
from fitbit_web_api.models.irn_alert import IrnAlert

# TODO update the JSON string below
json = "{}"
# create an instance of IrnAlert from a JSON string
irn_alert_instance = IrnAlert.from_json(json)
# print the JSON string representation of the object
print(IrnAlert.to_json())

# convert the object into a dict
irn_alert_dict = irn_alert_instance.to_dict()
# create an instance of IrnAlert from a dict
irn_alert_from_dict = IrnAlert.from_dict(irn_alert_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
