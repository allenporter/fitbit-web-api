# ActivityLog

## Properties

| Name                        | Type         | Description                                                                                 | Notes      |
| --------------------------- | ------------ | ------------------------------------------------------------------------------------------- | ---------- |
| **activity_id**             | **int**      | The ID of the activity.                                                                     | [optional] |
| **activity_parent_id**      | **int**      | The ID of the top level (&#39;parent&#39;) activity.                                        | [optional] |
| **activity_parent_name**    | **str**      | The name of the top level (&#39;parent&#39;) activity.                                      | [optional] |
| **calories**                | **int**      | Number of calories burned during the exercise.                                              | [optional] |
| **description**             | **str**      | The description of the recorded exercise.                                                   | [optional] |
| **distance**                | **float**    | Distance traveled during the on-device recorded exercise.                                   | [optional] |
| **duration**                | **int**      | The activeDuration (milliseconds) + any pauses that occurred during the activity recording. | [optional] |
| **has_active_zone_minutes** | **bool**     | Indicates if the activity has active zone minutes.                                          | [optional] |
| **has_start_time**          | **bool**     | Indicates if the activity has a start time.                                                 | [optional] |
| **is_favorite**             | **bool**     | Indicates if the activity is a favorite.                                                    | [optional] |
| **last_modified**           | **datetime** | Timestamp the exercise was last modified.                                                   | [optional] |
| **log_id**                  | **int**      | The activity log identifier for the exercise.                                               | [optional] |
| **name**                    | **str**      | Name of the recorded exercise.                                                              | [optional] |
| **start_date**              | **date**     | The start date of the recorded exercise.                                                    | [optional] |
| **start_time**              | **str**      | The start time of the recorded exercise.                                                    | [optional] |
| **steps**                   | **int**      | Number of steps recorded during the exercise.                                               | [optional] |

## Example

```python
from fitbit_web_api.models.activity_log import ActivityLog

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityLog from a JSON string
activity_log_instance = ActivityLog.from_json(json)
# print the JSON string representation of the object
print(ActivityLog.to_json())

# convert the object into a dict
activity_log_dict = activity_log_instance.to_dict()
# create an instance of ActivityLog from a dict
activity_log_from_dict = ActivityLog.from_dict(activity_log_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
