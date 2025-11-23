# GetActivityIntradayResponse

## Properties

| Name                                     | Type                                                                    | Description | Notes      |
| ---------------------------------------- | ----------------------------------------------------------------------- | ----------- | ---------- |
| **activities_calories**                  | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_calories_intraday**         | [**ActivityIntradayDataset**](ActivityIntradayDataset.md)               |             | [optional] |
| **activities_distance**                  | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_distance_intraday**         | [**ActivityIntradayDataset**](ActivityIntradayDataset.md)               |             | [optional] |
| **activities_elevation**                 | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_elevation_intraday**        | [**ActivityIntradayDataset**](ActivityIntradayDataset.md)               |             | [optional] |
| **activities_floors**                    | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_floors_intraday**           | [**ActivityIntradayDataset**](ActivityIntradayDataset.md)               |             | [optional] |
| **activities_steps**                     | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_steps_intraday**            | [**ActivityIntradayDataset**](ActivityIntradayDataset.md)               |             | [optional] |
| **activities_swimming_strokes**          | [**List[ActivityTimeSeriesDatapoint]**](ActivityTimeSeriesDatapoint.md) |             | [optional] |
| **activities_swimming_strokes_intraday** | [**ActivityIntradayDataset**](ActivityIntradayDataset.md)               |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_activity_intraday_response import GetActivityIntradayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetActivityIntradayResponse from a JSON string
get_activity_intraday_response_instance = GetActivityIntradayResponse.from_json(json)
# print the JSON string representation of the object
print(GetActivityIntradayResponse.to_json())

# convert the object into a dict
get_activity_intraday_response_dict = get_activity_intraday_response_instance.to_dict()
# create an instance of GetActivityIntradayResponse from a dict
get_activity_intraday_response_from_dict = GetActivityIntradayResponse.from_dict(get_activity_intraday_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
