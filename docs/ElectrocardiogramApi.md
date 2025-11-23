# fitbit_web_api.ElectrocardiogramApi

All URIs are relative to *https://api.fitbit.com*

| Method                                                           | HTTP request                    | Description      |
| ---------------------------------------------------------------- | ------------------------------- | ---------------- |
| [**get_ecg_log_list**](ElectrocardiogramApi.md#get_ecg_log_list) | **GET** /1/user/-/ecg/list.json | Get ECG Log List |

# **get_ecg_log_list**

> GetEcgLogListResponse get_ecg_log_list(sort, offset, limit, before_date=before_date, after_date=after_date)

Get ECG Log List

This endpoint is used for querying the user's on-device ECG readings.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_ecg_log_list_response import GetEcgLogListResponse
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
    api_instance = fitbit_web_api.ElectrocardiogramApi(api_client)
    sort = 'sort_example' # str | The sort order of entries by date asc (ascending) or desc (descending).
    offset = 0 # int | The offset number of entries. (default to 0)
    limit = 56 # int | The maximum number of entries returned (maximum;10).
    before_date = '2013-10-20' # date | The date in the format yyyy-MM-ddTHH:mm:ss. Only yyyy-MM-dd is required. Either beforeDate or afterDate should be specified. (optional)
    after_date = '2013-10-20' # date | The date in the format yyyy-MM-ddTHH:mm:ss. (optional)

    try:
        # Get ECG Log List
        api_response = await api_instance.get_ecg_log_list(sort, offset, limit, before_date=before_date, after_date=after_date)
        print("The response of ElectrocardiogramApi->get_ecg_log_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ElectrocardiogramApi->get_ecg_log_list: %s\n" % e)
```

### Parameters

| Name            | Type     | Description                                                                                                                  | Notes          |
| --------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------- | -------------- |
| **sort**        | **str**  | The sort order of entries by date asc (ascending) or desc (descending).                                                      |
| **offset**      | **int**  | The offset number of entries.                                                                                                | [default to 0] |
| **limit**       | **int**  | The maximum number of entries returned (maximum;10).                                                                         |
| **before_date** | **date** | The date in the format yyyy-MM-ddTHH:mm:ss. Only yyyy-MM-dd is required. Either beforeDate or afterDate should be specified. | [optional]     |
| **after_date**  | **date** | The date in the format yyyy-MM-ddTHH:mm:ss.                                                                                  | [optional]     |

### Return type

[**GetEcgLogListResponse**](GetEcgLogListResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
