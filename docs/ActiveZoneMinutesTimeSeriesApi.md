# fitbit_web_api.ActiveZoneMinutesTimeSeriesApi

All URIs are relative to *https://api.fitbit.com*

| Method                                                                                                   | HTTP request                                                                       | Description                     |
| -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------- |
| [**get_azm_time_series_by_date**](ActiveZoneMinutesTimeSeriesApi.md#get_azm_time_series_by_date)         | **GET** /1/user/-/activities/active-zone-minutes/date/{date}/{period}.json         | Get AZM Time Series by Date     |
| [**get_azm_time_series_by_interval**](ActiveZoneMinutesTimeSeriesApi.md#get_azm_time_series_by_interval) | **GET** /1/user/-/activities/active-zone-minutes/date/{start-date}/{end-date}.json | Get AZM Time Series by Interval |

# **get_azm_time_series_by_date**

> GetAzmTimeSeriesResponse get_azm_time_series_by_date(var_date, period)

Get AZM Time Series by Date

Returns the daily summary values over a period of time by specifying a date and time period.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_azm_time_series_response import GetAzmTimeSeriesResponse
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
    api_instance = fitbit_web_api.ActiveZoneMinutesTimeSeriesApi(api_client)
    var_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today
    period = 'period_example' # str | The range for which data will be returned. **Supported:** 1d | 7d | 30d | 1w | 1m | 3m | 6m | 1y

    try:
        # Get AZM Time Series by Date
        api_response = await api_instance.get_azm_time_series_by_date(var_date, period)
        print("The response of ActiveZoneMinutesTimeSeriesApi->get_azm_time_series_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActiveZoneMinutesTimeSeriesApi->get_azm_time_series_by_date: %s\n" % e)
```

### Parameters

| Name         | Type     | Description                                                  | Notes |
| ------------ | -------- | ------------------------------------------------------------ | ----- | --- | --- | --- | --- | --- | --- |
| **var_date** | **date** | The date in the format yyyy-MM-dd or today                   |
| **period**   | **str**  | The range for which data will be returned. **Supported:** 1d | 7d    | 30d | 1w  | 1m  | 3m  | 6m  | 1y  |

### Return type

[**GetAzmTimeSeriesResponse**](GetAzmTimeSeriesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                  | Response headers |
| ----------- | ---------------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                        | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified.      | -                |
| **401**     | The request requires user authentication.                                    | -                |
| **403**     | The API client is not authorized by Fitbit to access the resource requested. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_azm_time_series_by_interval**

> GetAzmTimeSeriesResponse get_azm_time_series_by_interval(start_date, end_date)

Get AZM Time Series by Interval

Returns the daily summary values over an interval by specifying a date range.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_azm_time_series_response import GetAzmTimeSeriesResponse
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
    api_instance = fitbit_web_api.ActiveZoneMinutesTimeSeriesApi(api_client)
    start_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today
    end_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today

    try:
        # Get AZM Time Series by Interval
        api_response = await api_instance.get_azm_time_series_by_interval(start_date, end_date)
        print("The response of ActiveZoneMinutesTimeSeriesApi->get_azm_time_series_by_interval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActiveZoneMinutesTimeSeriesApi->get_azm_time_series_by_interval: %s\n" % e)
```

### Parameters

| Name           | Type     | Description                                | Notes |
| -------------- | -------- | ------------------------------------------ | ----- |
| **start_date** | **date** | The date in the format yyyy-MM-dd or today |
| **end_date**   | **date** | The date in the format yyyy-MM-dd or today |

### Return type

[**GetAzmTimeSeriesResponse**](GetAzmTimeSeriesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                  | Response headers |
| ----------- | ---------------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                        | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified.      | -                |
| **401**     | The request requires user authentication.                                    | -                |
| **403**     | The API client is not authorized by Fitbit to access the resource requested. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
