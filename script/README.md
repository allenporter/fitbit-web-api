# Scripts

The scripts in this directory are used to generate the python client library from the public Fitbit OpenAPI specification.

## Schema Generation

The `generate-schema.sh` script is used to download the latest schema from the
Fitbit API. This script downloads the swagger file and converts it to an
OpenAPI specification (`openapi/fitbit-web-api-openapi.json`).

## Schema Upgrades

The upstream Fitbit OpenAPI specification is incomplete and is missing response
schemas for most API endpoints. The `upgrade-schema.py` script is used to
fix these issues and produce a more complete schema.

The script takes `openapi/fitbit-web-api-openapi.json` as input and produces
`openapi/fitbit-web-api-openapi-fixed.json` as output. This fixed schema is
then used for API generation.

The upgrade process works as follows:

1.  **Bug Fixes**: The script applies a series of hardcoded fixes for known
    issues in the upstream schema.
2.  **Dynamic Schema Loading**: The script dynamically loads all `*.json` files
    from the `openapi/model/` directory. Each file is expected to contain a
    JSON schema definition for a single data model or API response. The filename
    is converted from `snake_case` to `PascalCase` to create the schema name
    (e.g., `get_sleep_goal_response.json` becomes `GetSleepGoalResponse`).
3.  **Response Mapping**: A `PATH_CONFIG` dictionary within the script maps API
    paths (e.g., `/1.2/user/-/sleep/goal.json`) to their corresponding response
    schemas that were loaded in the previous step.

This approach allows for a maintainable way to augment the upstream schema with
missing information. To add a new response schema, one would typically:

1.  Create a new JSON schema file in `openapi/model/` for the response object.
2.  Create another JSON schema file in `openapi/model/` for the data model if needed.
3.  Update the `paths/` with a config file that links the API to the new response schema.

## Schema Coverage

This section tracks the progress of enhancing the OpenAPI schema with response
objects. The Fitbit Web API schema includes all of the request objects, but it is
missing the response objects. Therefore we have a process of reviewing the FitBit
developer documentation examples and building a schema out of this. Once the schema
is created, we use the above tooling to re-generate the code.

### Adding new response schemas:

Follow these steps to add a new schema:

1. Review the [Developer Guide](https://dev.fitbit.com/build/reference/web-api/) to get an idea for all the things that exist in the API. Each sub-page has more details on the specific request/response object types. For example,
   the page https://dev.fitbit.com/build/reference/web-api/sleep/get-sleep-goals/ is for the `Get Sleep Goal` command
   which has a response description:

```
Element Name	Description
goal : bedtime	The user's targeted bedtime.
goal : minDuration	Length of the sleep goal period in minutes.
goal : updatedOn	The timestamp that the goal was created/updated.
goal : wakeupTime	The user's targeted wake time.
```

With example output:

```json
{
  "goal": {
    "bedtime": "22:00",
    "minDuration": 600,
    "updatedOn": "2025-05-01T20:00:00.000Z",
    "wakeupTime": "07:00"
  }
}
```

2. Review the existing schemas in `openapi/model/` and the list below of completed API categories to understand what already exists. These are the examples of the output format we want.

Example `openapi/model/sleep_goal.json` content:

```json
{
  "type": "object",
  "properties": {
    "updatedOn": {
      "type": "string",
      "format": "date-time",
      "description": "The timestamp that the goal was created/updated."
    },
    "minDuration": {
      "type": "integer",
      "description": "Length of the sleep goal period in minutes."
    },
    "bedtime": {
      "type": "string",
      "description": "The user's targeted bedtime."
    },
    "wakeupTime": {
      "type": "string",
      "description": "The user's targeted wake time."
    }
  }
}
```

3. Specific paths to their response object types are mapped in `paths/` such as these examples:

Example from `openapi/model/sleep/get_sleep_goal_response.json`:

```
{
  "type": "object",
  "properties": {
    "goal": {
      "$ref": "#/components/schemas/SleepGoal"
    }
  }
}
```

Example from `openapi/paths/sleep_paths.json`:

```json
{
  "/1.2/user/-/sleep/goal.json": {
    "get": {
      "200": "GetSleepGoalResponse"
    },
    ...
  }
}
```

### Completed API Categories

- Active Zone Minutes Time Series
- Activity
- Activity Time Series
- Body
- Body Time Series
- Breathing Rate
- Cardio Fitness Score (VO2 Max)
- Devices
- Electrocardiogram
- Friends
- Heart Rate Time Series
- Heart Rate Variability
- Irregular Rhythm Notifications
- Nutrition
- Nutrition Time Series
- Sleep
- SpO2
- Subscriptions
- Temperature
- User

### Remaining API Categories

The following API categories still need to be updated with response schemas:

- Active Zone Minutes Intraday Time Series
- Activity Intraday Time Series
- Breathing Rate Intraday
- Heart Rate Intraday Time Series
- Heart Rate Variability Intraday
- SpO2 Intraday

## API Generation

The `generate-api.sh` script is used to generate the python client
library from the OpenAPI specification. This uses the `openapi-generator-cli`
to generate a `python-aiohttp` client from the `openapi/fitbit-web-api-openapi-fixed.json` file.
