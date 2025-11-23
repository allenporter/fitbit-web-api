# IrnWindow

## Properties

| Name           | Type                                  | Description                                                                                                     | Notes      |
| -------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ---------- |
| **start_time** | **datetime**                          | The start time for the analyzable window (representing 5 consecutive minutes of data following the start time). | [optional] |
| **bpm_data**   | [**List[IrnBpmData]**](IrnBpmData.md) | List of heart beat data.                                                                                        | [optional] |

## Example

```python
from fitbit_web_api.models.irn_window import IrnWindow

# TODO update the JSON string below
json = "{}"
# create an instance of IrnWindow from a JSON string
irn_window_instance = IrnWindow.from_json(json)
# print the JSON string representation of the object
print(IrnWindow.to_json())

# convert the object into a dict
irn_window_dict = irn_window_instance.to_dict()
# create an instance of IrnWindow from a dict
irn_window_from_dict = IrnWindow.from_dict(irn_window_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
