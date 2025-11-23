"""
Unit tests for ActivityApi.
"""

from collections.abc import AsyncGenerator, Callable
from datetime import date
from typing import Any, Dict

import pytest

import fitbit_web_api
from fitbit_web_api.api.activity_api import ActivityApi

ACTIVITIES_LIST_PATH = "/1/user/-/activities/list.json"


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
