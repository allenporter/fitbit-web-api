# GetAzmIntradayResponseActivitiesActiveZoneMinutesInner

## Properties

| Name          | Type                        | Description | Notes      |
| ------------- | --------------------------- | ----------- | ---------- |
| **date_time** | **date**                    |             | [optional] |
| **value**     | [**AzmValue**](AzmValue.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_azm_intraday_response_activities_active_zone_minutes_inner import GetAzmIntradayResponseActivitiesActiveZoneMinutesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAzmIntradayResponseActivitiesActiveZoneMinutesInner from a JSON string
get_azm_intraday_response_activities_active_zone_minutes_inner_instance = GetAzmIntradayResponseActivitiesActiveZoneMinutesInner.from_json(json)
# print the JSON string representation of the object
print(GetAzmIntradayResponseActivitiesActiveZoneMinutesInner.to_json())

# convert the object into a dict
get_azm_intraday_response_activities_active_zone_minutes_inner_dict = get_azm_intraday_response_activities_active_zone_minutes_inner_instance.to_dict()
# create an instance of GetAzmIntradayResponseActivitiesActiveZoneMinutesInner from a dict
get_azm_intraday_response_activities_active_zone_minutes_inner_from_dict = GetAzmIntradayResponseActivitiesActiveZoneMinutesInner.from_dict(get_azm_intraday_response_activities_active_zone_minutes_inner_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
