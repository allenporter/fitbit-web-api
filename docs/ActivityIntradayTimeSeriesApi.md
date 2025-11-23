# fitbit_web_api.ActivityIntradayTimeSeriesApi

All URIs are relative to *https://api.fitbit.com*

| Method                                                                                                                                                        | HTTP request                                                                                                         | Description                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| [**get_activities_resource_by_date_intraday**](ActivityIntradayTimeSeriesApi.md#get_activities_resource_by_date_intraday)                                     | **GET** /1/user/-/activities/{resource-path}/date/{date}/1d/{detail-level}.json                                      | Get Intraday Time Series          |
| [**get_activities_resource_by_date_range_intraday**](ActivityIntradayTimeSeriesApi.md#get_activities_resource_by_date_range_intraday)                         | **GET** /1/user/-/activities/{resource-path}/date/{base-date}/{end-date}/{detail-level}.json                         | Get Activity Intraday Time Series |
| [**get_activities_resource_by_date_range_time_series_intraday**](ActivityIntradayTimeSeriesApi.md#get_activities_resource_by_date_range_time_series_intraday) | **GET** /1/user/-/activities/{resource-path}/date/{date}/{end-date}/{detail-level}/time/{start-time}/{end-time}.json | Get Activity Intraday Time Series |
| [**get_activities_resource_by_date_time_series_intraday**](ActivityIntradayTimeSeriesApi.md#get_activities_resource_by_date_time_series_intraday)             | **GET** /1/user/-/activities/{resource-path}/date/{date}/1d/{detail-level}/time/{start-time}/{end-time}.json         | Get Intraday Time Series          |

# **get_activities_resource_by_date_intraday**

> GetActivityIntradayResponse get_activities_resource_by_date_intraday(var_resource_path, var_date, detail_level)

Get Intraday Time Series

Returns the Intraday Time Series for a given resource in the format requested.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_activity_intraday_response import GetActivityIntradayResponse
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
    api_instance = fitbit_web_api.ActivityIntradayTimeSeriesApi(api_client)
    var_resource_path = steps # str | The resource-path; see options in the Resource Path Options section in the full documentation. (default to steps)
    var_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today.
    detail_level = '1min' # str | Number of data points to include. Either 1min or 15min. Optional. (default to '1min')

    try:
        # Get Intraday Time Series
        api_response = await api_instance.get_activities_resource_by_date_intraday(var_resource_path, var_date, detail_level)
        print("The response of ActivityIntradayTimeSeriesApi->get_activities_resource_by_date_intraday:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityIntradayTimeSeriesApi->get_activities_resource_by_date_intraday: %s\n" % e)
```

### Parameters

| Name                  | Type     | Description                                                                                    | Notes                       |
| --------------------- | -------- | ---------------------------------------------------------------------------------------------- | --------------------------- |
| **var_resource_path** | **str**  | The resource-path; see options in the Resource Path Options section in the full documentation. | [default to steps]          |
| **var_date**          | **date** | The date in the format yyyy-MM-dd or today.                                                    |
| **detail_level**      | **str**  | Number of data points to include. Either 1min or 15min. Optional.                              | [default to &#39;1min&#39;] |

### Return type

[**GetActivityIntradayResponse**](GetActivityIntradayResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                                                                                                                          | Response headers |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                                                                                                                                                | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified.                                                                                                                              | -                |
| **401**     | The request requires user authentication.                                                                                                                                                            | -                |
| **409**     | Returned if the given user is already subscribed to this stream using a different subscription ID, OR if the given subscription ID is already used to identify a subscription to a different stream. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activities_resource_by_date_range_intraday**

> GetActivityIntradayResponse get_activities_resource_by_date_range_intraday(var_resource_path, base_date, end_date, detail_level)

Get Activity Intraday Time Series

Returns the Activity Intraday Time Series for a given resource in the format requested.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_activity_intraday_response import GetActivityIntradayResponse
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
    api_instance = fitbit_web_api.ActivityIntradayTimeSeriesApi(api_client)
    var_resource_path = steps # str | The resource-path; see options in the Resource Path Options section in the full documentation. (default to steps)
    base_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today.
    end_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today.
    detail_level = '1min' # str | Number of data points to include. Either 1min or 15min. Optional. (default to '1min')

    try:
        # Get Activity Intraday Time Series
        api_response = await api_instance.get_activities_resource_by_date_range_intraday(var_resource_path, base_date, end_date, detail_level)
        print("The response of ActivityIntradayTimeSeriesApi->get_activities_resource_by_date_range_intraday:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityIntradayTimeSeriesApi->get_activities_resource_by_date_range_intraday: %s\n" % e)
```

### Parameters

| Name                  | Type     | Description                                                                                    | Notes                       |
| --------------------- | -------- | ---------------------------------------------------------------------------------------------- | --------------------------- |
| **var_resource_path** | **str**  | The resource-path; see options in the Resource Path Options section in the full documentation. | [default to steps]          |
| **base_date**         | **date** | The date in the format yyyy-MM-dd or today.                                                    |
| **end_date**          | **date** | The date in the format yyyy-MM-dd or today.                                                    |
| **detail_level**      | **str**  | Number of data points to include. Either 1min or 15min. Optional.                              | [default to &#39;1min&#39;] |

### Return type

[**GetActivityIntradayResponse**](GetActivityIntradayResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                                                                                                                          | Response headers |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                                                                                                                                                | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified.                                                                                                                              | -                |
| **401**     | The request requires user authentication.                                                                                                                                                            | -                |
| **409**     | Returned if the given user is already subscribed to this stream using a different subscription ID, OR if the given subscription ID is already used to identify a subscription to a different stream. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activities_resource_by_date_range_time_series_intraday**

> GetActivityIntradayResponse get_activities_resource_by_date_range_time_series_intraday(var_resource_path, var_date, end_date, detail_level, start_time, end_time)

Get Activity Intraday Time Series

Returns the Intraday Time Series for a given resource in the format requested.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_activity_intraday_response import GetActivityIntradayResponse
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
    api_instance = fitbit_web_api.ActivityIntradayTimeSeriesApi(api_client)
    var_resource_path = steps # str | The resource-path; see options in the Resource Path Options section in the full documentation. (default to steps)
    var_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today.
    end_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today.
    detail_level = '1min' # str | Number of data points to include. Either 1min or 15min. (default to '1min')
    start_time = 'start_time_example' # str | The start of the period in the format HH:mm.
    end_time = 'end_time_example' # str | The end of the period in the format HH:mm.

    try:
        # Get Activity Intraday Time Series
        api_response = await api_instance.get_activities_resource_by_date_range_time_series_intraday(var_resource_path, var_date, end_date, detail_level, start_time, end_time)
        print("The response of ActivityIntradayTimeSeriesApi->get_activities_resource_by_date_range_time_series_intraday:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityIntradayTimeSeriesApi->get_activities_resource_by_date_range_time_series_intraday: %s\n" % e)
```

### Parameters

| Name                  | Type     | Description                                                                                    | Notes                       |
| --------------------- | -------- | ---------------------------------------------------------------------------------------------- | --------------------------- |
| **var_resource_path** | **str**  | The resource-path; see options in the Resource Path Options section in the full documentation. | [default to steps]          |
| **var_date**          | **date** | The date in the format yyyy-MM-dd or today.                                                    |
| **end_date**          | **date** | The date in the format yyyy-MM-dd or today.                                                    |
| **detail_level**      | **str**  | Number of data points to include. Either 1min or 15min.                                        | [default to &#39;1min&#39;] |
| **start_time**        | **str**  | The start of the period in the format HH:mm.                                                   |
| **end_time**          | **str**  | The end of the period in the format HH:mm.                                                     |

### Return type

[**GetActivityIntradayResponse**](GetActivityIntradayResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                                                                                                                          | Response headers |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                                                                                                                                                | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified.                                                                                                                              | -                |
| **401**     | The request requires user authentication.                                                                                                                                                            | -                |
| **409**     | Returned if the given user is already subscribed to this stream using a different subscription ID, OR if the given subscription ID is already used to identify a subscription to a different stream. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activities_resource_by_date_time_series_intraday**

> GetActivityIntradayResponse get_activities_resource_by_date_time_series_intraday(var_resource_path, var_date, detail_level, start_time, end_time)

Get Intraday Time Series

Returns the Intraday Time Series for a given resource in the format requested.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_activity_intraday_response import GetActivityIntradayResponse
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
    api_instance = fitbit_web_api.ActivityIntradayTimeSeriesApi(api_client)
    var_resource_path = steps # str | The resource-path; see options in the Resource Path Options section in the full documentation. (default to steps)
    var_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today.
    detail_level = '1min' # str | Number of data points to include. Either 1min or 15min. (default to '1min')
    start_time = 'start_time_example' # str | The start of the period in the format HH:mm.
    end_time = 'end_time_example' # str | The end of the period in the format HH:mm.

    try:
        # Get Intraday Time Series
        api_response = await api_instance.get_activities_resource_by_date_time_series_intraday(var_resource_path, var_date, detail_level, start_time, end_time)
        print("The response of ActivityIntradayTimeSeriesApi->get_activities_resource_by_date_time_series_intraday:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityIntradayTimeSeriesApi->get_activities_resource_by_date_time_series_intraday: %s\n" % e)
```

### Parameters

| Name                  | Type     | Description                                                                                    | Notes                       |
| --------------------- | -------- | ---------------------------------------------------------------------------------------------- | --------------------------- |
| **var_resource_path** | **str**  | The resource-path; see options in the Resource Path Options section in the full documentation. | [default to steps]          |
| **var_date**          | **date** | The date in the format yyyy-MM-dd or today.                                                    |
| **detail_level**      | **str**  | Number of data points to include. Either 1min or 15min.                                        | [default to &#39;1min&#39;] |
| **start_time**        | **str**  | The start of the period in the format HH:mm.                                                   |
| **end_time**          | **str**  | The end of the period in the format HH:mm.                                                     |

### Return type

[**GetActivityIntradayResponse**](GetActivityIntradayResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                                                                                                                          | Response headers |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                                                                                                                                                | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified.                                                                                                                              | -                |
| **401**     | The request requires user authentication.                                                                                                                                                            | -                |
| **409**     | Returned if the given user is already subscribed to this stream using a different subscription ID, OR if the given subscription ID is already used to identify a subscription to a different stream. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
