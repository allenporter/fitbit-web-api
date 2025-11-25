# fitbit_web_api.HeartRateTimeSeriesApi

All URIs are relative to *https://api.fitbit.com*

| Method                                                                             | HTTP request                                                        | Description                |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------- | -------------------------- |
| [**get_heart_by_date_period**](HeartRateTimeSeriesApi.md#get_heart_by_date_period) | **GET** /1/user/-/activities/heart/date/{date}/{period}.json        | Get Heart Rate Time Series |
| [**get_heart_by_date_range**](HeartRateTimeSeriesApi.md#get_heart_by_date_range)   | **GET** /1/user/-/activities/heart/date/{base-date}/{end-date}.json | Get Heart Rate Time Series |

# **get_heart_by_date_period**

> GetHeartRateTimeSeriesResponse get_heart_by_date_period(var_date, period)

Get Heart Rate Time Series

Returns the time series data in the specified range for a given resource in the format requested using units in the unit systems that corresponds to the Accept-Language header provided.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_heart_rate_time_series_response import GetHeartRateTimeSeriesResponse
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
    api_instance = fitbit_web_api.HeartRateTimeSeriesApi(api_client)
    var_date = 'var_date_example' # str | The end date of the period specified in the format yyyy-MM-dd or today.
    period = 'period_example' # str | The range of which data will be returned. Options are 1d, 7d, 30d, 1w, and 1m.

    try:
        # Get Heart Rate Time Series
        api_response = await api_instance.get_heart_by_date_period(var_date, period)
        print("The response of HeartRateTimeSeriesApi->get_heart_by_date_period:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeartRateTimeSeriesApi->get_heart_by_date_period: %s\n" % e)
```

### Parameters

| Name         | Type    | Description                                                                    | Notes |
| ------------ | ------- | ------------------------------------------------------------------------------ | ----- |
| **var_date** | **str** | The end date of the period specified in the format yyyy-MM-dd or today.        |
| **period**   | **str** | The range of which data will be returned. Options are 1d, 7d, 30d, 1w, and 1m. |

### Return type

[**GetHeartRateTimeSeriesResponse**](GetHeartRateTimeSeriesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                       | Response headers |
| ----------- | ----------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                             | -                |
| **401**     | The request requires user authentication.                         | -                |
| **403**     | The server understood the request, but is refusing to fulfill it. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heart_by_date_range**

> GetHeartRateTimeSeriesResponse get_heart_by_date_range(base_date, end_date)

Get Heart Rate Time Series

Returns the time series data in the specified range for a given resource in the format requested using units in the unit systems that corresponds to the Accept-Language header provided.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_heart_rate_time_series_response import GetHeartRateTimeSeriesResponse
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
    api_instance = fitbit_web_api.HeartRateTimeSeriesApi(api_client)
    base_date = 'base_date_example' # str | The range start date in  the format yyyy-MM-dd or today.
    end_date = '2013-10-20' # date | The end date of the range.

    try:
        # Get Heart Rate Time Series
        api_response = await api_instance.get_heart_by_date_range(base_date, end_date)
        print("The response of HeartRateTimeSeriesApi->get_heart_by_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeartRateTimeSeriesApi->get_heart_by_date_range: %s\n" % e)
```

### Parameters

| Name          | Type     | Description                                             | Notes |
| ------------- | -------- | ------------------------------------------------------- | ----- |
| **base_date** | **str**  | The range start date in the format yyyy-MM-dd or today. |
| **end_date**  | **date** | The end date of the range.                              |

### Return type

[**GetHeartRateTimeSeriesResponse**](GetHeartRateTimeSeriesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                       | Response headers |
| ----------- | ----------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                             | -                |
| **401**     | The request requires user authentication.                         | -                |
| **403**     | The server understood the request, but is refusing to fulfill it. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
