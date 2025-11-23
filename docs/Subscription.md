# Subscription

## Properties

| Name                | Type    | Description                              | Notes      |
| ------------------- | ------- | ---------------------------------------- | ---------- |
| **collection_type** | **str** | The collection type of the subscription. | [optional] |
| **owner_id**        | **str** | The owner ID of the subscription.        | [optional] |
| **owner_type**      | **str** | The owner type of the subscription.      | [optional] |
| **subscriber_id**   | **str** | The subscriber ID of the subscription.   | [optional] |
| **subscription_id** | **str** | The subscription ID.                     | [optional] |

## Example

```python
from fitbit_web_api.models.subscription import Subscription

# TODO update the JSON string below
json = "{}"
# create an instance of Subscription from a JSON string
subscription_instance = Subscription.from_json(json)
# print the JSON string representation of the object
print(Subscription.to_json())

# convert the object into a dict
subscription_dict = subscription_instance.to_dict()
# create an instance of Subscription from a dict
subscription_from_dict = Subscription.from_dict(subscription_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
