# BodyFatLog

## Properties

| Name         | Type      | Description                                       | Notes      |
| ------------ | --------- | ------------------------------------------------- | ---------- |
| **var_date** | **date**  | The date the body fat log was recorded.           | [optional] |
| **fat**      | **float** | The body fat percentage.                          | [optional] |
| **log_id**   | **int**   | The body fat log Id.                              | [optional] |
| **source**   | **str**   | The location where the body fat data originated.  | [optional] |
| **time**     | **str**   | The timestamp when the body fat log was recorded. | [optional] |

## Example

```python
from fitbit_web_api.models.body_fat_log import BodyFatLog

# TODO update the JSON string below
json = "{}"
# create an instance of BodyFatLog from a JSON string
body_fat_log_instance = BodyFatLog.from_json(json)
# print the JSON string representation of the object
print(BodyFatLog.to_json())

# convert the object into a dict
body_fat_log_dict = body_fat_log_instance.to_dict()
# create an instance of BodyFatLog from a dict
body_fat_log_from_dict = BodyFatLog.from_dict(body_fat_log_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
