"""
Unit tests for ActivityApi.
"""

from collections.abc import AsyncGenerator, Callable
from datetime import date
from typing import Any, Dict

import pytest

import fitbit_web_api
from fitbit_web_api.api.activity_api import ActivityApi

ACTIVITIES_PATH = "/1/user/-/activities.json"
ACTIVITIES_LIST_PATH = "/1/user/-/activities/list.json"
DELETE_ACTIVITY_PATH = "/1/user/-/activities/{activity-log-id}.json"

@pytest.fixture
async def activity_api(
    api_client: fitbit_web_api.ApiClient,
) -> AsyncGenerator[ActivityApi, None]:
    yield ActivityApi(api_client)


async def test_get_activities_log_list(
    activity_api: ActivityApi,
    responses: Dict[str, Any],
    load_test_data: Callable[[str], Any],
) -> None:
    """Test case for get_activities_log_list."""
    activity_data = load_test_data("activity_log_list.json")
    responses[ACTIVITIES_LIST_PATH] = activity_data

    response = await activity_api.get_activities_log_list(
        after_date=date(2023, 1, 1),
        sort="desc",
        offset=0,
        limit=1,
    )

    assert response.activities is not None
    assert len(response.activities) == 1
    activity = response.activities[0]
    assert activity.activity_id == 51007
    assert activity.name == "Walking"
    assert activity.duration == 3600000
    assert response.pagination is not None
    assert response.pagination.limit == 1


async def test_add_activities_log(
    activity_api: ActivityApi,
    post_responses: Dict[str, Any],
    post_requests: list[tuple[str, dict[str, Any]]],
) -> None:
    """Test case for get_activities_log_list."""
    post_responses[ACTIVITIES_PATH] = {}

    await activity_api.add_activities_log(
        activity_id=90013,
        manual_calories=300,
        start_time="12:00",
        duration_millis=1800000,
        var_date=date(2023, 1, 2),
        distance=2,
        activity_name="Walking",
    )
    assert post_requests == [
        (
            ACTIVITIES_PATH,
            {
                "activityId": "90013",
                "manualCalories": "300",
                "startTime": "12:00",
                "durationMillis": "1800000",
                "date": "2023-01-02",
                "distance": "2",
                "activityName": "Walking",
            },
            {},
        )
    ]


async def test_delete_activities_log(
    activity_api: ActivityApi,
    delete_responses: dict[str, Any],
    delete_requests: list[tuple[str, dict[str, Any]]],
) -> None:
    """Test case for delete_activities_log."""
    log_id = 12345
    delete_path = DELETE_ACTIVITY_PATH.format(**{"activity-log-id": log_id})
    delete_responses[delete_path] = {}

    await activity_api.delete_activities_log(activity_log_id=12345)
    assert delete_requests == [(delete_path, {})]
