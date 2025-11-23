# ActivitySummary

## Properties

| Name                       | Type                                                                        | Description                                                                                         | Notes      |
| -------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ---------- |
| **active_score**           | **int**                                                                     | Functionality removed. A response is returned for backward compatibility.                           | [optional] |
| **activity_calories**      | **int**                                                                     | The number of calories burned for the day during periods the user was active above sedentary level. | [optional] |
| **calories_bmr**           | **int**                                                                     | Total BMR calories burned for the day.                                                              | [optional] |
| **calories_out**           | **int**                                                                     | Total calories burned for the day.                                                                  | [optional] |
| **distances**              | [**List[ActivitySummaryDistancesInner]**](ActivitySummaryDistancesInner.md) | List of distances traveled for the day.                                                             | [optional] |
| **elevation**              | **float**                                                                   | The elevation traveled for the day.                                                                 | [optional] |
| **fairly_active_minutes**  | **int**                                                                     | Total minutes the user was fairly/moderately active.                                                | [optional] |
| **floors**                 | **int**                                                                     | The equivalent floors climbed for the day.                                                          | [optional] |
| **lightly_active_minutes** | **int**                                                                     | Total minutes the user was lightly active.                                                          | [optional] |
| **marginal_calories**      | **int**                                                                     | Total marginal estimated calories burned for the day.                                               | [optional] |
| **resting_heart_rate**     | **int**                                                                     | The user&#39;s calculated resting heart rate.                                                       | [optional] |
| **sedentary_minutes**      | **int**                                                                     | Total minutes the user was sedentary.                                                               | [optional] |
| **steps**                  | **int**                                                                     | Total steps taken for the day.                                                                      | [optional] |
| **very_active_minutes**    | **int**                                                                     | Total minutes the user was very active.                                                             | [optional] |

## Example

```python
from fitbit_web_api.models.activity_summary import ActivitySummary

# TODO update the JSON string below
json = "{}"
# create an instance of ActivitySummary from a JSON string
activity_summary_instance = ActivitySummary.from_json(json)
# print the JSON string representation of the object
print(ActivitySummary.to_json())

# convert the object into a dict
activity_summary_dict = activity_summary_instance.to_dict()
# create an instance of ActivitySummary from a dict
activity_summary_from_dict = ActivitySummary.from_dict(activity_summary_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
