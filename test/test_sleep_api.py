"""
Unit tests for SleepApi.
"""

from collections.abc import AsyncGenerator, Callable
from datetime import date
from typing import Any, Dict

import pytest

import fitbit_web_api
from fitbit_web_api.api.sleep_api import SleepApi

SLEEP_LIST_PATH = "/1.2/user/-/sleep/list.json"


@pytest.fixture
async def sleep_api(
    api_client: fitbit_web_api.ApiClient,
) -> AsyncGenerator[SleepApi, None]:
    yield SleepApi(api_client)


async def test_get_sleep_list(
    sleep_api: SleepApi,
    responses: Dict[str, Any],
    load_test_data: Callable[[str], Any],
) -> None:
    """Test case for get_sleep_list."""
    sleep_data = load_test_data("sleep_log_list.json")
    responses[SLEEP_LIST_PATH] = sleep_data

    response = await sleep_api.get_sleep_list(
        after_date=date(2023, 1, 1),
        sort="desc",
        offset=0,
        limit=1,
    )

    assert response.sleep is not None
    assert len(response.sleep) == 1
    sleep_log = response.sleep[0]
    assert sleep_log.log_id == 9876543210
    assert sleep_log.efficiency == 95
    assert sleep_log.duration == 28800000
    assert response.pagination is not None
    assert response.pagination.limit == 1
    assert response.summary is not None
    assert response.summary.total_minutes_asleep == 480
