# WeightLog

## Properties

| Name         | Type      | Description                                                                        | Notes      |
| ------------ | --------- | ---------------------------------------------------------------------------------- | ---------- |
| **bmi**      | **float** | Calculated BMI.                                                                    | [optional] |
| **var_date** | **date**  | Log entry date.                                                                    | [optional] |
| **log_id**   | **int**   | Weight Log IDs are unique to the user, but not globally unique.                    | [optional] |
| **source**   | **str**   | The source of the weight log.                                                      | [optional] |
| **time**     | **str**   | Time of the measurement.                                                           | [optional] |
| **weight**   | **float** | Weight in the unit system that corresponds to the Accept-Language header provided. | [optional] |

## Example

```python
from fitbit_web_api.models.weight_log import WeightLog

# TODO update the JSON string below
json = "{}"
# create an instance of WeightLog from a JSON string
weight_log_instance = WeightLog.from_json(json)
# print the JSON string representation of the object
print(WeightLog.to_json())

# convert the object into a dict
weight_log_dict = weight_log_instance.to_dict()
# create an instance of WeightLog from a dict
weight_log_from_dict = WeightLog.from_dict(weight_log_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
