# fitbit_web_api.ActiveZoneMinutesIntradayTimeSeriesApi

All URIs are relative to *https://api.fitbit.com*

| Method                                                                                                                           | HTTP request                                                                                                     | Description                  |
| -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| [**get_azmby_date_intraday**](ActiveZoneMinutesIntradayTimeSeriesApi.md#get_azmby_date_intraday)                                 | **GET** /1/user/-/activities/active-zone-minutes/date/{date}/1d/{detail-level}.json                              | Get AZM Intraday by Date     |
| [**get_azmby_date_time_series_intraday**](ActiveZoneMinutesIntradayTimeSeriesApi.md#get_azmby_date_time_series_intraday)         | **GET** /1/user/-/activities/active-zone-minutes/date/{date}/1d/{detail-level}/time/{start-time}/{end-time}.json | Get AZM Intraday by Date     |
| [**get_azmby_interval_intraday**](ActiveZoneMinutesIntradayTimeSeriesApi.md#get_azmby_interval_intraday)                         | **GET** /1/user/-/activities/active-zone-minutes/date/{start-date}/{end-date}/{detail-level}.json                | Get AZM Intraday by Interval |
| [**get_azmby_interval_time_series_intraday**](ActiveZoneMinutesIntradayTimeSeriesApi.md#get_azmby_interval_time_series_intraday) | **GET** /1/user/-/activities/active-zone-minutes/date/{start-date}/{end-date}/time/{start-time}/{end-time}.json  | Get AZM Intraday by Interval |

# **get_azmby_date_intraday**

> GetAzmIntradayResponse get_azmby_date_intraday(var_date, detail_level)

Get AZM Intraday by Date

Returns the active zone minutes intraday data for a 24 hour period by specifying a date and/or time range.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_azm_intraday_response import GetAzmIntradayResponse
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
    api_instance = fitbit_web_api.ActiveZoneMinutesIntradayTimeSeriesApi(api_client)
    var_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today
    detail_level = 'detail_level_example' # str | The detail for which data will be returned. **Supported:** 1min | 5min | 15min

    try:
        # Get AZM Intraday by Date
        api_response = await api_instance.get_azmby_date_intraday(var_date, detail_level)
        print("The response of ActiveZoneMinutesIntradayTimeSeriesApi->get_azmby_date_intraday:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActiveZoneMinutesIntradayTimeSeriesApi->get_azmby_date_intraday: %s\n" % e)
```

### Parameters

| Name             | Type     | Description                                                     | Notes |
| ---------------- | -------- | --------------------------------------------------------------- | ----- | ----- |
| **var_date**     | **date** | The date in the format yyyy-MM-dd or today                      |
| **detail_level** | **str**  | The detail for which data will be returned. **Supported:** 1min | 5min  | 15min |

### Return type

[**GetAzmIntradayResponse**](GetAzmIntradayResponse.md)

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

# **get_azmby_date_time_series_intraday**

> GetAzmIntradayResponse get_azmby_date_time_series_intraday(var_date, detail_level, start_time, end_time)

Get AZM Intraday by Date

Returns the active zone minutes intraday data for a 24 hour period by specifying a date and/or time range.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_azm_intraday_response import GetAzmIntradayResponse
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
    api_instance = fitbit_web_api.ActiveZoneMinutesIntradayTimeSeriesApi(api_client)
    var_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today
    detail_level = 'detail_level_example' # str | The detail for which data will be returned. **Supported:** 1min | 5min | 15min
    start_time = 'start_time_example' # str | The start of the period in the format HH:mm.
    end_time = 'end_time_example' # str | The end of the period in the format HH:mm.

    try:
        # Get AZM Intraday by Date
        api_response = await api_instance.get_azmby_date_time_series_intraday(var_date, detail_level, start_time, end_time)
        print("The response of ActiveZoneMinutesIntradayTimeSeriesApi->get_azmby_date_time_series_intraday:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActiveZoneMinutesIntradayTimeSeriesApi->get_azmby_date_time_series_intraday: %s\n" % e)
```

### Parameters

| Name             | Type     | Description                                                     | Notes |
| ---------------- | -------- | --------------------------------------------------------------- | ----- | ----- |
| **var_date**     | **date** | The date in the format yyyy-MM-dd or today                      |
| **detail_level** | **str**  | The detail for which data will be returned. **Supported:** 1min | 5min  | 15min |
| **start_time**   | **str**  | The start of the period in the format HH:mm.                    |
| **end_time**     | **str**  | The end of the period in the format HH:mm.                      |

### Return type

[**GetAzmIntradayResponse**](GetAzmIntradayResponse.md)

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

# **get_azmby_interval_intraday**

> GetAzmIntradayResponse get_azmby_interval_intraday(start_date, end_date, detail_level)

Get AZM Intraday by Interval

Returns the active zone minutes intraday data for a 24 hour period by specifying a date range and/or time range.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_azm_intraday_response import GetAzmIntradayResponse
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
    api_instance = fitbit_web_api.ActiveZoneMinutesIntradayTimeSeriesApi(api_client)
    start_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today
    end_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today
    detail_level = 'detail_level_example' # str | The detail for which data will be returned. **Support:** 1min | 5min | 15min

    try:
        # Get AZM Intraday by Interval
        api_response = await api_instance.get_azmby_interval_intraday(start_date, end_date, detail_level)
        print("The response of ActiveZoneMinutesIntradayTimeSeriesApi->get_azmby_interval_intraday:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActiveZoneMinutesIntradayTimeSeriesApi->get_azmby_interval_intraday: %s\n" % e)
```

### Parameters

| Name             | Type     | Description                                                   | Notes |
| ---------------- | -------- | ------------------------------------------------------------- | ----- | ----- |
| **start_date**   | **date** | The date in the format yyyy-MM-dd or today                    |
| **end_date**     | **date** | The date in the format yyyy-MM-dd or today                    |
| **detail_level** | **str**  | The detail for which data will be returned. **Support:** 1min | 5min  | 15min |

### Return type

[**GetAzmIntradayResponse**](GetAzmIntradayResponse.md)

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

# **get_azmby_interval_time_series_intraday**

> GetAzmIntradayResponse get_azmby_interval_time_series_intraday(start_date, end_date, detail_level, start_time, end_time)

Get AZM Intraday by Interval

Returns the active zone minutes intraday data for a 24 hour period by specifying a date range and/or time range.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_azm_intraday_response import GetAzmIntradayResponse
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
    api_instance = fitbit_web_api.ActiveZoneMinutesIntradayTimeSeriesApi(api_client)
    start_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today
    end_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today
    detail_level = 'detail_level_example' # str | The detail for which data will be returned. **Support:** 1min | 5min | 15min
    start_time = 'start_time_example' # str | The start of the period in the format HH:mm.
    end_time = 'end_time_example' # str | The end of the period in the format HH:mm.

    try:
        # Get AZM Intraday by Interval
        api_response = await api_instance.get_azmby_interval_time_series_intraday(start_date, end_date, detail_level, start_time, end_time)
        print("The response of ActiveZoneMinutesIntradayTimeSeriesApi->get_azmby_interval_time_series_intraday:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActiveZoneMinutesIntradayTimeSeriesApi->get_azmby_interval_time_series_intraday: %s\n" % e)
```

### Parameters

| Name             | Type     | Description                                                   | Notes |
| ---------------- | -------- | ------------------------------------------------------------- | ----- | ----- |
| **start_date**   | **date** | The date in the format yyyy-MM-dd or today                    |
| **end_date**     | **date** | The date in the format yyyy-MM-dd or today                    |
| **detail_level** | **str**  | The detail for which data will be returned. **Support:** 1min | 5min  | 15min |
| **start_time**   | **str**  | The start of the period in the format HH:mm.                  |
| **end_time**     | **str**  | The end of the period in the format HH:mm.                    |

### Return type

[**GetAzmIntradayResponse**](GetAzmIntradayResponse.md)

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
