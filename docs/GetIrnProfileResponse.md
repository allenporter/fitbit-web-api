# GetIrnProfileResponse

## Properties

| Name             | Type         | Description                                                                                      | Notes      |
| ---------------- | ------------ | ------------------------------------------------------------------------------------------------ | ---------- |
| **onboarded**    | **bool**     | Whether or not the user has onboarded onto the IRN feature.                                      | [optional] |
| **enrolled**     | **bool**     | Whether or not the user is currently enrolled in having their data processed for IRN alerts.     | [optional] |
| **last_updated** | **datetime** | The timestamp of the last piece of analyzable data synced by the user (displayed as local time). | [optional] |

## Example

```python
from fitbit_web_api.models.get_irn_profile_response import GetIrnProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetIrnProfileResponse from a JSON string
get_irn_profile_response_instance = GetIrnProfileResponse.from_json(json)
# print the JSON string representation of the object
print(GetIrnProfileResponse.to_json())

# convert the object into a dict
get_irn_profile_response_dict = get_irn_profile_response_instance.to_dict()
# create an instance of GetIrnProfileResponse from a dict
get_irn_profile_response_from_dict = GetIrnProfileResponse.from_dict(get_irn_profile_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
