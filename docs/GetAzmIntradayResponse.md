# GetAzmIntradayResponse

## Properties

| Name                                        | Type                                                                                                                          | Description | Notes      |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------- |
| **activities_active_zone_minutes**          | [**List[GetAzmIntradayResponseActivitiesActiveZoneMinutesInner]**](GetAzmIntradayResponseActivitiesActiveZoneMinutesInner.md) |             | [optional] |
| **activities_active_zone_minutes_intraday** | [**AzmIntradayDataset**](AzmIntradayDataset.md)                                                                               |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_azm_intraday_response import GetAzmIntradayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAzmIntradayResponse from a JSON string
get_azm_intraday_response_instance = GetAzmIntradayResponse.from_json(json)
# print the JSON string representation of the object
print(GetAzmIntradayResponse.to_json())

# convert the object into a dict
get_azm_intraday_response_dict = get_azm_intraday_response_instance.to_dict()
# create an instance of GetAzmIntradayResponse from a dict
get_azm_intraday_response_from_dict = GetAzmIntradayResponse.from_dict(get_azm_intraday_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
