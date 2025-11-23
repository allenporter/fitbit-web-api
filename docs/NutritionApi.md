# fitbit_web_api.NutritionApi

All URIs are relative to *https://api.fitbit.com*

| Method                                                             | HTTP request                                             | Description          |
| ------------------------------------------------------------------ | -------------------------------------------------------- | -------------------- |
| [**add_favorite_food**](NutritionApi.md#add_favorite_food)         | **POST** /1/user/-/foods/log/favorite/{food-id}.json     | Add Favorite Food    |
| [**add_foods**](NutritionApi.md#add_foods)                         | **POST** /1/user/-/foods.json                            | Create Food          |
| [**add_foods_log**](NutritionApi.md#add_foods_log)                 | **POST** /1/user/-/foods/log.json                        | Log Food             |
| [**add_meal**](NutritionApi.md#add_meal)                           | **POST** /1/user/-/meals.json                            | Create Meal          |
| [**add_update_foods_goal**](NutritionApi.md#add_update_foods_goal) | **POST** /1/user/-/foods/log/goal.json                   | Update Food Goal     |
| [**add_update_water_goal**](NutritionApi.md#add_update_water_goal) | **POST** /1/user/-/foods/log/water/goal.json             | Update Water Goal    |
| [**add_water_log**](NutritionApi.md#add_water_log)                 | **POST** /1/user/-/foods/log/water.json                  | Log Water            |
| [**delete_favorite_food**](NutritionApi.md#delete_favorite_food)   | **DELETE** /1/user/-/foods/log/favorite/{food-id}.json   | Delete Favorite Food |
| [**delete_foods**](NutritionApi.md#delete_foods)                   | **DELETE** /1/user/-/foods/{food-id}.json                | Delete Custom Food   |
| [**delete_foods_log**](NutritionApi.md#delete_foods_log)           | **DELETE** /1/user/-/foods/log/{food-log-id}.json        | Delete Food Log      |
| [**delete_meal**](NutritionApi.md#delete_meal)                     | **DELETE** /1/user/-/meals/{meal-id}.json                | Delete Meal          |
| [**delete_water_log**](NutritionApi.md#delete_water_log)           | **DELETE** /1/user/-/foods/log/water/{water-log-id}.json | Delete Water Log     |
| [**edit_foods_log**](NutritionApi.md#edit_foods_log)               | **POST** /1/user/-/foods/log/{food-log-id}.json          | Edit Food Log        |
| [**get_favorite_foods**](NutritionApi.md#get_favorite_foods)       | **GET** /1/user/-/foods/log/favorite.json                | Get Favorite Foods   |
| [**get_foods_by_date**](NutritionApi.md#get_foods_by_date)         | **GET** /1/user/-/foods/log/date/{date}.json             | Get Food Logs        |
| [**get_foods_goal**](NutritionApi.md#get_foods_goal)               | **GET** /1/user/-/foods/log/goal.json                    | Get Food Goals       |
| [**get_foods_info**](NutritionApi.md#get_foods_info)               | **GET** /1/foods/{food-id}.json                          | Get Food             |
| [**get_foods_list**](NutritionApi.md#get_foods_list)               | **GET** /1/foods/search.json                             | Search Foods         |
| [**get_foods_locales**](NutritionApi.md#get_foods_locales)         | **GET** /1/foods/locales.json                            | Get Food Locales     |
| [**get_foods_units**](NutritionApi.md#get_foods_units)             | **GET** /1/foods/units.json                              | Get Food Units       |
| [**get_frequent_foods**](NutritionApi.md#get_frequent_foods)       | **GET** /1/user/-/foods/log/frequent.json                | Get Frequent Foods   |
| [**get_meal**](NutritionApi.md#get_meal)                           | **GET** /1/user/-/meals/{meal-id}.json                   | Get Meal             |
| [**get_meals**](NutritionApi.md#get_meals)                         | **GET** /1/user/-/meals.json                             | Get Meals            |
| [**get_recent_foods**](NutritionApi.md#get_recent_foods)           | **GET** /1/user/-/foods/log/recent.json                  | Get Recent Foods     |
| [**get_water_by_date**](NutritionApi.md#get_water_by_date)         | **GET** /1/user/-/foods/log/water/date/{date}.json       | Get Water Logs       |
| [**get_water_goal**](NutritionApi.md#get_water_goal)               | **GET** /1/user/-/foods/log/water/goal.json              | Get Water Goal       |
| [**update_meal**](NutritionApi.md#update_meal)                     | **POST** /1/user/-/meals/{meal-id}.json                  | Update Meal          |
| [**update_water_log**](NutritionApi.md#update_water_log)           | **POST** /1/user/-/foods/log/water/{water-log-id}.json   | Update Water Log     |

# **add_favorite_food**

> add_favorite_food(food_id)

Add Favorite Food

Updates a user's daily activity goals and returns a response using units in the unit system which corresponds to the Accept-Language header provided.

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
    api_instance = fitbit_web_api.NutritionApi(api_client)
    food_id = 'food_id_example' # str | The ID of the food to be added to user's favorites.

    try:
        # Add Favorite Food
        await api_instance.add_favorite_food(food_id)
    except Exception as e:
        print("Exception when calling NutritionApi->add_favorite_food: %s\n" % e)
```

### Parameters

| Name        | Type    | Description                                             | Notes |
| ----------- | ------- | ------------------------------------------------------- | ----- |
| **food_id** | **str** | The ID of the food to be added to user&#39;s favorites. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details

| Status code | Description                                                             | Response headers |
| ----------- | ----------------------------------------------------------------------- | ---------------- |
| **200**     | Successful request.                                                     | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified. | -                |
| **401**     | The request requires user authentication.                               | -                |
| **403**     | The server understood the request, but is refusing to fulfill it.       | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_foods**

> add_foods(name, default_food_measurement_unit_id, default_serving_size, calories, form_type=form_type, description=description)

Create Food

Creates a new private food for a user and returns a response in the format requested. The created food is found via the Search Foods call.

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
    api_instance = fitbit_web_api.NutritionApi(api_client)
    name = 'name_example' # str | The food name.
    default_food_measurement_unit_id = 'default_food_measurement_unit_id_example' # str | The ID of the default measurement unit. Full list of units can be retrieved via the Get Food Units endpoint.
    default_serving_size = 'default_serving_size_example' # str | The size of the default serving. Nutrition values should be provided for this serving size.
    calories = 'calories_example' # str | The calories in the default serving size.
    form_type = 'form_type_example' # str | Form type; LIQUID or DRY. (optional)
    description = 'description_example' # str | The description of the food. (optional)

    try:
        # Create Food
        await api_instance.add_foods(name, default_food_measurement_unit_id, default_serving_size, calories, form_type=form_type, description=description)
    except Exception as e:
        print("Exception when calling NutritionApi->add_foods: %s\n" % e)
```

### Parameters

| Name                                 | Type    | Description                                                                                                  | Notes      |
| ------------------------------------ | ------- | ------------------------------------------------------------------------------------------------------------ | ---------- |
| **name**                             | **str** | The food name.                                                                                               |
| **default_food_measurement_unit_id** | **str** | The ID of the default measurement unit. Full list of units can be retrieved via the Get Food Units endpoint. |
| **default_serving_size**             | **str** | The size of the default serving. Nutrition values should be provided for this serving size.                  |
| **calories**                         | **str** | The calories in the default serving size.                                                                    |
| **form_type**                        | **str** | Form type; LIQUID or DRY.                                                                                    | [optional] |
| **description**                      | **str** | The description of the food.                                                                                 | [optional] |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details

| Status code | Description                                                                  | Response headers |
| ----------- | ---------------------------------------------------------------------------- | ---------------- |
| **201**     | The request has been fulfilled and resulted in a new resource being created. | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified.      | -                |
| **401**     | The request requires user authentication.                                    | -                |
| **403**     | The server understood the request, but is refusing to fulfill it.            | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_foods_log**

> add_foods_log(food_id, meal_type_id, unit_id, amount, var_date, food_name=food_name, favorite=favorite, brand_name=brand_name, calories=calories)

Log Food

Creates food log entries for users with or without foodId value.

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
    api_instance = fitbit_web_api.NutritionApi(api_client)
    food_id = 'food_id_example' # str | The ID of the food to be logged. Either foodId or foodName must be provided.
    meal_type_id = 'meal_type_id_example' # str | Meal types. 1=Breakfast; 2=Morning Snack; 3=Lunch; 4=Afternoon Snack; 5=Dinner; 7=Anytime.
    unit_id = 'unit_id_example' # str | The ID of units used. Typically retrieved via a previous call to Get Food Logs, Search Foods, or Get Food Units.
    amount = 'amount_example' # str | The amount consumed in the format X.XX in the specified unitId.
    var_date = '2013-10-20' # date | Log entry date in the format yyyy-MM-dd.
    food_name = 'food_name_example' # str | Food entry name. Either foodId or foodName must be provided. (optional)
    favorite = True # bool | The `true` value will add the food to the user's favorites after creating the log entry; while the `false` value will not. Valid only with foodId value. (optional)
    brand_name = 'brand_name_example' # str | Brand name of food. Valid only with foodName parameters. (optional)
    calories = 56 # int | Calories for this serving size. This is allowed with foodName parameter (default to zero); otherwise it is ignored. (optional)

    try:
        # Log Food
        await api_instance.add_foods_log(food_id, meal_type_id, unit_id, amount, var_date, food_name=food_name, favorite=favorite, brand_name=brand_name, calories=calories)
    except Exception as e:
        print("Exception when calling NutritionApi->add_foods_log: %s\n" % e)
```

### Parameters

| Name             | Type     | Description                                                                                                                                                                      | Notes      |
| ---------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **food_id**      | **str**  | The ID of the food to be logged. Either foodId or foodName must be provided.                                                                                                     |
| **meal_type_id** | **str**  | Meal types. 1&#x3D;Breakfast; 2&#x3D;Morning Snack; 3&#x3D;Lunch; 4&#x3D;Afternoon Snack; 5&#x3D;Dinner; 7&#x3D;Anytime.                                                         |
| **unit_id**      | **str**  | The ID of units used. Typically retrieved via a previous call to Get Food Logs, Search Foods, or Get Food Units.                                                                 |
| **amount**       | **str**  | The amount consumed in the format X.XX in the specified unitId.                                                                                                                  |
| **var_date**     | **date** | Log entry date in the format yyyy-MM-dd.                                                                                                                                         |
| **food_name**    | **str**  | Food entry name. Either foodId or foodName must be provided.                                                                                                                     | [optional] |
| **favorite**     | **bool** | The &#x60;true&#x60; value will add the food to the user&#39;s favorites after creating the log entry; while the &#x60;false&#x60; value will not. Valid only with foodId value. | [optional] |
| **brand_name**   | **str**  | Brand name of food. Valid only with foodName parameters.                                                                                                                         | [optional] |
| **calories**     | **int**  | Calories for this serving size. This is allowed with foodName parameter (default to zero); otherwise it is ignored.                                                              | [optional] |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details

| Status code | Description                                                                  | Response headers |
| ----------- | ---------------------------------------------------------------------------- | ---------------- |
| **201**     | The request has been fulfilled and resulted in a new resource being created. | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified.      | -                |
| **401**     | The request requires user authentication.                                    | -                |
| **403**     | The server understood the request, but is refusing to fulfill it.            | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_meal**

> add_meal(meal)

Create Meal

Creates a meal with the given food contained in the post body.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.meal import Meal
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
    api_instance = fitbit_web_api.NutritionApi(api_client)
    meal = fitbit_web_api.Meal() # Meal | Meal to create

    try:
        # Create Meal
        await api_instance.add_meal(meal)
    except Exception as e:
        print("Exception when calling NutritionApi->add_meal: %s\n" % e)
```

### Parameters

| Name     | Type                | Description    | Notes |
| -------- | ------------------- | -------------- | ----- |
| **meal** | [**Meal**](Meal.md) | Meal to create |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details

| Status code | Description                                                             | Response headers |
| ----------- | ----------------------------------------------------------------------- | ---------------- |
| **200**     | Successful request.                                                     | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified. | -                |
| **401**     | The request requires user authentication.                               | -                |
| **403**     | The server understood the request, but is refusing to fulfill it.       | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_update_foods_goal**

> add_update_foods_goal(calories, intensity=intensity, personalized=personalized)

Update Food Goal

Updates a user's daily calories consumption goal or food plan and returns a response in the format requested.

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
    api_instance = fitbit_web_api.NutritionApi(api_client)
    calories = 56 # int | Manual calorie consumption goal in either calories or intensity must be provided.
    intensity = 'intensity_example' # str | Food plan intensity (MAINTENANCE, EASIER, MEDIUM, KINDAHARD, or HARDER). Either calories or intensity must be provided. (optional)
    personalized = 'personalized_example' # str | Food plan type; true or false. (optional)

    try:
        # Update Food Goal
        await api_instance.add_update_foods_goal(calories, intensity=intensity, personalized=personalized)
    except Exception as e:
        print("Exception when calling NutritionApi->add_update_foods_goal: %s\n" % e)
```

### Parameters

| Name             | Type    | Description                                                                                                             | Notes      |
| ---------------- | ------- | ----------------------------------------------------------------------------------------------------------------------- | ---------- |
| **calories**     | **int** | Manual calorie consumption goal in either calories or intensity must be provided.                                       |
| **intensity**    | **str** | Food plan intensity (MAINTENANCE, EASIER, MEDIUM, KINDAHARD, or HARDER). Either calories or intensity must be provided. | [optional] |
| **personalized** | **str** | Food plan type; true or false.                                                                                          | [optional] |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details

| Status code | Description                                                                  | Response headers |
| ----------- | ---------------------------------------------------------------------------- | ---------------- |
| **201**     | The request has been fulfilled and resulted in a new resource being created. | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified.      | -                |
| **401**     | The request requires user authentication.                                    | -                |
| **403**     | The server understood the request, but is refusing to fulfill it.            | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_update_water_goal**

> add_update_water_goal(target)

Update Water Goal

Updates a user's daily calories consumption goal or food plan and returns a response in the format requested.

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
    api_instance = fitbit_web_api.NutritionApi(api_client)
    target = 56 # int | The target water goal in the format X.X is set in unit based on locale.

    try:
        # Update Water Goal
        await api_instance.add_update_water_goal(target)
    except Exception as e:
        print("Exception when calling NutritionApi->add_update_water_goal: %s\n" % e)
```

### Parameters

| Name       | Type    | Description                                                             | Notes |
| ---------- | ------- | ----------------------------------------------------------------------- | ----- |
| **target** | **int** | The target water goal in the format X.X is set in unit based on locale. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details

| Status code | Description                                                                  | Response headers |
| ----------- | ---------------------------------------------------------------------------- | ---------------- |
| **201**     | The request has been fulfilled and resulted in a new resource being created. | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified.      | -                |
| **401**     | The request requires user authentication.                                    | -                |
| **403**     | The server understood the request, but is refusing to fulfill it.            | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_water_log**

> add_water_log(var_date, amount, unit=unit)

Log Water

Creates a log entry for water using units in the unit systems that corresponds to the Accept-Language header provided.

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
    api_instance = fitbit_web_api.NutritionApi(api_client)
    var_date = '2013-10-20' # date | The date of records to be returned in the format yyyy-MM-dd.
    amount = 56 # int | The amount consumption in the format X.XX and in the specified waterUnit or in the unit system that corresponds to the Accept-Language header provided.
    unit = 'unit_example' # str | Water measurement unit; `ml`, `fl oz`, or `cup`. (optional)

    try:
        # Log Water
        await api_instance.add_water_log(var_date, amount, unit=unit)
    except Exception as e:
        print("Exception when calling NutritionApi->add_water_log: %s\n" % e)
```

### Parameters

| Name         | Type     | Description                                                                                                                                             | Notes      |
| ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **var_date** | **date** | The date of records to be returned in the format yyyy-MM-dd.                                                                                            |
| **amount**   | **int**  | The amount consumption in the format X.XX and in the specified waterUnit or in the unit system that corresponds to the Accept-Language header provided. |
| **unit**     | **str**  | Water measurement unit; &#x60;ml&#x60;, &#x60;fl oz&#x60;, or &#x60;cup&#x60;.                                                                          | [optional] |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details

| Status code | Description                                                                  | Response headers |
| ----------- | ---------------------------------------------------------------------------- | ---------------- |
| **201**     | The request has been fulfilled and resulted in a new resource being created. | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified.      | -                |
| **401**     | The request requires user authentication.                                    | -                |
| **403**     | The server understood the request, but is refusing to fulfill it.            | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_favorite_food**

> delete_favorite_food(food_id)

Delete Favorite Food

Deletes a food with the given ID to the user's list of favorite foods.

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
    api_instance = fitbit_web_api.NutritionApi(api_client)
    food_id = 'food_id_example' # str | The ID of the food to be deleted from user's favorites.

    try:
        # Delete Favorite Food
        await api_instance.delete_favorite_food(food_id)
    except Exception as e:
        print("Exception when calling NutritionApi->delete_favorite_food: %s\n" % e)
```

### Parameters

| Name        | Type    | Description                                                 | Notes |
| ----------- | ------- | ----------------------------------------------------------- | ----- |
| **food_id** | **str** | The ID of the food to be deleted from user&#39;s favorites. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details

| Status code | Description                                             | Response headers |
| ----------- | ------------------------------------------------------- | ---------------- |
| **204**     | No Content. The request was successful.                 | -                |
| **400**     | Bad Request. The request likely contained bad syntax.   | -                |
| **401**     | Unauthorized. The request requires user authentication. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_foods**

> delete_foods(food_id)

Delete Custom Food

Deletes custom food for a user and returns a response in the format requested.

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
    api_instance = fitbit_web_api.NutritionApi(api_client)
    food_id = 'food_id_example' # str | The ID of the food to be deleted.

    try:
        # Delete Custom Food
        await api_instance.delete_foods(food_id)
    except Exception as e:
        print("Exception when calling NutritionApi->delete_foods: %s\n" % e)
```

### Parameters

| Name        | Type    | Description                       | Notes |
| ----------- | ------- | --------------------------------- | ----- |
| **food_id** | **str** | The ID of the food to be deleted. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details

| Status code | Description                                             | Response headers |
| ----------- | ------------------------------------------------------- | ---------------- |
| **204**     | No Content. The request was successful.                 | -                |
| **400**     | Bad Request. The request likely contained bad syntax.   | -                |
| **401**     | Unauthorized. The request requires user authentication. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_foods_log**

> delete_foods_log(food_log_id)

Delete Food Log

Deletes a user's food log entry with the given ID.

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
    api_instance = fitbit_web_api.NutritionApi(api_client)
    food_log_id = 'food_log_id_example' # str | The ID of the food log entry to be deleted.

    try:
        # Delete Food Log
        await api_instance.delete_foods_log(food_log_id)
    except Exception as e:
        print("Exception when calling NutritionApi->delete_foods_log: %s\n" % e)
```

### Parameters

| Name            | Type    | Description                                 | Notes |
| --------------- | ------- | ------------------------------------------- | ----- |
| **food_log_id** | **str** | The ID of the food log entry to be deleted. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details

| Status code | Description                                             | Response headers |
| ----------- | ------------------------------------------------------- | ---------------- |
| **204**     | No Content. The request was successful.                 | -                |
| **400**     | Bad Request. The request likely contained bad syntax.   | -                |
| **401**     | Unauthorized. The request requires user authentication. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_meal**

> delete_meal(meal_id)

Delete Meal

Deletes a user's meal with the given meal id.

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
    api_instance = fitbit_web_api.NutritionApi(api_client)
    meal_id = 'meal_id_example' # str | Id of the meal to delete.

    try:
        # Delete Meal
        await api_instance.delete_meal(meal_id)
    except Exception as e:
        print("Exception when calling NutritionApi->delete_meal: %s\n" % e)
```

### Parameters

| Name        | Type    | Description               | Notes |
| ----------- | ------- | ------------------------- | ----- |
| **meal_id** | **str** | Id of the meal to delete. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details

| Status code | Description                                             | Response headers |
| ----------- | ------------------------------------------------------- | ---------------- |
| **204**     | No Content. The request was successful.                 | -                |
| **400**     | Bad Request. The request likely contained bad syntax.   | -                |
| **401**     | Unauthorized. The request requires user authentication. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_water_log**

> delete_water_log(water_log_id)

Delete Water Log

Deletes a user's water log entry with the given ID.

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
    api_instance = fitbit_web_api.NutritionApi(api_client)
    water_log_id = 'water_log_id_example' # str | The ID of the waterUnit log entry to be deleted.

    try:
        # Delete Water Log
        await api_instance.delete_water_log(water_log_id)
    except Exception as e:
        print("Exception when calling NutritionApi->delete_water_log: %s\n" % e)
```

### Parameters

| Name             | Type    | Description                                      | Notes |
| ---------------- | ------- | ------------------------------------------------ | ----- |
| **water_log_id** | **str** | The ID of the waterUnit log entry to be deleted. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details

| Status code | Description                                             | Response headers |
| ----------- | ------------------------------------------------------- | ---------------- |
| **204**     | No Content. The request was successful.                 | -                |
| **400**     | Bad Request. The request likely contained bad syntax.   | -                |
| **401**     | Unauthorized. The request requires user authentication. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_foods_log**

> edit_foods_log(food_log_id, meal_type_id, unit_id, amount, calories=calories)

Edit Food Log

The Edit Food Log endpoint changes the quantity or calories consumed for a user's food log entry with the given Food Log ID.

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
    api_instance = fitbit_web_api.NutritionApi(api_client)
    food_log_id = 'food_log_id_example' # str | The ID of the food log entry to be edited.
    meal_type_id = 'meal_type_id_example' # str | Meal types. 1=Breakfast; 2=Morning Snack; 3=Lunch; 4=Afternoon Snack; 5=Dinner; 7=Anytime.
    unit_id = 'unit_id_example' # str | The ID of units used. Typically retrieved via a previous call to Get Food Logs, Search Foods, or Get Food Units.
    amount = 'amount_example' # str | The amount consumed in the format X.XX in the specified unitId.
    calories = 56 # int | Calories for this serving size. This is allowed with foodName parameter (default to zero); otherwise it is ignored. (optional)

    try:
        # Edit Food Log
        await api_instance.edit_foods_log(food_log_id, meal_type_id, unit_id, amount, calories=calories)
    except Exception as e:
        print("Exception when calling NutritionApi->edit_foods_log: %s\n" % e)
```

### Parameters

| Name             | Type    | Description                                                                                                              | Notes      |
| ---------------- | ------- | ------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **food_log_id**  | **str** | The ID of the food log entry to be edited.                                                                               |
| **meal_type_id** | **str** | Meal types. 1&#x3D;Breakfast; 2&#x3D;Morning Snack; 3&#x3D;Lunch; 4&#x3D;Afternoon Snack; 5&#x3D;Dinner; 7&#x3D;Anytime. |
| **unit_id**      | **str** | The ID of units used. Typically retrieved via a previous call to Get Food Logs, Search Foods, or Get Food Units.         |
| **amount**       | **str** | The amount consumed in the format X.XX in the specified unitId.                                                          |
| **calories**     | **int** | Calories for this serving size. This is allowed with foodName parameter (default to zero); otherwise it is ignored.      | [optional] |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details

| Status code | Description                                                             | Response headers |
| ----------- | ----------------------------------------------------------------------- | ---------------- |
| **200**     | Successful request.                                                     | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified. | -                |
| **401**     | The request requires user authentication.                               | -                |
| **403**     | The server understood the request, but is refusing to fulfill it.       | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorite_foods**

> List[Food] get_favorite_foods()

Get Favorite Foods

Returns a list of a user's favorite foods in the format requested. A favorite food in the list provides a quick way to log the food via the Log Food endpoint.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.food import Food
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
    api_instance = fitbit_web_api.NutritionApi(api_client)

    try:
        # Get Favorite Foods
        api_response = await api_instance.get_favorite_foods()
        print("The response of NutritionApi->get_favorite_foods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NutritionApi->get_favorite_foods: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Food]**](Food.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                             | Response headers |
| ----------- | ----------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                   | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified. | -                |
| **401**     | The request requires user authentication.                               | -                |
| **403**     | The server understood the request, but is refusing to fulfill it.       | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_foods_by_date**

> GetFoodLogResponse get_foods_by_date(var_date)

Get Food Logs

Retreives a summary and list of a user's food log entries for a given day in the format requested.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_food_log_response import GetFoodLogResponse
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
    api_instance = fitbit_web_api.NutritionApi(api_client)
    var_date = '2013-10-20' # date | The date of records to be returned. In the format yyyy-MM-dd.

    try:
        # Get Food Logs
        api_response = await api_instance.get_foods_by_date(var_date)
        print("The response of NutritionApi->get_foods_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NutritionApi->get_foods_by_date: %s\n" % e)
```

### Parameters

| Name         | Type     | Description                                                   | Notes |
| ------------ | -------- | ------------------------------------------------------------- | ----- |
| **var_date** | **date** | The date of records to be returned. In the format yyyy-MM-dd. |

### Return type

[**GetFoodLogResponse**](GetFoodLogResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                             | Response headers |
| ----------- | ----------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                   | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified. | -                |
| **401**     | The request requires user authentication.                               | -                |
| **403**     | The server understood the request, but is refusing to fulfill it.       | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_foods_goal**

> GetFoodGoalsResponse get_foods_goal()

Get Food Goals

Returns a user's current daily calorie consumption goal and/or foodPlan value in the format requested.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_food_goals_response import GetFoodGoalsResponse
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
    api_instance = fitbit_web_api.NutritionApi(api_client)

    try:
        # Get Food Goals
        api_response = await api_instance.get_foods_goal()
        print("The response of NutritionApi->get_foods_goal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NutritionApi->get_foods_goal: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetFoodGoalsResponse**](GetFoodGoalsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                             | Response headers |
| ----------- | ----------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                   | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified. | -                |
| **401**     | The request requires user authentication.                               | -                |
| **403**     | The server understood the request, but is refusing to fulfill it.       | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_foods_info**

> GetFoodResponse get_foods_info(food_id)

Get Food

Returns the details of a specific food in the Fitbit food databases or a private food that an authorized user has entered in the format requested.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_food_response import GetFoodResponse
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
    api_instance = fitbit_web_api.NutritionApi(api_client)
    food_id = 'food_id_example' # str | The ID of the food.

    try:
        # Get Food
        api_response = await api_instance.get_foods_info(food_id)
        print("The response of NutritionApi->get_foods_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NutritionApi->get_foods_info: %s\n" % e)
```

### Parameters

| Name        | Type    | Description         | Notes |
| ----------- | ------- | ------------------- | ----- |
| **food_id** | **str** | The ID of the food. |

### Return type

[**GetFoodResponse**](GetFoodResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                             | Response headers |
| ----------- | ----------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                   | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified. | -                |
| **401**     | The request requires user authentication.                               | -                |
| **403**     | The server understood the request, but is refusing to fulfill it.       | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_foods_list**

> SearchFoodsResponse get_foods_list(query)

Search Foods

Returns a list of public foods from the Fitbit food database and private food the user created in the format requested.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.search_foods_response import SearchFoodsResponse
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
    api_instance = fitbit_web_api.NutritionApi(api_client)
    query = 'query_example' # str | The URL-encoded search query.

    try:
        # Search Foods
        api_response = await api_instance.get_foods_list(query)
        print("The response of NutritionApi->get_foods_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NutritionApi->get_foods_list: %s\n" % e)
```

### Parameters

| Name      | Type    | Description                   | Notes |
| --------- | ------- | ----------------------------- | ----- |
| **query** | **str** | The URL-encoded search query. |

### Return type

[**SearchFoodsResponse**](SearchFoodsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                             | Response headers |
| ----------- | ----------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                   | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified. | -                |
| **401**     | The request requires user authentication.                               | -                |
| **403**     | The server understood the request, but is refusing to fulfill it.       | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_foods_locales**

> List[FoodLocale] get_foods_locales()

Get Food Locales

Returns the food locales that the user may choose to search, log, and create food in.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.food_locale import FoodLocale
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
    api_instance = fitbit_web_api.NutritionApi(api_client)

    try:
        # Get Food Locales
        api_response = await api_instance.get_foods_locales()
        print("The response of NutritionApi->get_foods_locales:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NutritionApi->get_foods_locales: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FoodLocale]**](FoodLocale.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                             | Response headers |
| ----------- | ----------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                   | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified. | -                |
| **401**     | The request requires user authentication.                               | -                |
| **403**     | The server understood the request, but is refusing to fulfill it.       | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_foods_units**

> List[FoodUnit] get_foods_units()

Get Food Units

Returns a list of all valid Fitbit food units in the format requested.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.food_unit import FoodUnit
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
    api_instance = fitbit_web_api.NutritionApi(api_client)

    try:
        # Get Food Units
        api_response = await api_instance.get_foods_units()
        print("The response of NutritionApi->get_foods_units:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NutritionApi->get_foods_units: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FoodUnit]**](FoodUnit.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                             | Response headers |
| ----------- | ----------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                   | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified. | -                |
| **401**     | The request requires user authentication.                               | -                |
| **403**     | The server understood the request, but is refusing to fulfill it.       | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_frequent_foods**

> GetFrequentFoodsResponse get_frequent_foods()

Get Frequent Foods

Returns a list of a user's frequent foods in the format requested. A frequent food in the list provides a quick way to log the food via the Log Food endpoint.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_frequent_foods_response import GetFrequentFoodsResponse
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
    api_instance = fitbit_web_api.NutritionApi(api_client)

    try:
        # Get Frequent Foods
        api_response = await api_instance.get_frequent_foods()
        print("The response of NutritionApi->get_frequent_foods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NutritionApi->get_frequent_foods: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetFrequentFoodsResponse**](GetFrequentFoodsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                             | Response headers |
| ----------- | ----------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                   | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified. | -                |
| **401**     | The request requires user authentication.                               | -                |
| **403**     | The server understood the request, but is refusing to fulfill it.       | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meal**

> GetMealResponse get_meal(user_id, meal_id)

Get Meal

Retrieves a single meal created by the user from their food log given the meal id.

### Example

```python
import fitbit_web_api
from fitbit_web_api.models.get_meal_response import GetMealResponse
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
    api_instance = fitbit_web_api.NutritionApi(api_client)
    user_id = '-' # str | The encoded ID of the user. Use '-' (dash) for current logged-in user. (default to '-')
    meal_id = 'meal_id_example' # str | The ID of the meal.

    try:
        # Get Meal
        api_response = await api_instance.get_meal(user_id, meal_id)
        print("The response of NutritionApi->get_meal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NutritionApi->get_meal: %s\n" % e)
```

### Parameters

| Name        | Type    | Description                                                                    | Notes                    |
| ----------- | ------- | ------------------------------------------------------------------------------ | ------------------------ |
| **user_id** | **str** | The encoded ID of the user. Use &#39;-&#39; (dash) for current logged-in user. | [default to &#39;-&#39;] |
| **meal_id** | **str** | The ID of the meal.                                                            |

### Return type

[**GetMealResponse**](GetMealResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description           | Response headers |
| ----------- | --------------------- | ---------------- |
| **200**     | A successful request. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meals**

> GetMealsResponse get_meals()

Get Meals

Returns a list of meals created by user in the user's food log in the format requested. User creates and manages meals on the Food Log tab on the website.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_meals_response import GetMealsResponse
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
    api_instance = fitbit_web_api.NutritionApi(api_client)

    try:
        # Get Meals
        api_response = await api_instance.get_meals()
        print("The response of NutritionApi->get_meals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NutritionApi->get_meals: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetMealsResponse**](GetMealsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                             | Response headers |
| ----------- | ----------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                   | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified. | -                |
| **401**     | The request requires user authentication.                               | -                |
| **403**     | The server understood the request, but is refusing to fulfill it.       | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recent_foods**

> GetRecentFoodsResponse get_recent_foods()

Get Recent Foods

Returns a list of a user's frequent foods in the format requested. A frequent food in the list provides a quick way to log the food via the Log Food endpoint.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_recent_foods_response import GetRecentFoodsResponse
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
    api_instance = fitbit_web_api.NutritionApi(api_client)

    try:
        # Get Recent Foods
        api_response = await api_instance.get_recent_foods()
        print("The response of NutritionApi->get_recent_foods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NutritionApi->get_recent_foods: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetRecentFoodsResponse**](GetRecentFoodsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                             | Response headers |
| ----------- | ----------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                   | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified. | -                |
| **401**     | The request requires user authentication.                               | -                |
| **403**     | The server understood the request, but is refusing to fulfill it.       | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_water_by_date**

> GetWaterLogResponse get_water_by_date(var_date)

Get Water Logs

Retreives a summary and list of a user's water log entries for a given day in the requested using units in the unit system that corresponds to the Accept-Language header provided.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_water_log_response import GetWaterLogResponse
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
    api_instance = fitbit_web_api.NutritionApi(api_client)
    var_date = '2013-10-20' # date | The date of records to be returned. In the format yyyy-MM-dd.

    try:
        # Get Water Logs
        api_response = await api_instance.get_water_by_date(var_date)
        print("The response of NutritionApi->get_water_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NutritionApi->get_water_by_date: %s\n" % e)
```

### Parameters

| Name         | Type     | Description                                                   | Notes |
| ------------ | -------- | ------------------------------------------------------------- | ----- |
| **var_date** | **date** | The date of records to be returned. In the format yyyy-MM-dd. |

### Return type

[**GetWaterLogResponse**](GetWaterLogResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                             | Response headers |
| ----------- | ----------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                   | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified. | -                |
| **401**     | The request requires user authentication.                               | -                |
| **403**     | The server understood the request, but is refusing to fulfill it.       | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_water_goal**

> GetWaterGoalResponse get_water_goal()

Get Water Goal

Retreives a summary and list of a user's water goal entries for a given day in the requested using units in the unit system that corresponds to the Accept-Language header provided.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_water_goal_response import GetWaterGoalResponse
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
    api_instance = fitbit_web_api.NutritionApi(api_client)

    try:
        # Get Water Goal
        api_response = await api_instance.get_water_goal()
        print("The response of NutritionApi->get_water_goal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NutritionApi->get_water_goal: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetWaterGoalResponse**](GetWaterGoalResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description           | Response headers |
| ----------- | --------------------- | ---------------- |
| **200**     | A successful request. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_meal**

> update_meal(meal_id, meal)

Update Meal

Replaces an existing meal with the contents of the request. The response contains the updated meal.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.meal import Meal
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
    api_instance = fitbit_web_api.NutritionApi(api_client)
    meal_id = 'meal_id_example' # str | The ID of the meal.
    meal = fitbit_web_api.Meal() # Meal | Meal to create

    try:
        # Update Meal
        await api_instance.update_meal(meal_id, meal)
    except Exception as e:
        print("Exception when calling NutritionApi->update_meal: %s\n" % e)
```

### Parameters

| Name        | Type                | Description         | Notes |
| ----------- | ------------------- | ------------------- | ----- |
| **meal_id** | **str**             | The ID of the meal. |
| **meal**    | [**Meal**](Meal.md) | Meal to create      |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details

| Status code | Description                                                             | Response headers |
| ----------- | ----------------------------------------------------------------------- | ---------------- |
| **200**     | Successful request.                                                     | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified. | -                |
| **401**     | The request requires user authentication.                               | -                |
| **403**     | The server understood the request, but is refusing to fulfill it.       | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_water_log**

> update_water_log(water_log_id, amount, unit=unit)

Update Water Log

Updates a user's water log entry with the given ID.

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
    api_instance = fitbit_web_api.NutritionApi(api_client)
    water_log_id = 'water_log_id_example' # str | The ID of the waterUnit log entry to be deleted.
    amount = 'amount_example' # str | Amount consumed; in the format X.X and in the specified waterUnit or in the unit system that corresponds to the Accept-Language header provided.
    unit = 'unit_example' # str | Water measurement unit. 'ml', 'fl oz', or 'cup'. (optional)

    try:
        # Update Water Log
        await api_instance.update_water_log(water_log_id, amount, unit=unit)
    except Exception as e:
        print("Exception when calling NutritionApi->update_water_log: %s\n" % e)
```

### Parameters

| Name             | Type    | Description                                                                                                                                      | Notes      |
| ---------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **water_log_id** | **str** | The ID of the waterUnit log entry to be deleted.                                                                                                 |
| **amount**       | **str** | Amount consumed; in the format X.X and in the specified waterUnit or in the unit system that corresponds to the Accept-Language header provided. |
| **unit**         | **str** | Water measurement unit. &#39;ml&#39;, &#39;fl oz&#39;, or &#39;cup&#39;.                                                                         | [optional] |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

### HTTP response details

| Status code | Description                                                             | Response headers |
| ----------- | ----------------------------------------------------------------------- | ---------------- |
| **200**     | Successful request.                                                     | -                |
| **400**     | The request had bad syntax or was inherently impossible to be satified. | -                |
| **401**     | The request requires user authentication.                               | -                |
| **403**     | The server understood the request, but is refusing to fulfill it.       | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
