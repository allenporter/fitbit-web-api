# fitbit_web_api.SubscriptionsApi

All URIs are relative to *https://api.fitbit.com*

| Method                                                                   | HTTP request                                                                   | Description                 |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | --------------------------- |
| [**add_subscriptions**](SubscriptionsApi.md#add_subscriptions)           | **POST** /1/user/-/{collection-path}/apiSubscriptions/{subscription-id}.json   | Add a Subscription          |
| [**delete_subscriptions**](SubscriptionsApi.md#delete_subscriptions)     | **DELETE** /1/user/-/{collection-path}/apiSubscriptions/{subscription-id}.json | Delete a Subscription       |
| [**get_subscriptions_list**](SubscriptionsApi.md#get_subscriptions_list) | **GET** /1/user/-/{collection-path}/apiSubscriptions.json                      | Get a List of Subscriptions |

# **add_subscriptions**

> Subscription add_subscriptions(collection_path, subscription_id)

Add a Subscription

Adds a subscription in your application so that users can get notifications and return a response in the format requested. The subscription-id value provides a way to associate an update with a particular user stream in your application.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.subscription import Subscription
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
    api_instance = fitbit_web_api.SubscriptionsApi(api_client)
    collection_path = 'collection_path_example' # str | This is the resource of the collection to receive notifications from (foods, activities, sleep, or body). If not present, subscription will be created for all collections. If you have both all and specific collection subscriptions, you will get duplicate notifications on that collections' updates. Each subscriber can have only one subscription for a specific user's collection.
    subscription_id = 'subscription_id_example' # str | This is the unique ID of the subscription created by the API client application. Each ID must be unique across the entire set of subscribers and collections. The Fitbit servers will pass this ID back along with any notifications about the user indicated by the user parameter in the URL path.

    try:
        # Add a Subscription
        api_response = await api_instance.add_subscriptions(collection_path, subscription_id)
        print("The response of SubscriptionsApi->add_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->add_subscriptions: %s\n" % e)
```

### Parameters

| Name                | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                         | Notes |
| ------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **collection_path** | **str** | This is the resource of the collection to receive notifications from (foods, activities, sleep, or body). If not present, subscription will be created for all collections. If you have both all and specific collection subscriptions, you will get duplicate notifications on that collections&#39; updates. Each subscriber can have only one subscription for a specific user&#39;s collection. |
| **subscription_id** | **str** | This is the unique ID of the subscription created by the API client application. Each ID must be unique across the entire set of subscribers and collections. The Fitbit servers will pass this ID back along with any notifications about the user indicated by the user parameter in the URL path.                                                                                                |

### Return type

[**Subscription**](Subscription.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                                                                                                                          | Response headers |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                                                                                                                                                | -                |
| **201**     | A successful request.                                                                                                                                                                                | -                |
| **409**     | Returned if the given user is already subscribed to this stream using a different subscription ID, OR if the given subscription ID is already used to identify a subscription to a different stream. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscriptions**

> delete_subscriptions(collection_path, subscription_id)

Delete a Subscription

Deletes a subscription for a user..

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
    api_instance = fitbit_web_api.SubscriptionsApi(api_client)
    collection_path = 'collection_path_example' # str | This is the resource of the collection to receive notifications from (foods, activities, sleep, or body). If not present, subscription will be created for all collections. If you have both all and specific collection subscriptions, you will get duplicate notifications on that collections' updates. Each subscriber can have only one subscription for a specific user's collection.
    subscription_id = 'subscription_id_example' # str | This is the resource of the collection to receive notifications from (foods, activities, sleep, or body). If not present, subscription will be created for all collections. If you have both all and specific collection subscriptions, you will get duplicate notifications on that collections' updates. Each subscriber can have only one subscription for a specific user's collection.

    try:
        # Delete a Subscription
        await api_instance.delete_subscriptions(collection_path, subscription_id)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->delete_subscriptions: %s\n" % e)
```

### Parameters

| Name                | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                         | Notes |
| ------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **collection_path** | **str** | This is the resource of the collection to receive notifications from (foods, activities, sleep, or body). If not present, subscription will be created for all collections. If you have both all and specific collection subscriptions, you will get duplicate notifications on that collections&#39; updates. Each subscriber can have only one subscription for a specific user&#39;s collection. |
| **subscription_id** | **str** | This is the resource of the collection to receive notifications from (foods, activities, sleep, or body). If not present, subscription will be created for all collections. If you have both all and specific collection subscriptions, you will get duplicate notifications on that collections&#39; updates. Each subscriber can have only one subscription for a specific user&#39;s collection. |

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

# **get_subscriptions_list**

> GetSubscriptionListResponse get_subscriptions_list(collection_path)

Get a List of Subscriptions

Retreives a list of a user's subscriptions for your application in the format requested. You can either fetch subscriptions for a specific collection or the entire list of subscriptions for the user. For best practice, make sure that your application maintains this list on your side and use this endpoint only to periodically ensure data consistency.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_subscription_list_response import GetSubscriptionListResponse
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
    api_instance = fitbit_web_api.SubscriptionsApi(api_client)
    collection_path = 'collection_path_example' # str | This is the resource of the collection to receive notifications from (foods, activities, sleep, or body). If not present, subscription will be created for all collections. If you have both all and specific collection subscriptions, you will get duplicate notifications on that collections' updates. Each subscriber can have only one subscription for a specific user's collection.

    try:
        # Get a List of Subscriptions
        api_response = await api_instance.get_subscriptions_list(collection_path)
        print("The response of SubscriptionsApi->get_subscriptions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_subscriptions_list: %s\n" % e)
```

### Parameters

| Name                | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                         | Notes |
| ------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **collection_path** | **str** | This is the resource of the collection to receive notifications from (foods, activities, sleep, or body). If not present, subscription will be created for all collections. If you have both all and specific collection subscriptions, you will get duplicate notifications on that collections&#39; updates. Each subscriber can have only one subscription for a specific user&#39;s collection. |

### Return type

[**GetSubscriptionListResponse**](GetSubscriptionListResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                                                                                                                          | Response headers |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                                                                                                                                                | -                |
| **201**     | Returned if a new subscription was created in response to your request.                                                                                                                              | -                |
| **409**     | Returned if the given user is already subscribed to this stream using a different subscription ID, OR if the given subscription ID is already used to identify a subscription to a different stream. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
