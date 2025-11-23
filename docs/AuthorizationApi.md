# fitbit_web_api.AuthorizationApi

All URIs are relative to *https://api.fitbit.com*

| Method                                             | HTTP request                    | Description                                          |
| -------------------------------------------------- | ------------------------------- | ---------------------------------------------------- |
| [**introspect**](AuthorizationApi.md#introspect)   | **POST** /1.1/oauth2/introspect | Retrieve the active state of an OAuth 2.0 token      |
| [**oauth_token**](AuthorizationApi.md#oauth_token) | **POST** /oauth2/token          | Get OAuth 2 access token                             |
| [**revoke**](AuthorizationApi.md#revoke)           | **POST** /oauth2/revoke         | Revokes consent of the access token or refresh token |

# **introspect**

> Oauth2Introspect introspect(token)

Retrieve the active state of an OAuth 2.0 token

Retrieves the active state of an OAuth 2.0 token. It follows https://tools.ietf.org/html/rfc7662.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.oauth2_introspect import Oauth2Introspect
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
    api_instance = fitbit_web_api.AuthorizationApi(api_client)
    token = 'token_example' # str | OAuth 2.0 token to retrieve the state of

    try:
        # Retrieve the active state of an OAuth 2.0 token
        api_response = await api_instance.introspect(token)
        print("The response of AuthorizationApi->introspect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationApi->introspect: %s\n" % e)
```

### Parameters

| Name      | Type    | Description                              | Notes |
| --------- | ------- | ---------------------------------------- | ----- |
| **token** | **str** | OAuth 2.0 token to retrieve the state of |

### Return type

[**Oauth2Introspect**](Oauth2Introspect.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                              | Response headers |
| ----------- | ------------------------------------------------------------------------ | ---------------- |
| **200**     | A successful request.                                                    | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satisfied. | -                |
| **401**     | Authentication was unsuccessful due to invalid client credentials.       | -                |
| **409**     | Request conflict due to multiple clients                                 | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_token**

> Oauth2Token oauth_token(client_id, grant_type, authorization=authorization, code=code, expires_in=expires_in, redirect_uri=redirect_uri, refresh_token=refresh_token, state=state)

Get OAuth 2 access token

Retrieves an OAuth 2 access token.

### Example

```python
import fitbit_web_api
from fitbit_web_api.models.oauth2_token import Oauth2Token
from fitbit_web_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fitbit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fitbit_web_api.Configuration(
    host = "https://api.fitbit.com"
)


# Enter a context with an instance of the API client
async with fitbit_web_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fitbit_web_api.AuthorizationApi(api_client)
    client_id = 'client_id_example' # str | This is your Fitbit API application id from your settings on dev.fitbit.com.
    grant_type = 'grant_type_example' # str | Authorization grant type. Valid values are 'authorization_code' and 'refresh_token'.
    authorization = 'authorization_example' # str | The Authorization header must be set to 'Basic' followed by a space, then the Base64 encoded string of your application's client id and secret concatenated with a colon. For example, 'Basic Y2xpZW50X2lkOmNsaWVudCBzZWNyZXQ='. The Base64 encoded string, 'Y2xpZW50X2lkOmNsaWVudCBzZWNyZXQ=', is decoded as 'client_id:client secret'. (optional)
    code = 'code_example' # str | Authorization code received in the redirect as URI parameter. Required if using the Authorization Code flow. (optional)
    expires_in = 'expires_in_example' # str | Specify the desired access token lifetime. Defaults to 28800 for 8 hours. The other valid value is 3600 for 1 hour. (optional)
    redirect_uri = 'redirect_uri_example' # str | Uri to which the access token will be sent if the request is successful. Required if specified in the redirect to the authorization page. Must be exact match. (optional)
    refresh_token = 'refresh_token_example' # str | Refresh token issued by Fitbit. Required if 'grant_type' is 'refresh_token'. (optional)
    state = 'state_example' # str | Required if specified in the redirect uri of the authorization page. Must be an exact match. (optional)

    try:
        # Get OAuth 2 access token
        api_response = await api_instance.oauth_token(client_id, grant_type, authorization=authorization, code=code, expires_in=expires_in, redirect_uri=redirect_uri, refresh_token=refresh_token, state=state)
        print("The response of AuthorizationApi->oauth_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationApi->oauth_token: %s\n" % e)
```

### Parameters

| Name              | Type    | Description                                                                                                                                                                                                                                                                                                                                                                            | Notes      |
| ----------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **client_id**     | **str** | This is your Fitbit API application id from your settings on dev.fitbit.com.                                                                                                                                                                                                                                                                                                           |
| **grant_type**    | **str** | Authorization grant type. Valid values are &#39;authorization_code&#39; and &#39;refresh_token&#39;.                                                                                                                                                                                                                                                                                   |
| **authorization** | **str** | The Authorization header must be set to &#39;Basic&#39; followed by a space, then the Base64 encoded string of your application&#39;s client id and secret concatenated with a colon. For example, &#39;Basic Y2xpZW50X2lkOmNsaWVudCBzZWNyZXQ&#x3D;&#39;. The Base64 encoded string, &#39;Y2xpZW50X2lkOmNsaWVudCBzZWNyZXQ&#x3D;&#39;, is decoded as &#39;client_id:client secret&#39;. | [optional] |
| **code**          | **str** | Authorization code received in the redirect as URI parameter. Required if using the Authorization Code flow.                                                                                                                                                                                                                                                                           | [optional] |
| **expires_in**    | **str** | Specify the desired access token lifetime. Defaults to 28800 for 8 hours. The other valid value is 3600 for 1 hour.                                                                                                                                                                                                                                                                    | [optional] |
| **redirect_uri**  | **str** | Uri to which the access token will be sent if the request is successful. Required if specified in the redirect to the authorization page. Must be exact match.                                                                                                                                                                                                                         | [optional] |
| **refresh_token** | **str** | Refresh token issued by Fitbit. Required if &#39;grant_type&#39; is &#39;refresh_token&#39;.                                                                                                                                                                                                                                                                                           | [optional] |
| **state**         | **str** | Required if specified in the redirect uri of the authorization page. Must be an exact match.                                                                                                                                                                                                                                                                                           | [optional] |

### Return type

[**Oauth2Token**](Oauth2Token.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                           | Response headers |
| ----------- | ------------------------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                                 | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satisfied.              | -                |
| **401**     | Authentication was unsuccessful due to invalid client credentials.                    | -                |
| **409**     | Request conflict due to multiple clients attempting to refresh the same access token. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke**

> revoke(token)

Revokes consent of the access token or refresh token

Revokes consent of the access token or refresh token

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
    api_instance = fitbit_web_api.AuthorizationApi(api_client)
    token = 'token_example' # str | The access token or refresh token to be revoked

    try:
        # Revokes consent of the access token or refresh token
        await api_instance.revoke(token)
    except Exception as e:
        print("Exception when calling AuthorizationApi->revoke: %s\n" % e)
```

### Parameters

| Name      | Type    | Description                                     | Notes |
| --------- | ------- | ----------------------------------------------- | ----- |
| **token** | **str** | The access token or refresh token to be revoked |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined

### HTTP response details

| Status code | Description                                                              | Response headers |
| ----------- | ------------------------------------------------------------------------ | ---------------- |
| **200**     | A successful request.                                                    | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satisfied. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
