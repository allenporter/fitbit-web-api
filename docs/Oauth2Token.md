# Oauth2Token

## Properties

| Name              | Type    | Description                                           | Notes      |
| ----------------- | ------- | ----------------------------------------------------- | ---------- |
| **access_token**  | **str** | The access token.                                     | [optional] |
| **expires_in**    | **int** | The number of seconds until the access token expires. | [optional] |
| **refresh_token** | **str** | The refresh token.                                    | [optional] |
| **scope**         | **str** | The scopes that the token has access to.              | [optional] |
| **token_type**    | **str** | The type of token.                                    | [optional] |
| **user_id**       | **str** | The user ID.                                          | [optional] |

## Example

```python
from fitbit_web_api.models.oauth2_token import Oauth2Token

# TODO update the JSON string below
json = "{}"
# create an instance of Oauth2Token from a JSON string
oauth2_token_instance = Oauth2Token.from_json(json)
# print the JSON string representation of the object
print(Oauth2Token.to_json())

# convert the object into a dict
oauth2_token_dict = oauth2_token_instance.to_dict()
# create an instance of Oauth2Token from a dict
oauth2_token_from_dict = Oauth2Token.from_dict(oauth2_token_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
