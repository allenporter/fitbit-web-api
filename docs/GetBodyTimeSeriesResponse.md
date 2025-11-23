# GetBodyTimeSeriesResponse

## Properties

| Name            | Type                                                            | Description | Notes      |
| --------------- | --------------------------------------------------------------- | ----------- | ---------- |
| **body_bmi**    | [**List[BodyTimeSeriesDatapoint]**](BodyTimeSeriesDatapoint.md) |             | [optional] |
| **body_fat**    | [**List[BodyTimeSeriesDatapoint]**](BodyTimeSeriesDatapoint.md) |             | [optional] |
| **body_weight** | [**List[BodyTimeSeriesDatapoint]**](BodyTimeSeriesDatapoint.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_body_time_series_response import GetBodyTimeSeriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBodyTimeSeriesResponse from a JSON string
get_body_time_series_response_instance = GetBodyTimeSeriesResponse.from_json(json)
# print the JSON string representation of the object
print(GetBodyTimeSeriesResponse.to_json())

# convert the object into a dict
get_body_time_series_response_dict = get_body_time_series_response_instance.to_dict()
# create an instance of GetBodyTimeSeriesResponse from a dict
get_body_time_series_response_from_dict = GetBodyTimeSeriesResponse.from_dict(get_body_time_series_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
