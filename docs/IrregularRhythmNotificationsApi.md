# fitbit_web_api.IrregularRhythmNotificationsApi

All URIs are relative to *https://api.fitbit.com*

| Method                                                                            | HTTP request                           | Description         |
| --------------------------------------------------------------------------------- | -------------------------------------- | ------------------- |
| [**get_irn_alerts_list**](IrregularRhythmNotificationsApi.md#get_irn_alerts_list) | **GET** /1/user/-/irn/alerts/list.json | Get IRN Alerts List |
| [**get_irn_profile**](IrregularRhythmNotificationsApi.md#get_irn_profile)         | **GET** /1/user/-/irn/profile.json     | Get IRN Profile     |

# **get_irn_alerts_list**

> GetIrnAlertsListResponse get_irn_alerts_list(sort, offset, limit, before_date=before_date, after_date=after_date)

Get IRN Alerts List

This endpoint returns a paginated list of Irregular Rhythm Notifications (IRN) alerts, as well as all of the alert tachograms. This endpoint will only return alerts that the user has read in the Fitbit app already, as that is meant as the primary entrypoint for viewing notifications.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_irn_alerts_list_response import GetIrnAlertsListResponse
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
    api_instance = fitbit_web_api.IrregularRhythmNotificationsApi(api_client)
    sort = 'sort_example' # str | The sort order of entries by date. Use asc (ascending) when using afterDate. Use desc (descending) when using beforeDate.
    offset = 0 # int | The offset number of entries. (default to 0)
    limit = 56 # int | The maximum number of entries returned (maximum;10).
    before_date = '2013-10-20' # date | The date in the format yyyy-MM-ddTHH:mm:ss. Only yyyy-MM-dd is required. Either beforeDate or afterDate should be specified. (optional)
    after_date = '2013-10-20' # date | The date in the format yyyy-MM-ddTHH:mm:ss. Only yyyy-MM-dd is required. Either beforeDate or afterDate should be specified. (optional)

    try:
        # Get IRN Alerts List
        api_response = await api_instance.get_irn_alerts_list(sort, offset, limit, before_date=before_date, after_date=after_date)
        print("The response of IrregularRhythmNotificationsApi->get_irn_alerts_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IrregularRhythmNotificationsApi->get_irn_alerts_list: %s\n" % e)
```

### Parameters

| Name            | Type     | Description                                                                                                                  | Notes          |
| --------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------- | -------------- |
| **sort**        | **str**  | The sort order of entries by date. Use asc (ascending) when using afterDate. Use desc (descending) when using beforeDate.    |
| **offset**      | **int**  | The offset number of entries.                                                                                                | [default to 0] |
| **limit**       | **int**  | The maximum number of entries returned (maximum;10).                                                                         |
| **before_date** | **date** | The date in the format yyyy-MM-ddTHH:mm:ss. Only yyyy-MM-dd is required. Either beforeDate or afterDate should be specified. | [optional]     |
| **after_date**  | **date** | The date in the format yyyy-MM-ddTHH:mm:ss. Only yyyy-MM-dd is required. Either beforeDate or afterDate should be specified. | [optional]     |

### Return type

[**GetIrnAlertsListResponse**](GetIrnAlertsListResponse.md)

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

# **get_irn_profile**

> GetIrnProfileResponse get_irn_profile()

Get IRN Profile

This endpoint returns the user state for Irregular Rhythm Notifications (IRN). The user state contains most information about the user’s current engagement with the feature, including onboarding progress and algorithm processing state.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_irn_profile_response import GetIrnProfileResponse
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
    api_instance = fitbit_web_api.IrregularRhythmNotificationsApi(api_client)

    try:
        # Get IRN Profile
        api_response = await api_instance.get_irn_profile()
        print("The response of IrregularRhythmNotificationsApi->get_irn_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IrregularRhythmNotificationsApi->get_irn_profile: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIrnProfileResponse**](GetIrnProfileResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                               | Response headers |
| ----------- | ----------------------------------------- | ---------------- |
| **200**     | A successful request.                     | -                |
| **401**     | The request requires user authentication. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
