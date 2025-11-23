# Testing Guide

This guide outlines the testing approach for the Fitbit Web API project. It is designed to help developers and agents understand the existing testing patterns and add new tests effectively.

## Testing Philosophy

We use `pytest` as our testing framework. The tests are divided into two main categories:

1.  **Model Tests**: Unit tests for data models (e.g., `User`, `Device`). These tests verify that models can be instantiated correctly, and can be serialized/deserialized to/from JSON.
2.  **API Tests**: Integration-style tests for API clients (e.g., `UserApi`, `DevicesApi`). These tests verify that the API client methods correctly make requests and parse responses. We use mocking to simulate network calls.

## Environment Setup

This project uses `uv`. The environment should already be set up.

> [!IMPORTANT]
> **Do not attempt to fix the environment or add missing dependencies.**
> If `uv run pytest` fails due to missing dependencies, assume it is a configuration issue outside the scope of adding tests.

## Running Tests

To run all tests:

```bash
uv run pytest
```

To run a specific test file:

```bash
uv run pytest test/test_user_api.py
```

## Writing Model Tests

Model tests are located in `test/test_<model_name>.py`. They should cover:

*   **Instantiation**: Verify the model can be created with required fields.
*   **From Dict**: Verify the model can be created from a dictionary (deserialization).
*   **To Dict**: Verify the model can be converted back to a dictionary (serialization).

**Example (`test/test_device.py`):**

```python
def test_device_model_from_dict(load_test_data):
    data = load_test_data("devices.json")
    device = Device.from_dict(data[0])
    assert device.battery == "Medium"
```

## Writing API Tests

API tests are located in `test/test_<api_name>_api.py`. They use `pytest-asyncio` for async support.

**Key Components:**

*   **`api_client` fixture**: Provides a configured `ApiClient`.
*   **`responses` fixture**: Used to mock API responses.
*   **`load_test_data` fixture**: Helper to load JSON data from `test/data/`.

**Pattern:**

1.  **Mock the Endpoint**: Use `responses` to define what the API should return for a specific URL.
2.  **Call the API**: Call the method on the API client.
3.  **Assert**: Verify the returned object matches expectations.

**Example (`test/test_devices_api.py`):**

```python
async def test_get_devices(devices_api, responses, load_test_data):
    # 1. Prepare data
    devices_data = load_test_data("devices.json")
    responses["/1/user/-/devices.json"] = devices_data

    # 2. Call API
    devices = await devices_api.get_devices()

    # 3. Assert
    assert len(devices) == 2
    assert devices[0].device_version == "Charge 2"
```

## Test Data

Test data is stored in `test/data/` as JSON files.
*   Use `load_test_data("filename.json")` to load this data in your tests.
*   Keep data realistic by using examples from the official documentation.

## Finding Example Requests/Responses

To write accurate tests, we need real-world example responses. We use the [Fitbit Web API Reference](https://dev.fitbit.com/build/reference/web-api/) for this.

**How to navigate:**

1.  Go to [https://dev.fitbit.com/build/reference/web-api/](https://dev.fitbit.com/build/reference/web-api/).
2.  Select the category you are testing (e.g., "Devices", "User").
3.  Click on the specific endpoint (e.g., "Get Devices").
4.  Scroll down to the **Example Response** section.
5.  Copy the JSON content.
6.  Create a new file in `test/data/` (e.g., `devices.json`) and paste the content there.
7.  Use this data in your tests to mock the API response.

**Example Workflow:**

1.  **Task**: Add tests for "Get Activity Log List".
2.  **Find Docs**: Navigate to **Activity** -> **Get Activity Log List**.
3.  **Get Data**: Copy the JSON from "Example Response".
4.  **Save Data**: Save to `test/data/activity_log_list.json`.
5.  **Write Test**: Create `test/test_activity_api.py`, load the data, mock the endpoint, and assert the parsed objects.
