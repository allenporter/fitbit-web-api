# GetSubscriptionListResponse

## Properties

| Name                  | Type                                      | Description | Notes      |
| --------------------- | ----------------------------------------- | ----------- | ---------- |
| **api_subscriptions** | [**List[Subscription]**](Subscription.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_subscription_list_response import GetSubscriptionListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubscriptionListResponse from a JSON string
get_subscription_list_response_instance = GetSubscriptionListResponse.from_json(json)
# print the JSON string representation of the object
print(GetSubscriptionListResponse.to_json())

# convert the object into a dict
get_subscription_list_response_dict = get_subscription_list_response_instance.to_dict()
# create an instance of GetSubscriptionListResponse from a dict
get_subscription_list_response_from_dict = GetSubscriptionListResponse.from_dict(get_subscription_list_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
