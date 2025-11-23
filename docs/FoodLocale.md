# FoodLocale

## Properties

| Name             | Type     | Description                        | Notes      |
| ---------------- | -------- | ---------------------------------- | ---------- |
| **barcode**      | **bool** | Whether barcode is supported.      | [optional] |
| **image_upload** | **bool** | Whether image upload is supported. | [optional] |
| **label**        | **str**  | Name of the locale.                | [optional] |
| **value**        | **str**  | The locale value.                  | [optional] |

## Example

```python
from fitbit_web_api.models.food_locale import FoodLocale

# TODO update the JSON string below
json = "{}"
# create an instance of FoodLocale from a JSON string
food_locale_instance = FoodLocale.from_json(json)
# print the JSON string representation of the object
print(FoodLocale.to_json())

# convert the object into a dict
food_locale_dict = food_locale_instance.to_dict()
# create an instance of FoodLocale from a dict
food_locale_from_dict = FoodLocale.from_dict(food_locale_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
