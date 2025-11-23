# Vo2MaxValue

## Properties

| Name        | Type    | Description                                    | Notes      |
| ----------- | ------- | ---------------------------------------------- | ---------- |
| **vo2_max** | **str** | The displayable value of VO2 Max in mL/kg/min. | [optional] |

## Example

```python
from fitbit_web_api.models.vo2_max_value import Vo2MaxValue

# TODO update the JSON string below
json = "{}"
# create an instance of Vo2MaxValue from a JSON string
vo2_max_value_instance = Vo2MaxValue.from_json(json)
# print the JSON string representation of the object
print(Vo2MaxValue.to_json())

# convert the object into a dict
vo2_max_value_dict = vo2_max_value_instance.to_dict()
# create an instance of Vo2MaxValue from a dict
vo2_max_value_from_dict = Vo2MaxValue.from_dict(vo2_max_value_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
