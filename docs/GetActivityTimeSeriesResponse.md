# GetActivityTimeSeriesResponse

## Properties

| Name                                          | Type                                                                    | Description | Notes      |
| --------------------------------------------- | ----------------------------------------------------------------------- | ----------- | ---------- |
| **activities_activity_calories**              | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_calories**                       | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_calories_bmr**                   | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_distance**                       | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_elevation**                      | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_floors**                         | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_minutes_sedentary**              | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_minutes_lightly_active**         | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_minutes_fairly_active**          | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_minutes_very_active**            | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_steps**                          | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_swimming_strokes**               | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_tracker_activity_calories**      | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_tracker_calories**               | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_tracker_distance**               | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_tracker_elevation**              | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_tracker_floors**                 | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_tracker_minutes_sedentary**      | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_tracker_minutes_lightly_active** | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_tracker_minutes_fairly_active**  | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_tracker_minutes_very_active**    | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_tracker_steps**                  | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_activity_time_series_response import GetActivityTimeSeriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetActivityTimeSeriesResponse from a JSON string
get_activity_time_series_response_instance = GetActivityTimeSeriesResponse.from_json(json)
# print the JSON string representation of the object
print(GetActivityTimeSeriesResponse.to_json())

# convert the object into a dict
get_activity_time_series_response_dict = get_activity_time_series_response_instance.to_dict()
# create an instance of GetActivityTimeSeriesResponse from a dict
get_activity_time_series_response_from_dict = GetActivityTimeSeriesResponse.from_dict(get_activity_time_series_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
