# fitbit_web_api.NutritionTimeSeriesApi

All URIs are relative to *https://api.fitbit.com*

| Method                                                                                               | HTTP request                                                                 | Description                   |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ----------------------------- |
| [**get_foods_by_date_range**](NutritionTimeSeriesApi.md#get_foods_by_date_range)                     | **GET** /1/user/-/foods/log/{resource-path}/date/{base-date}/{end-date}.json | Get Food or Water Time Series |
| [**get_foods_resource_by_date_period**](NutritionTimeSeriesApi.md#get_foods_resource_by_date_period) | **GET** /1/user/-/foods/log/{resource-path}/date/{date}/{period}.json        | Get Food or Water Time Series |

# **get_foods_by_date_range**

> GetNutritionTimeSeriesResponse get_foods_by_date_range(var_resource_path, base_date, end_date)

Get Food or Water Time Series

Updates a user's daily activity goals and returns a response using units in the unit system which corresponds to the Accept-Language header provided.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_nutrition_time_series_response import GetNutritionTimeSeriesResponse
from fitbit_web_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fitbit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fitbit_web_api.Configuration(
    host = "https://api.fitbit.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with fitbit_web_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fitbit_web_api.NutritionTimeSeriesApi(api_client)
    var_resource_path = caloriesIn # str | The resouce path. See options in the Resouce Path Options section in the full documentation. (default to caloriesIn)
    base_date = 'base_date_example' # str | The range start date in the format yyyy-MM-dd or today.
    end_date = '2013-10-20' # date | The end date of the range.

    try:
        # Get Food or Water Time Series
        api_response = await api_instance.get_foods_by_date_range(var_resource_path, base_date, end_date)
        print("The response of NutritionTimeSeriesApi->get_foods_by_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NutritionTimeSeriesApi->get_foods_by_date_range: %s\n" % e)
```

### Parameters

| Name                  | Type     | Description                                                                                  | Notes                   |
| --------------------- | -------- | -------------------------------------------------------------------------------------------- | ----------------------- |
| **var_resource_path** | **str**  | The resouce path. See options in the Resouce Path Options section in the full documentation. | [default to caloriesIn] |
| **base_date**         | **str**  | The range start date in the format yyyy-MM-dd or today.                                      |
| **end_date**          | **date** | The end date of the range.                                                                   |

### Return type

[**GetNutritionTimeSeriesResponse**](GetNutritionTimeSeriesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                             | Response headers |
| ----------- | ----------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                   | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified. | -                |
| **401**     | The request requires user authentication.                               | -                |
| **403**     | The server understood the request, but is refusing to fulfill it.       | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_foods_resource_by_date_period**

> GetNutritionTimeSeriesResponse get_foods_resource_by_date_period(var_resource_path, var_date, period)

Get Food or Water Time Series

Updates a user's daily activity goals and returns a response using units in the unit system which corresponds to the Accept-Language header provided.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_nutrition_time_series_response import GetNutritionTimeSeriesResponse
from fitbit_web_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fitbit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fitbit_web_api.Configuration(
    host = "https://api.fitbit.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with fitbit_web_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fitbit_web_api.NutritionTimeSeriesApi(api_client)
    var_resource_path = caloriesIn # str | The resouce path. See options in the Resouce Path Options section in the full documentation. (default to caloriesIn)
    var_date = 'var_date_example' # str | The end date of the period specified in the format yyyy-MM-dd or today.
    period = 'period_example' # str | The range for which data will be returned. Options are 1d, 7d, 30d, 1w, 3m, 6m, 1y, or max.

    try:
        # Get Food or Water Time Series
        api_response = await api_instance.get_foods_resource_by_date_period(var_resource_path, var_date, period)
        print("The response of NutritionTimeSeriesApi->get_foods_resource_by_date_period:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NutritionTimeSeriesApi->get_foods_resource_by_date_period: %s\n" % e)
```

### Parameters

| Name                  | Type    | Description                                                                                  | Notes                   |
| --------------------- | ------- | -------------------------------------------------------------------------------------------- | ----------------------- |
| **var_resource_path** | **str** | The resouce path. See options in the Resouce Path Options section in the full documentation. | [default to caloriesIn] |
| **var_date**          | **str** | The end date of the period specified in the format yyyy-MM-dd or today.                      |
| **period**            | **str** | The range for which data will be returned. Options are 1d, 7d, 30d, 1w, 3m, 6m, 1y, or max.  |

### Return type

[**GetNutritionTimeSeriesResponse**](GetNutritionTimeSeriesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                             | Response headers |
| ----------- | ----------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                   | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified. | -                |
| **401**     | The request requires user authentication.                               | -                |
| **403**     | The server understood the request, but is refusing to fulfill it.       | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
