# fitbit_web_api.FriendsApi

All URIs are relative to *https://api.fitbit.com*

| Method                                                               | HTTP request                                 | Description             |
| -------------------------------------------------------------------- | -------------------------------------------- | ----------------------- |
| [**get_friends**](FriendsApi.md#get_friends)                         | **GET** /1.1/user/-/friends.json             | Get Friends             |
| [**get_friends_leaderboard**](FriendsApi.md#get_friends_leaderboard) | **GET** /1.1/user/-/leaderboard/friends.json | Get Friends Leaderboard |

# **get_friends**

> GetFriendsResponse get_friends()

Get Friends

Returns data of a user's friends in the format requested using units in the unit system which corresponds to the Accept-Language header provided.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_friends_response import GetFriendsResponse
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
    api_instance = fitbit_web_api.FriendsApi(api_client)

    try:
        # Get Friends
        api_response = await api_instance.get_friends()
        print("The response of FriendsApi->get_friends:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FriendsApi->get_friends: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetFriendsResponse**](GetFriendsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                            | Response headers |
| ----------- | ---------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                  | -                |
| **401**     | The request requires user authentication.                              | -                |
| **403**     | The user&#39;s privacy settings prevent you from seeing their friends. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_friends_leaderboard**

> GetFriendsLeaderboardResponse get_friends_leaderboard()

Get Friends Leaderboard

Returns data of a user's friends in the format requested using units in the unit system which corresponds to the Accept-Language header provided.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_friends_leaderboard_response import GetFriendsLeaderboardResponse
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
    api_instance = fitbit_web_api.FriendsApi(api_client)

    try:
        # Get Friends Leaderboard
        api_response = await api_instance.get_friends_leaderboard()
        print("The response of FriendsApi->get_friends_leaderboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FriendsApi->get_friends_leaderboard: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetFriendsLeaderboardResponse**](GetFriendsLeaderboardResponse.md)

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
