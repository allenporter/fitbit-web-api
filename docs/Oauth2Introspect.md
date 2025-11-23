# Oauth2Introspect

## Properties

| Name           | Type     | Description                                   | Notes      |
| -------------- | -------- | --------------------------------------------- | ---------- |
| **active**     | **bool** | True if the token is active, false otherwise. | [optional] |
| **scope**      | **str**  | The scopes that the token has access to.      | [optional] |
| **client_id**  | **str**  | The client ID.                                | [optional] |
| **user_id**    | **str**  | The user ID.                                  | [optional] |
| **token_type** | **str**  | The type of token.                            | [optional] |
| **exp**        | **int**  | The timestamp when the token expires.         | [optional] |
| **iat**        | **int**  | The timestamp when the token was issued.      | [optional] |

## Example

```python
from fitbit_web_api.models.oauth2_introspect import Oauth2Introspect

# TODO update the JSON string below
json = "{}"
# create an instance of Oauth2Introspect from a JSON string
oauth2_introspect_instance = Oauth2Introspect.from_json(json)
# print the JSON string representation of the object
print(Oauth2Introspect.to_json())

# convert the object into a dict
oauth2_introspect_dict = oauth2_introspect_instance.to_dict()
# create an instance of Oauth2Introspect from a dict
oauth2_introspect_from_dict = Oauth2Introspect.from_dict(oauth2_introspect_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
