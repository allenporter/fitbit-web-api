"""
Unit tests for BodyApi.
"""

from collections.abc import AsyncGenerator, Callable
from datetime import date
from typing import Any, Dict

import pytest

import fitbit_web_api
from fitbit_web_api.api.body_api import BodyApi

WEIGHT_LOG_DATE_PATH = "/1/user/-/body/log/weight/date/2023-01-01.json"


@pytest.fixture
async def body_api(
    api_client: fitbit_web_api.ApiClient,
) -> AsyncGenerator[BodyApi, None]:
    yield BodyApi(api_client)


async def test_get_weight_by_date(
    body_api: BodyApi,
    responses: Dict[str, Any],
    load_test_data: Callable[[str], Any],
) -> None:
    """Test case for get_weight_by_date."""
    weight_data = load_test_data("weight_log_list.json")
    responses[WEIGHT_LOG_DATE_PATH] = weight_data

    response = await body_api.get_weight_by_date(
        var_date=date(2023, 1, 1),
    )

    assert response.weight is not None
    assert len(response.weight) == 1
    weight_entry = response.weight[0]
    assert weight_entry.log_id == 1234567890
    assert weight_entry.weight == 72.5
    assert weight_entry.bmi == 23.57
    assert weight_entry.source == "API"


# TODO: Add tests for mutable methods
# These are placeholders to track missing test coverage for write operations


@pytest.mark.skip(reason="TODO: Implement test for add_weight_log")
async def test_add_weight_log(body_api: BodyApi) -> None:
    """Test case for add_weight_log - Log Weight."""
    pass


@pytest.mark.skip(reason="TODO: Implement test for delete_weight_log")
async def test_delete_weight_log(body_api: BodyApi) -> None:
    """Test case for delete_weight_log - Delete Weight Log."""
    pass


@pytest.mark.skip(reason="TODO: Implement test for update_weight_goal")
async def test_update_weight_goal(body_api: BodyApi) -> None:
    """Test case for update_weight_goal - Update Weight Goal."""
    pass


@pytest.mark.skip(reason="TODO: Implement test for add_body_fat_log")
async def test_add_body_fat_log(body_api: BodyApi) -> None:
    """Test case for add_body_fat_log - Log Body Fat."""
    pass


@pytest.mark.skip(reason="TODO: Implement test for delete_body_fat_log")
async def test_delete_body_fat_log(body_api: BodyApi) -> None:
    """Test case for delete_body_fat_log - Delete Body Fat Log."""
    pass


@pytest.mark.skip(reason="TODO: Implement test for update_body_fat_goal")
async def test_update_body_fat_goal(body_api: BodyApi) -> None:
    """Test case for update_body_fat_goal - Update Body Fat Goal."""
    pass
