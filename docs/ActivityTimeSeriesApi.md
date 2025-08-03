# fitbit_web_api.ActivityTimeSeriesApi

All URIs are relative to *https://api.fitbit.com*

| Method                                                                                                                        | HTTP request                                                                          | Description                                             |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| [**get_activities_resource_by_date_period**](ActivityTimeSeriesApi.md#get_activities_resource_by_date_period)                 | **GET** /1/user/-/activities/{resource-path}/date/{date}/{period}.json                | Get Activity Time Series                                |
| [**get_activities_resource_by_date_range**](ActivityTimeSeriesApi.md#get_activities_resource_by_date_range)                   | **GET** /1/user/-/activities/{resource-path}/date/{base-date}/{end-date}.json         | Get Activity Resource by Date Range                     |
| [**get_activities_tracker_resource_by_date_period**](ActivityTimeSeriesApi.md#get_activities_tracker_resource_by_date_period) | **GET** /1/user/-/activities/tracker/{resource-path}/date/{date}/{period}.json        | Get Activity Time Series                                |
| [**get_activities_tracker_resource_by_date_range**](ActivityTimeSeriesApi.md#get_activities_tracker_resource_by_date_range)   | **GET** /1/user/-/activities/tracker/{resource-path}/date/{base-date}/{end-date}.json | Get Activity Tracker Resource by Date Range Time Series |

# **get_activities_resource_by_date_period**

> get_activities_resource_by_date_period(var_resource_path, var_date, period)

Get Activity Time Series

Returns time series data in the specified range for a given resource in the format requested using units in the unit system that corresponds to the Accept-Language header provided.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
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
    api_instance = fitbit_web_api.ActivityTimeSeriesApi(api_client)
    var_resource_path = steps # str | The resource-path; see options in the Resource Path Options section in the full documentation. (default to steps)
    var_date = '2013-10-20' # date | The end date of the period specified in the format yyyy-MM-dd or today.
    period = 'period_example' # str | The range for which data will be returned. Options are 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, or max.

    try:
        # Get Activity Time Series
        await api_instance.get_activities_resource_by_date_period(var_resource_path, var_date, period)
    except Exception as e:
        print("Exception when calling ActivityTimeSeriesApi->get_activities_resource_by_date_period: %s\n" % e)
```

### Parameters

| Name                  | Type     | Description                                                                                     | Notes              |
| --------------------- | -------- | ----------------------------------------------------------------------------------------------- | ------------------ |
| **var_resource_path** | **str**  | The resource-path; see options in the Resource Path Options section in the full documentation.  | [default to steps] |
| **var_date**          | **date** | The end date of the period specified in the format yyyy-MM-dd or today.                         |
| **period**            | **str**  | The range for which data will be returned. Options are 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, or max. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details

| Status code | Description                                                                                                                                                                                          | Response headers |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                                                                                                                                                | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified.                                                                                                                              | -                |
| **401**     | The request requires user authentication.                                                                                                                                                            | -                |
| **409**     | Returned if the given user is already subscribed to this stream using a different subscription ID, OR if the given subscription ID is already used to identify a subscription to a different stream. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activities_resource_by_date_range**

> get_activities_resource_by_date_range(var_resource_path, base_date, end_date)

Get Activity Resource by Date Range

Returns activities time series data in the specified range for a given resource.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
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
    api_instance = fitbit_web_api.ActivityTimeSeriesApi(api_client)
    var_resource_path = steps # str | The resource-path; see options in the Resource Path Options section in the full documentation. (default to steps)
    base_date = '2013-10-20' # date | The range start date in the format yyyy-MM-dd or today.
    end_date = '2013-10-20' # date | The end date of the range.

    try:
        # Get Activity Resource by Date Range
        await api_instance.get_activities_resource_by_date_range(var_resource_path, base_date, end_date)
    except Exception as e:
        print("Exception when calling ActivityTimeSeriesApi->get_activities_resource_by_date_range: %s\n" % e)
```

### Parameters

| Name                  | Type     | Description                                                                                    | Notes              |
| --------------------- | -------- | ---------------------------------------------------------------------------------------------- | ------------------ |
| **var_resource_path** | **str**  | The resource-path; see options in the Resource Path Options section in the full documentation. | [default to steps] |
| **base_date**         | **date** | The range start date in the format yyyy-MM-dd or today.                                        |
| **end_date**          | **date** | The end date of the range.                                                                     |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details

| Status code | Description                                                                                                                                                                                          | Response headers |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                                                                                                                                                | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified.                                                                                                                              | -                |
| **401**     | The request requires user authentication.                                                                                                                                                            | -                |
| **409**     | Returned if the given user is already subscribed to this stream using a different subscription ID, OR if the given subscription ID is already used to identify a subscription to a different stream. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activities_tracker_resource_by_date_period**

> get_activities_tracker_resource_by_date_period(var_resource_path, var_date, period)

Get Activity Time Series

Returns time series data in the specified range for a given resource in the format requested using units in the unit system that corresponds to the Accept-Language header provided.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
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
    api_instance = fitbit_web_api.ActivityTimeSeriesApi(api_client)
    var_resource_path = steps # str | The resource-path; see options in the Resource Path Options section in the full documentation. (default to steps)
    var_date = '2013-10-20' # date | The end date of the period specified in the format yyyy-MM-dd or today.
    period = 'period_example' # str | The range for which data will be returned. Options are 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, or max.

    try:
        # Get Activity Time Series
        await api_instance.get_activities_tracker_resource_by_date_period(var_resource_path, var_date, period)
    except Exception as e:
        print("Exception when calling ActivityTimeSeriesApi->get_activities_tracker_resource_by_date_period: %s\n" % e)
```

### Parameters

| Name                  | Type     | Description                                                                                     | Notes              |
| --------------------- | -------- | ----------------------------------------------------------------------------------------------- | ------------------ |
| **var_resource_path** | **str**  | The resource-path; see options in the Resource Path Options section in the full documentation.  | [default to steps] |
| **var_date**          | **date** | The end date of the period specified in the format yyyy-MM-dd or today.                         |
| **period**            | **str**  | The range for which data will be returned. Options are 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, or max. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details

| Status code | Description                                                                                                                                                                                          | Response headers |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                                                                                                                                                | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified.                                                                                                                              | -                |
| **401**     | The request requires user authentication.                                                                                                                                                            | -                |
| **409**     | Returned if the given user is already subscribed to this stream using a different subscription ID, OR if the given subscription ID is already used to identify a subscription to a different stream. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activities_tracker_resource_by_date_range**

> get_activities_tracker_resource_by_date_range(var_resource_path, base_date, end_date)

Get Activity Tracker Resource by Date Range Time Series

Returns time series data in the specified range for a given resource.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
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
    api_instance = fitbit_web_api.ActivityTimeSeriesApi(api_client)
    var_resource_path = steps # str | The resource-path; see options in the Resource Path Options section in the full documentation. (default to steps)
    base_date = '2013-10-20' # date | The range start date in the format yyyy-MM-dd or today.
    end_date = '2013-10-20' # date | The end date of the range.

    try:
        # Get Activity Tracker Resource by Date Range Time Series
        await api_instance.get_activities_tracker_resource_by_date_range(var_resource_path, base_date, end_date)
    except Exception as e:
        print("Exception when calling ActivityTimeSeriesApi->get_activities_tracker_resource_by_date_range: %s\n" % e)
```

### Parameters

| Name                  | Type     | Description                                                                                    | Notes              |
| --------------------- | -------- | ---------------------------------------------------------------------------------------------- | ------------------ |
| **var_resource_path** | **str**  | The resource-path; see options in the Resource Path Options section in the full documentation. | [default to steps] |
| **base_date**         | **date** | The range start date in the format yyyy-MM-dd or today.                                        |
| **end_date**          | **date** | The end date of the range.                                                                     |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details

| Status code | Description                                                                                                                                                                                          | Response headers |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                                                                                                                                                | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified.                                                                                                                              | -                |
| **401**     | The request requires user authentication.                                                                                                                                                            | -                |
| **409**     | Returned if the given user is already subscribed to this stream using a different subscription ID, OR if the given subscription ID is already used to identify a subscription to a different stream. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
