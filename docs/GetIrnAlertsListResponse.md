# GetIrnAlertsListResponse

## Properties

| Name           | Type                                                                      | Description         | Notes      |
| -------------- | ------------------------------------------------------------------------- | ------------------- | ---------- |
| **alerts**     | [**List[IrnAlert]**](IrnAlert.md)                                         | List of IRN alerts. | [optional] |
| **pagination** | [**GetEcgLogListResponsePagination**](GetEcgLogListResponsePagination.md) |                     | [optional] |

## Example

```python
from fitbit_web_api.models.get_irn_alerts_list_response import GetIrnAlertsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetIrnAlertsListResponse from a JSON string
get_irn_alerts_list_response_instance = GetIrnAlertsListResponse.from_json(json)
# print the JSON string representation of the object
print(GetIrnAlertsListResponse.to_json())

# convert the object into a dict
get_irn_alerts_list_response_dict = get_irn_alerts_list_response_instance.to_dict()
# create an instance of GetIrnAlertsListResponse from a dict
get_irn_alerts_list_response_from_dict = GetIrnAlertsListResponse.from_dict(get_irn_alerts_list_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
