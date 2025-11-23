# fitbit_web_api.ActivityApi

All URIs are relative to *https://api.fitbit.com*

| Method                                                                        | HTTP request                                                | Description                  |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------- | ---------------------------- |
| [**add_activities_log**](ActivityApi.md#add_activities_log)                   | **POST** /1/user/-/activities.json                          | Log Activity                 |
| [**add_favorite_activities**](ActivityApi.md#add_favorite_activities)         | **POST** /1/user/-/activities/favorite/{activity-id}.json   | Add Favorite Activity        |
| [**add_update_activities_goals**](ActivityApi.md#add_update_activities_goals) | **POST** /1/user/-/activities/goals/{period}.json           | Update Activity Goals        |
| [**delete_activities_log**](ActivityApi.md#delete_activities_log)             | **DELETE** /1/user/-/activities/{activity-log-id}.json      | Delete Activity Log          |
| [**delete_favorite_activities**](ActivityApi.md#delete_favorite_activities)   | **DELETE** /1/user/-/activities/favorite/{activity-id}.json | Delete Favorite Activity     |
| [**get_activities_by_date**](ActivityApi.md#get_activities_by_date)           | **GET** /1/user/-/activities/date/{date}.json               | Get Activity Summary by Date |
| [**get_activities_goals**](ActivityApi.md#get_activities_goals)               | **GET** /1/user/-/activities/goals/{period}.json            | Get Activity Goals           |
| [**get_activities_log**](ActivityApi.md#get_activities_log)                   | **GET** /1/user/-/activities.json                           | Get Lifetime Stats           |
| [**get_activities_log_list**](ActivityApi.md#get_activities_log_list)         | **GET** /1/user/-/activities/list.json                      | Get Activity Log List        |
| [**get_activities_tcx**](ActivityApi.md#get_activities_tcx)                   | **GET** /1/user/-/activities/{log-id}.tcx                   | Get Activity TCX             |
| [**get_activities_type_detail**](ActivityApi.md#get_activities_type_detail)   | **GET** /1/activities/{activity-id}.json                    | Get Activity Type            |
| [**get_activities_types**](ActivityApi.md#get_activities_types)               | **GET** /1/activities.json                                  | Browse Activity Types        |
| [**get_favorite_activities**](ActivityApi.md#get_favorite_activities)         | **GET** /1/user/-/activities/favorite.json                  | Get Favorite Activities      |
| [**get_frequent_activities**](ActivityApi.md#get_frequent_activities)         | **GET** /1/user/-/activities/frequent.json                  | Get Frequent Activities      |
| [**get_recent_activities**](ActivityApi.md#get_recent_activities)             | **GET** /1/user/-/activities/recent.json                    | Get Recent Activity Types    |

# **add_activities_log**

> add_activities_log(activity_id, manual_calories, start_time, duration_millis, var_date, distance, activity_name=activity_name, distance_unit=distance_unit)

Log Activity

The Log Activity endpoint creates log entry for an activity or user's private custom activity using units in the unit system which corresponds to the Accept-Language header provided (or using optional custom distanceUnit) and get a response in the format requested.

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
    api_instance = fitbit_web_api.ActivityApi(api_client)
    activity_id = 56 # int | The ID of the activity, directory activity or intensity level activity.
    manual_calories = 56 # int | Calories burned that are manaully specified. Required with activityName must be provided.
    start_time = 'start_time_example' # str | Activity start time. Hours and minutes in the format HH:mm:ss.
    duration_millis = 56 # int | Duration in milliseconds.
    var_date = '2013-10-20' # date | Log entry date in the format yyyy-MM-dd.
    distance = 56 # int | Distance is required for logging directory activity in the format X.XX and in the selected distanceUnit.
    activity_name = 'activity_name_example' # str | Custom activity name. Either activityId or activityName must be provided. (optional)
    distance_unit = 56 # int | Distance measurement unit. Steps units are available only for Walking (activityId=90013) and Running (activityId=90009) directory activities and their intensity levels. (optional)

    try:
        # Log Activity
        await api_instance.add_activities_log(activity_id, manual_calories, start_time, duration_millis, var_date, distance, activity_name=activity_name, distance_unit=distance_unit)
    except Exception as e:
        print("Exception when calling ActivityApi->add_activities_log: %s\n" % e)
```

### Parameters

| Name                | Type     | Description                                                                                                                                                                        | Notes      |
| ------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **activity_id**     | **int**  | The ID of the activity, directory activity or intensity level activity.                                                                                                            |
| **manual_calories** | **int**  | Calories burned that are manaully specified. Required with activityName must be provided.                                                                                          |
| **start_time**      | **str**  | Activity start time. Hours and minutes in the format HH:mm:ss.                                                                                                                     |
| **duration_millis** | **int**  | Duration in milliseconds.                                                                                                                                                          |
| **var_date**        | **date** | Log entry date in the format yyyy-MM-dd.                                                                                                                                           |
| **distance**        | **int**  | Distance is required for logging directory activity in the format X.XX and in the selected distanceUnit.                                                                           |
| **activity_name**   | **str**  | Custom activity name. Either activityId or activityName must be provided.                                                                                                          | [optional] |
| **distance_unit**   | **int**  | Distance measurement unit. Steps units are available only for Walking (activityId&#x3D;90013) and Running (activityId&#x3D;90009) directory activities and their intensity levels. | [optional] |

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

# **add_favorite_activities**

> add_favorite_activities(activity_id)

Add Favorite Activity

Adds the activity with the given ID to user's list of favorite activities.

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
    api_instance = fitbit_web_api.ActivityApi(api_client)
    activity_id = 'activity_id_example' # str | The encoded ID of the activity.

    try:
        # Add Favorite Activity
        await api_instance.add_favorite_activities(activity_id)
    except Exception as e:
        print("Exception when calling ActivityApi->add_favorite_activities: %s\n" % e)
```

### Parameters

| Name            | Type    | Description                     | Notes |
| --------------- | ------- | ------------------------------- | ----- |
| **activity_id** | **str** | The encoded ID of the activity. |

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
| **201**     | The request fulfilled and new resource being created.                                                                                                                                                | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified.                                                                                                                              | -                |
| **401**     | The request requires user authentication.                                                                                                                                                            | -                |
| **409**     | Returned if the given user is already subscribed to this stream using a different subscription ID, OR if the given subscription ID is already used to identify a subscription to a different stream. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_update_activities_goals**

> add_update_activities_goals(period, type, value)

Update Activity Goals

Updates a user's daily or weekly activity goals and returns a response using units in the unit system which corresponds to the Accept-Language header provided.

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
    api_instance = fitbit_web_api.ActivityApi(api_client)
    period = 'period_example' # str | daily or weekly.
    type = 'type_example' # str | goal type
    value = 'value_example' # str | goal value

    try:
        # Update Activity Goals
        await api_instance.add_update_activities_goals(period, type, value)
    except Exception as e:
        print("Exception when calling ActivityApi->add_update_activities_goals: %s\n" % e)
```

### Parameters

| Name       | Type    | Description      | Notes |
| ---------- | ------- | ---------------- | ----- |
| **period** | **str** | daily or weekly. |
| **type**   | **str** | goal type        |
| **value**  | **str** | goal value       |

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

# **delete_activities_log**

> delete_activities_log(activity_log_id)

Delete Activity Log

Deletes a user's activity log entry with the given ID.

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
    api_instance = fitbit_web_api.ActivityApi(api_client)
    activity_log_id = 56 # int | The id of the activity log entry.

    try:
        # Delete Activity Log
        await api_instance.delete_activities_log(activity_log_id)
    except Exception as e:
        print("Exception when calling ActivityApi->delete_activities_log: %s\n" % e)
```

### Parameters

| Name                | Type    | Description                       | Notes |
| ------------------- | ------- | --------------------------------- | ----- |
| **activity_log_id** | **int** | The id of the activity log entry. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details

| Status code | Description                                             | Response headers |
| ----------- | ------------------------------------------------------- | ---------------- |
| **204**     | No Content. The request was successful.                 | -                |
| **400**     | Bad Request. The request likely contained bad syntax.   | -                |
| **401**     | Unauthorized. The request requires user authentication. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_favorite_activities**

> delete_favorite_activities(activity_id)

Delete Favorite Activity

Removes the activity with the given ID from a user's list of favorite activities.

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
    api_instance = fitbit_web_api.ActivityApi(api_client)
    activity_id = 'activity_id_example' # str | The ID of the activity to be removed.

    try:
        # Delete Favorite Activity
        await api_instance.delete_favorite_activities(activity_id)
    except Exception as e:
        print("Exception when calling ActivityApi->delete_favorite_activities: %s\n" % e)
```

### Parameters

| Name            | Type    | Description                           | Notes |
| --------------- | ------- | ------------------------------------- | ----- |
| **activity_id** | **str** | The ID of the activity to be removed. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details

| Status code | Description                                             | Response headers |
| ----------- | ------------------------------------------------------- | ---------------- |
| **204**     | No Content. The request was successful.                 | -                |
| **400**     | Bad Request. The request likely contained bad syntax.   | -                |
| **401**     | Unauthorized. The request requires user authentication. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activities_by_date**

> GetDailyActivitySummaryResponse get_activities_by_date(var_date)

Get Activity Summary by Date

Retrieves a summary and list of a user's activities and activity log entries for a given day.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_daily_activity_summary_response import GetDailyActivitySummaryResponse
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
    api_instance = fitbit_web_api.ActivityApi(api_client)
    var_date = '2013-10-20' # date | The date in the format yyyy-MM-dd

    try:
        # Get Activity Summary by Date
        api_response = await api_instance.get_activities_by_date(var_date)
        print("The response of ActivityApi->get_activities_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->get_activities_by_date: %s\n" % e)
```

### Parameters

| Name         | Type     | Description                       | Notes |
| ------------ | -------- | --------------------------------- | ----- |
| **var_date** | **date** | The date in the format yyyy-MM-dd |

### Return type

[**GetDailyActivitySummaryResponse**](GetDailyActivitySummaryResponse.md)

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

# **get_activities_goals**

> GetActivityGoalsResponse get_activities_goals(period)

Get Activity Goals

Retreives a user's current daily or weekly activity goals using measurement units as defined in the unit system, which corresponds to the Accept-Language header provided.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_activity_goals_response import GetActivityGoalsResponse
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
    api_instance = fitbit_web_api.ActivityApi(api_client)
    period = 'period_example' # str | daily or weekly.

    try:
        # Get Activity Goals
        api_response = await api_instance.get_activities_goals(period)
        print("The response of ActivityApi->get_activities_goals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->get_activities_goals: %s\n" % e)
```

### Parameters

| Name       | Type    | Description      | Notes |
| ---------- | ------- | ---------------- | ----- |
| **period** | **str** | daily or weekly. |

### Return type

[**GetActivityGoalsResponse**](GetActivityGoalsResponse.md)

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

# **get_activities_log**

> LifetimeStats get_activities_log()

Get Lifetime Stats

Updates a user's daily activity goals and returns a response using units in the unit system which corresponds to the Accept-Language header provided.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.lifetime_stats import LifetimeStats
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
    api_instance = fitbit_web_api.ActivityApi(api_client)

    try:
        # Get Lifetime Stats
        api_response = await api_instance.get_activities_log()
        print("The response of ActivityApi->get_activities_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->get_activities_log: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**LifetimeStats**](LifetimeStats.md)

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

# **get_activities_log_list**

> GetActivityLogListResponse get_activities_log_list(sort, offset, limit, before_date=before_date, after_date=after_date)

Get Activity Log List

Retreives a list of user's activity log entries before or after a given day with offset and limit using units in the unit system which corresponds to the Accept-Language header provided.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_activity_log_list_response import GetActivityLogListResponse
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
    api_instance = fitbit_web_api.ActivityApi(api_client)
    sort = 'sort_example' # str | The sort order of entries by date asc (ascending) or desc (descending).
    offset = 0 # int | The offset number of entries. (default to 0)
    limit = 56 # int | The maximum number of entries returned (maximum;100).
    before_date = '2013-10-20' # date | The date in the format yyyy-MM-ddTHH:mm:ss. Only yyyy-MM-dd is required. Either beforeDate or afterDate should be specified. (optional)
    after_date = '2013-10-20' # date | The date in the format yyyy-MM-ddTHH:mm:ss. (optional)

    try:
        # Get Activity Log List
        api_response = await api_instance.get_activities_log_list(sort, offset, limit, before_date=before_date, after_date=after_date)
        print("The response of ActivityApi->get_activities_log_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->get_activities_log_list: %s\n" % e)
```

### Parameters

| Name            | Type     | Description                                                                                                                  | Notes          |
| --------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------- | -------------- |
| **sort**        | **str**  | The sort order of entries by date asc (ascending) or desc (descending).                                                      |
| **offset**      | **int**  | The offset number of entries.                                                                                                | [default to 0] |
| **limit**       | **int**  | The maximum number of entries returned (maximum;100).                                                                        |
| **before_date** | **date** | The date in the format yyyy-MM-ddTHH:mm:ss. Only yyyy-MM-dd is required. Either beforeDate or afterDate should be specified. | [optional]     |
| **after_date**  | **date** | The date in the format yyyy-MM-ddTHH:mm:ss.                                                                                  | [optional]     |

### Return type

[**GetActivityLogListResponse**](GetActivityLogListResponse.md)

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

# **get_activities_tcx**

> get_activities_tcx(log_id, include_partial_tcx=include_partial_tcx)

Get Activity TCX

Retreives the details of a user's location and heart rate data during a logged exercise activity.

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
    api_instance = fitbit_web_api.ActivityApi(api_client)
    log_id = 'log_id_example' # str | The activity's log ID.
    include_partial_tcx = True # bool | Include TCX points regardless of GPS data being present (optional)

    try:
        # Get Activity TCX
        await api_instance.get_activities_tcx(log_id, include_partial_tcx=include_partial_tcx)
    except Exception as e:
        print("Exception when calling ActivityApi->get_activities_tcx: %s\n" % e)
```

### Parameters

| Name                    | Type     | Description                                             | Notes      |
| ----------------------- | -------- | ------------------------------------------------------- | ---------- |
| **log_id**              | **str**  | The activity&#39;s log ID.                              |
| **include_partial_tcx** | **bool** | Include TCX points regardless of GPS data being present | [optional] |

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
| **403**     | The request was a valid request, but the server is refusing to respond to it.                                                                                                                        | -                |
| **409**     | Returned if the given user is already subscribed to this stream using a different subscription ID, OR if the given subscription ID is already used to identify a subscription to a different stream. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activities_type_detail**

> get_activities_type_detail(activity_id)

Get Activity Type

Returns the detail of a specific activity in the Fitbit activities database in the format requested. If activity has levels, it also returns a list of activity level details.

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
    api_instance = fitbit_web_api.ActivityApi(api_client)
    activity_id = 'activity_id_example' # str | The activity ID.

    try:
        # Get Activity Type
        await api_instance.get_activities_type_detail(activity_id)
    except Exception as e:
        print("Exception when calling ActivityApi->get_activities_type_detail: %s\n" % e)
```

### Parameters

| Name            | Type    | Description      | Notes |
| --------------- | ------- | ---------------- | ----- |
| **activity_id** | **str** | The activity ID. |

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

# **get_activities_types**

> get_activities_types()

Browse Activity Types

Retreives a tree of all valid Fitbit public activities from the activities catelog as well as private custom activities the user created in the format requested.

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
    api_instance = fitbit_web_api.ActivityApi(api_client)

    try:
        # Browse Activity Types
        await api_instance.get_activities_types()
    except Exception as e:
        print("Exception when calling ActivityApi->get_activities_types: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

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

# **get_favorite_activities**

> get_favorite_activities()

Get Favorite Activities

Returns a list of a user's favorite activities.

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
    api_instance = fitbit_web_api.ActivityApi(api_client)

    try:
        # Get Favorite Activities
        await api_instance.get_favorite_activities()
    except Exception as e:
        print("Exception when calling ActivityApi->get_favorite_activities: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

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

# **get_frequent_activities**

> get_frequent_activities()

Get Frequent Activities

Retreives a list of a user's frequent activities in the format requested using units in the unit system which corresponds to the Accept-Language header provided.

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
    api_instance = fitbit_web_api.ActivityApi(api_client)

    try:
        # Get Frequent Activities
        await api_instance.get_frequent_activities()
    except Exception as e:
        print("Exception when calling ActivityApi->get_frequent_activities: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

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

# **get_recent_activities**

> get_recent_activities()

Get Recent Activity Types

Retreives a list of a user's recent activities types logged with some details of the last activity log of that type using units in the unit system which corresponds to the Accept-Language header provided.

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
    api_instance = fitbit_web_api.ActivityApi(api_client)

    try:
        # Get Recent Activity Types
        await api_instance.get_recent_activities()
    except Exception as e:
        print("Exception when calling ActivityApi->get_recent_activities: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

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
