# fitbit_web_api.TemperatureApi

All URIs are relative to *https://api.fitbit.com*

| Method                                                                                       | HTTP request                                                | Description                                |
| -------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------ |
| [**get_temp_core_summary_by_date**](TemperatureApi.md#get_temp_core_summary_by_date)         | **GET** /1/user/-/temp/core/date/{date}.json                | Get Temperature (Core) Summary by Date     |
| [**get_temp_core_summary_by_interval**](TemperatureApi.md#get_temp_core_summary_by_interval) | **GET** /1/user/-/temp/core/date/{startDate}/{endDate}.json | Get Temperature (Core) Summary by Interval |
| [**get_temp_skin_summary_by_interval**](TemperatureApi.md#get_temp_skin_summary_by_interval) | **GET** /1/user/-/temp/skin/date/{startDate}/{endDate}.json | Get Temperature (Skin) Summary by Interval |
| [**get_temp_skin_summary_date**](TemperatureApi.md#get_temp_skin_summary_date)               | **GET** /1/user/-/temp/skin/date/{date}.json                | Get Temperature (Skin) Summary by Date     |

# **get_temp_core_summary_by_date**

> GetTemperatureCoreSummaryResponse get_temp_core_summary_by_date(var_date)

Get Temperature (Core) Summary by Date

Returns the Temperature (Core) data for a single date. Temperature (Core) data applies specifically to data logged manually by the user throughout the day.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_temperature_core_summary_response import GetTemperatureCoreSummaryResponse
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
    api_instance = fitbit_web_api.TemperatureApi(api_client)
    var_date = 'var_date_example' # str | The date in the format of yyyy-MM-dd or today.

    try:
        # Get Temperature (Core) Summary by Date
        api_response = await api_instance.get_temp_core_summary_by_date(var_date)
        print("The response of TemperatureApi->get_temp_core_summary_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemperatureApi->get_temp_core_summary_by_date: %s\n" % e)
```

### Parameters

| Name         | Type    | Description                                    | Notes |
| ------------ | ------- | ---------------------------------------------- | ----- |
| **var_date** | **str** | The date in the format of yyyy-MM-dd or today. |

### Return type

[**GetTemperatureCoreSummaryResponse**](GetTemperatureCoreSummaryResponse.md)

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

# **get_temp_core_summary_by_interval**

> GetTemperatureCoreSummaryResponse get_temp_core_summary_by_interval(start_date, end_date)

Get Temperature (Core) Summary by Interval

Returns Temperature (Core) data for a date range. Temperature (Core) data applies specifically to data logged manually by the user throughout the day and the maximum date range cannot exceed 30 days.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_temperature_core_summary_response import GetTemperatureCoreSummaryResponse
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
    api_instance = fitbit_web_api.TemperatureApi(api_client)
    start_date = 'start_date_example' # str | The date in the format of yyyy-MM-dd or today.
    end_date = 'end_date_example' # str | The date in the format of yyyy-MM-dd or today.

    try:
        # Get Temperature (Core) Summary by Interval
        api_response = await api_instance.get_temp_core_summary_by_interval(start_date, end_date)
        print("The response of TemperatureApi->get_temp_core_summary_by_interval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemperatureApi->get_temp_core_summary_by_interval: %s\n" % e)
```

### Parameters

| Name           | Type    | Description                                    | Notes |
| -------------- | ------- | ---------------------------------------------- | ----- |
| **start_date** | **str** | The date in the format of yyyy-MM-dd or today. |
| **end_date**   | **str** | The date in the format of yyyy-MM-dd or today. |

### Return type

[**GetTemperatureCoreSummaryResponse**](GetTemperatureCoreSummaryResponse.md)

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

# **get_temp_skin_summary_by_interval**

> GetTemperatureSkinSummaryResponse get_temp_skin_summary_by_interval(start_date, end_date)

Get Temperature (Skin) Summary by Interval

Returns Temperature (Skin) data for a date range. It only returns a value for dates on which the Fitbit device was able to record Temperature (skin) data and the maximum date range cannot exceed 30 days.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_temperature_skin_summary_response import GetTemperatureSkinSummaryResponse
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
    api_instance = fitbit_web_api.TemperatureApi(api_client)
    start_date = 'start_date_example' # str | The date in the format of yyyy-MM-dd or today.
    end_date = 'end_date_example' # str | The date in the format of yyyy-MM-dd or today.

    try:
        # Get Temperature (Skin) Summary by Interval
        api_response = await api_instance.get_temp_skin_summary_by_interval(start_date, end_date)
        print("The response of TemperatureApi->get_temp_skin_summary_by_interval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemperatureApi->get_temp_skin_summary_by_interval: %s\n" % e)
```

### Parameters

| Name           | Type    | Description                                    | Notes |
| -------------- | ------- | ---------------------------------------------- | ----- |
| **start_date** | **str** | The date in the format of yyyy-MM-dd or today. |
| **end_date**   | **str** | The date in the format of yyyy-MM-dd or today. |

### Return type

[**GetTemperatureSkinSummaryResponse**](GetTemperatureSkinSummaryResponse.md)

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

# **get_temp_skin_summary_date**

> GetTemperatureSkinSummaryResponse get_temp_skin_summary_date(var_date)

Get Temperature (Skin) Summary by Date

Returns the Temperature (Skin) data for a single date. Temperature (Skin) data applies specifically to a user’s “main sleep”, which is the longest single period of time asleep on a given date.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_temperature_skin_summary_response import GetTemperatureSkinSummaryResponse
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
    api_instance = fitbit_web_api.TemperatureApi(api_client)
    var_date = 'var_date_example' # str | The date in the format of yyyy-MM-dd or today.

    try:
        # Get Temperature (Skin) Summary by Date
        api_response = await api_instance.get_temp_skin_summary_date(var_date)
        print("The response of TemperatureApi->get_temp_skin_summary_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemperatureApi->get_temp_skin_summary_date: %s\n" % e)
```

### Parameters

| Name         | Type    | Description                                    | Notes |
| ------------ | ------- | ---------------------------------------------- | ----- |
| **var_date** | **str** | The date in the format of yyyy-MM-dd or today. |

### Return type

[**GetTemperatureSkinSummaryResponse**](GetTemperatureSkinSummaryResponse.md)

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
