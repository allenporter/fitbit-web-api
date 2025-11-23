# CardioScoreSummary

## Properties

| Name          | Type                              | Description                                  | Notes      |
| ------------- | --------------------------------- | -------------------------------------------- | ---------- |
| **date_time** | **date**                          | The date specified in the format YYYY-MM-DD. | [optional] |
| **value**     | [**Vo2MaxValue**](Vo2MaxValue.md) |                                              | [optional] |

## Example

```python
from fitbit_web_api.models.cardio_score_summary import CardioScoreSummary

# TODO update the JSON string below
json = "{}"
# create an instance of CardioScoreSummary from a JSON string
cardio_score_summary_instance = CardioScoreSummary.from_json(json)
# print the JSON string representation of the object
print(CardioScoreSummary.to_json())

# convert the object into a dict
cardio_score_summary_dict = cardio_score_summary_instance.to_dict()
# create an instance of CardioScoreSummary from a dict
cardio_score_summary_from_dict = CardioScoreSummary.from_dict(cardio_score_summary_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
