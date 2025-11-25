# fitbit_web_api.SpO2Api

All URIs are relative to *https://api.fitbit.com*

| Method                                                                        | HTTP request                                           | Description                  |
| ----------------------------------------------------------------------------- | ------------------------------------------------------ | ---------------------------- |
| [**get_sp_o2_summary_by_date**](SpO2Api.md#get_sp_o2_summary_by_date)         | **GET** /1/user/-/spo2/date/{date}.json                | Get SpO2 Summary by Date     |
| [**get_sp_o2_summary_by_interval**](SpO2Api.md#get_sp_o2_summary_by_interval) | **GET** /1/user/-/spo2/date/{startDate}/{endDate}.json | Get SpO2 Summary by Interval |

# **get_sp_o2_summary_by_date**

> GetSpO2SummaryResponse get_sp_o2_summary_by_date(var_date)

Get SpO2 Summary by Date

This endpoint returns the SpO2 summary data for a single date. SpO2 applies specifically to a user’s “main sleep”, which is the longest single period of time asleep on a given date.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_sp_o2_summary_response import GetSpO2SummaryResponse
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
    api_instance = fitbit_web_api.SpO2Api(api_client)
    var_date = 'var_date_example' # str | The date in the format of yyyy-MM-dd or today.

    try:
        # Get SpO2 Summary by Date
        api_response = await api_instance.get_sp_o2_summary_by_date(var_date)
        print("The response of SpO2Api->get_sp_o2_summary_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpO2Api->get_sp_o2_summary_by_date: %s\n" % e)
```

### Parameters

| Name         | Type    | Description                                    | Notes |
| ------------ | ------- | ---------------------------------------------- | ----- |
| **var_date** | **str** | The date in the format of yyyy-MM-dd or today. |

### Return type

[**GetSpO2SummaryResponse**](GetSpO2SummaryResponse.md)

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

# **get_sp_o2_summary_by_interval**

> GetSpO2SummaryResponse get_sp_o2_summary_by_interval(start_date, end_date)

Get SpO2 Summary by Interval

This endpoint returns the SpO2 summary data for a date range. SpO2 applies specifically to a user’s “main sleep”, which is the longest single period of time asleep on a given date.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_sp_o2_summary_response import GetSpO2SummaryResponse
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
    api_instance = fitbit_web_api.SpO2Api(api_client)
    start_date = 'start_date_example' # str | The date in the format of yyyy-MM-dd or today.
    end_date = 'end_date_example' # str | The date in the format of yyyy-MM-dd or today.

    try:
        # Get SpO2 Summary by Interval
        api_response = await api_instance.get_sp_o2_summary_by_interval(start_date, end_date)
        print("The response of SpO2Api->get_sp_o2_summary_by_interval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpO2Api->get_sp_o2_summary_by_interval: %s\n" % e)
```

### Parameters

| Name           | Type    | Description                                    | Notes |
| -------------- | ------- | ---------------------------------------------- | ----- |
| **start_date** | **str** | The date in the format of yyyy-MM-dd or today. |
| **end_date**   | **str** | The date in the format of yyyy-MM-dd or today. |

### Return type

[**GetSpO2SummaryResponse**](GetSpO2SummaryResponse.md)

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
