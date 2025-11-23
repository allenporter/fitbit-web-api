# fitbit_web_api.HeartRateIntradayTimeSeriesApi

All URIs are relative to *https://api.fitbit.com*

| Method                                                                                                                         | HTTP request                                                                                               | Description                         |
| ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| [**get_heart_by_date_intraday**](HeartRateIntradayTimeSeriesApi.md#get_heart_by_date_intraday)                                 | **GET** /1/user/-/activities/heart/date/{date}/1d/{detail-level}.json                                      | Get Heart Rate Intraday Time Series |
| [**get_heart_by_date_range_intraday**](HeartRateIntradayTimeSeriesApi.md#get_heart_by_date_range_intraday)                     | **GET** /1/user/-/activities/heart/date/{date}/{end-date}/{detail-level}.json                              | Get Heart Rate Intraday Time Series |
| [**get_heart_by_date_range_timestamp_intraday**](HeartRateIntradayTimeSeriesApi.md#get_heart_by_date_range_timestamp_intraday) | **GET** /1/user/-/activities/heart/date/{date}/{end-date}/{detail-level}/time/{start-time}/{end-time}.json | Get Heart Rate Intraday Time Series |
| [**get_heart_by_date_timestamp_intraday**](HeartRateIntradayTimeSeriesApi.md#get_heart_by_date_timestamp_intraday)             | **GET** /1/user/-/activities/heart/date/{date}/1d/{detail-level}/time/{start-time}/{end-time}.json         | Get Heart Rate Intraday Time Series |

# **get_heart_by_date_intraday**

> GetHeartRateIntradayResponse get_heart_by_date_intraday(var_date, detail_level)

Get Heart Rate Intraday Time Series

Returns the intraday time series for a given resource in the format requested. If your application has the appropriate access, your calls to a time series endpoint for a specific day (by using start and end dates on the same day or a period of 1d), the response will include extended intraday values with a one-minute detail level for that day. Unlike other time series calls that allow fetching data of other users, intraday data is available only for and to the authorized user.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_heart_rate_intraday_response import GetHeartRateIntradayResponse
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
    api_instance = fitbit_web_api.HeartRateIntradayTimeSeriesApi(api_client)
    var_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.
    detail_level = '1min' # str | The number of data points to include either 1sec, 1min, 5min or 15min. (default to '1min')

    try:
        # Get Heart Rate Intraday Time Series
        api_response = await api_instance.get_heart_by_date_intraday(var_date, detail_level)
        print("The response of HeartRateIntradayTimeSeriesApi->get_heart_by_date_intraday:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeartRateIntradayTimeSeriesApi->get_heart_by_date_intraday: %s\n" % e)
```

### Parameters

| Name             | Type     | Description                                                            | Notes                       |
| ---------------- | -------- | ---------------------------------------------------------------------- | --------------------------- |
| **var_date**     | **date** | The date in the format of yyyy-MM-dd or today.                         |
| **detail_level** | **str**  | The number of data points to include either 1sec, 1min, 5min or 15min. | [default to &#39;1min&#39;] |

### Return type

[**GetHeartRateIntradayResponse**](GetHeartRateIntradayResponse.md)

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

# **get_heart_by_date_range_intraday**

> GetHeartRateIntradayResponse get_heart_by_date_range_intraday(var_date, end_date, detail_level)

Get Heart Rate Intraday Time Series

Returns the intraday time series for a given resource in the format requested. If your application has the appropriate access, your calls to a time series endpoint for a specific day (by using start and end dates on the same day or a period of 1d), the response will include extended intraday values with a one-minute detail level for that day. Unlike other time series calls that allow fetching data of other users, intraday data is available only for and to the authorized user.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_heart_rate_intraday_response import GetHeartRateIntradayResponse
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
    api_instance = fitbit_web_api.HeartRateIntradayTimeSeriesApi(api_client)
    var_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.
    end_date = '2013-10-20' # date | The end date in the format of yyyy-MM-dd or today.
    detail_level = '1min' # str | The number of data points to include either 1sec, 1min, 5min or 15min. (default to '1min')

    try:
        # Get Heart Rate Intraday Time Series
        api_response = await api_instance.get_heart_by_date_range_intraday(var_date, end_date, detail_level)
        print("The response of HeartRateIntradayTimeSeriesApi->get_heart_by_date_range_intraday:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeartRateIntradayTimeSeriesApi->get_heart_by_date_range_intraday: %s\n" % e)
```

### Parameters

| Name             | Type     | Description                                                            | Notes                       |
| ---------------- | -------- | ---------------------------------------------------------------------- | --------------------------- |
| **var_date**     | **date** | The date in the format of yyyy-MM-dd or today.                         |
| **end_date**     | **date** | The end date in the format of yyyy-MM-dd or today.                     |
| **detail_level** | **str**  | The number of data points to include either 1sec, 1min, 5min or 15min. | [default to &#39;1min&#39;] |

### Return type

[**GetHeartRateIntradayResponse**](GetHeartRateIntradayResponse.md)

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

# **get_heart_by_date_range_timestamp_intraday**

> GetHeartRateIntradayResponse get_heart_by_date_range_timestamp_intraday(var_date, end_date, detail_level, start_time, end_time)

Get Heart Rate Intraday Time Series

Returns the intraday time series for a given resource in the format requested. If your application has the appropriate access, your calls to a time series endpoint for a specific day (by using start and end dates on the same day or a period of 1d), the response will include extended intraday values with a one-minute detail level for that day. Unlike other time series calls that allow fetching data of other users, intraday data is available only for and to the authorized user.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_heart_rate_intraday_response import GetHeartRateIntradayResponse
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
    api_instance = fitbit_web_api.HeartRateIntradayTimeSeriesApi(api_client)
    var_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.
    end_date = '2013-10-20' # date | The end date in the format of yyyy-MM-dd or today.
    detail_level = '1min' # str | The number of data points to include either 1sec, 1min, 5min or 15min. (default to '1min')
    start_time = 'start_time_example' # str | The start of the period in the format of HH:mm.
    end_time = 'end_time_example' # str | The end time of the period in the format of HH:mm.

    try:
        # Get Heart Rate Intraday Time Series
        api_response = await api_instance.get_heart_by_date_range_timestamp_intraday(var_date, end_date, detail_level, start_time, end_time)
        print("The response of HeartRateIntradayTimeSeriesApi->get_heart_by_date_range_timestamp_intraday:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeartRateIntradayTimeSeriesApi->get_heart_by_date_range_timestamp_intraday: %s\n" % e)
```

### Parameters

| Name             | Type     | Description                                                            | Notes                       |
| ---------------- | -------- | ---------------------------------------------------------------------- | --------------------------- |
| **var_date**     | **date** | The date in the format of yyyy-MM-dd or today.                         |
| **end_date**     | **date** | The end date in the format of yyyy-MM-dd or today.                     |
| **detail_level** | **str**  | The number of data points to include either 1sec, 1min, 5min or 15min. | [default to &#39;1min&#39;] |
| **start_time**   | **str**  | The start of the period in the format of HH:mm.                        |
| **end_time**     | **str**  | The end time of the period in the format of HH:mm.                     |

### Return type

[**GetHeartRateIntradayResponse**](GetHeartRateIntradayResponse.md)

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

# **get_heart_by_date_timestamp_intraday**

> GetHeartRateIntradayResponse get_heart_by_date_timestamp_intraday(var_date, detail_level, start_time, end_time)

Get Heart Rate Intraday Time Series

Returns the intraday time series for a given resource in the format requested. If your application has the appropriate access, your calls to a time series endpoint for a specific day (by using start and end dates on the same day or a period of 1d), the response will include extended intraday values with a one-minute detail level for that day. Unlike other time series calls that allow fetching data of other users, intraday data is available only for and to the authorized user.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_heart_rate_intraday_response import GetHeartRateIntradayResponse
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
    api_instance = fitbit_web_api.HeartRateIntradayTimeSeriesApi(api_client)
    var_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.
    detail_level = '1min' # str | The number of data points to include either 1sec, 1min, 5min or 15min. (default to '1min')
    start_time = 'start_time_example' # str | The start of the period in the format of HH:mm.
    end_time = 'end_time_example' # str | The end time of the period in the format of HH:mm.

    try:
        # Get Heart Rate Intraday Time Series
        api_response = await api_instance.get_heart_by_date_timestamp_intraday(var_date, detail_level, start_time, end_time)
        print("The response of HeartRateIntradayTimeSeriesApi->get_heart_by_date_timestamp_intraday:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeartRateIntradayTimeSeriesApi->get_heart_by_date_timestamp_intraday: %s\n" % e)
```

### Parameters

| Name             | Type     | Description                                                            | Notes                       |
| ---------------- | -------- | ---------------------------------------------------------------------- | --------------------------- |
| **var_date**     | **date** | The date in the format of yyyy-MM-dd or today.                         |
| **detail_level** | **str**  | The number of data points to include either 1sec, 1min, 5min or 15min. | [default to &#39;1min&#39;] |
| **start_time**   | **str**  | The start of the period in the format of HH:mm.                        |
| **end_time**     | **str**  | The end time of the period in the format of HH:mm.                     |

### Return type

[**GetHeartRateIntradayResponse**](GetHeartRateIntradayResponse.md)

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
