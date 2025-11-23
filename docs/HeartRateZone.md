# HeartRateZone

## Properties

| Name             | Type      | Description                                                | Notes      |
| ---------------- | --------- | ---------------------------------------------------------- | ---------- |
| **calories_out** | **float** | Number calories burned with the specified heart rate zone. | [optional] |
| **max**          | **int**   | Maximum range for the heart rate zone.                     | [optional] |
| **min**          | **int**   | Minimum range for the heart rate zone.                     | [optional] |
| **minutes**      | **int**   | Number minutes withing the specified heart rate zone.      | [optional] |
| **name**         | **str**   | Name of the heart rate zone.                               | [optional] |

## Example

```python
from fitbit_web_api.models.heart_rate_zone import HeartRateZone

# TODO update the JSON string below
json = "{}"
# create an instance of HeartRateZone from a JSON string
heart_rate_zone_instance = HeartRateZone.from_json(json)
# print the JSON string representation of the object
print(HeartRateZone.to_json())

# convert the object into a dict
heart_rate_zone_dict = heart_rate_zone_instance.to_dict()
# create an instance of HeartRateZone from a dict
heart_rate_zone_from_dict = HeartRateZone.from_dict(heart_rate_zone_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
