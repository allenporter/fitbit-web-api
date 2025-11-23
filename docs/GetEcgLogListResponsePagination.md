# GetEcgLogListResponsePagination

## Properties

| Name            | Type     | Description                                                          | Notes      |
| --------------- | -------- | -------------------------------------------------------------------- | ---------- |
| **after_date**  | **date** | The afterDate parameter of the request.                              | [optional] |
| **before_date** | **date** | The beforeDate parameter of the request.                             | [optional] |
| **limit**       | **int**  | The limit parameter of the request.                                  | [optional] |
| **next**        | **str**  | The URL of the request that will fetch the next page of results.     | [optional] |
| **offset**      | **int**  | The offset parameter of the request.                                 | [optional] |
| **previous**    | **str**  | The URL of the request that will fetch the previous page of results. | [optional] |
| **sort**        | **str**  | The sort parameter of the request.                                   | [optional] |

## Example

```python
from fitbit_web_api.models.get_ecg_log_list_response_pagination import GetEcgLogListResponsePagination

# TODO update the JSON string below
json = "{}"
# create an instance of GetEcgLogListResponsePagination from a JSON string
get_ecg_log_list_response_pagination_instance = GetEcgLogListResponsePagination.from_json(json)
# print the JSON string representation of the object
print(GetEcgLogListResponsePagination.to_json())

# convert the object into a dict
get_ecg_log_list_response_pagination_dict = get_ecg_log_list_response_pagination_instance.to_dict()
# create an instance of GetEcgLogListResponsePagination from a dict
get_ecg_log_list_response_pagination_from_dict = GetEcgLogListResponsePagination.from_dict(get_ecg_log_list_response_pagination_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
