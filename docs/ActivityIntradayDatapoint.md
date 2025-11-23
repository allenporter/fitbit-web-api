# ActivityIntradayDatapoint

## Properties

| Name      | Type      | Description                                                                                                                                                                                                                                             | Notes      |
| --------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **time**  | **str**   | The time of the recorded resource.                                                                                                                                                                                                                      | [optional] |
| **value** | **float** | The specified resource&#39;s value at the time it is recorded.                                                                                                                                                                                          | [optional] |
| **level** | **int**   | Numerical value representing the user&#39;s activity-level at the moment when the resource was recorded. 0 &#x3D; sedentary 1 &#x3D; lightly active 2 &#x3D; fairly/moderately active 3 &#x3D; very active Returned only when resource &#x3D; calories. | [optional] |
| **mets**  | **int**   | METs value at the moment when the resource was recorded. Returned only when resource &#x3D; calories.                                                                                                                                                   | [optional] |

## Example

```python
from fitbit_web_api.models.activity_intraday_datapoint import ActivityIntradayDatapoint

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityIntradayDatapoint from a JSON string
activity_intraday_datapoint_instance = ActivityIntradayDatapoint.from_json(json)
# print the JSON string representation of the object
print(ActivityIntradayDatapoint.to_json())

# convert the object into a dict
activity_intraday_datapoint_dict = activity_intraday_datapoint_instance.to_dict()
# create an instance of ActivityIntradayDatapoint from a dict
activity_intraday_datapoint_from_dict = ActivityIntradayDatapoint.from_dict(activity_intraday_datapoint_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
