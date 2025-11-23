"""
Unit tests for NutritionApi.
"""

from collections.abc import AsyncGenerator, Callable
from datetime import date
from typing import Any, Dict

import pytest

import fitbit_web_api
from fitbit_web_api.api.nutrition_api import NutritionApi

FOOD_LOG_DATE_PATH = "/1/user/-/foods/log/date/2023-01-01.json"


@pytest.fixture
async def nutrition_api(
    api_client: fitbit_web_api.ApiClient,
) -> AsyncGenerator[NutritionApi, None]:
    yield NutritionApi(api_client)


async def test_get_foods_by_date(
    nutrition_api: NutritionApi,
    responses: Dict[str, Any],
    load_test_data: Callable[[str], Any],
) -> None:
    """Test case for get_foods_by_date."""
    food_data = load_test_data("food_log_list.json")
    responses[FOOD_LOG_DATE_PATH] = food_data

    response = await nutrition_api.get_foods_by_date(
        var_date=date(2023, 1, 1),
    )

    assert response.foods is not None
    assert len(response.foods) == 1
    food_entry = response.foods[0]
    assert food_entry.log_id == 12345
    assert food_entry.is_favorite is True
    assert food_entry.logged_food.name == "Apple"

    assert response.goals is not None
    assert response.goals.calories == 2000

    assert response.summary is not None
    assert response.summary.calories == 150


# TODO: Add tests for mutable methods
# These are placeholders to track missing test coverage for write operations


@pytest.mark.skip(reason="TODO: Implement test for add_foods_log")
async def test_add_foods_log(nutrition_api: NutritionApi) -> None:
    """Test case for add_foods_log - Log Food."""
    pass


@pytest.mark.skip(reason="TODO: Implement test for delete_foods_log")
async def test_delete_foods_log(nutrition_api: NutritionApi) -> None:
    """Test case for delete_foods_log - Delete Food Log."""
    pass


@pytest.mark.skip(reason="TODO: Implement test for edit_foods_log")
async def test_edit_foods_log(nutrition_api: NutritionApi) -> None:
    """Test case for edit_foods_log - Edit Food Log."""
    pass


@pytest.mark.skip(reason="TODO: Implement test for add_water_log")
async def test_add_water_log(nutrition_api: NutritionApi) -> None:
    """Test case for add_water_log - Log Water."""
    pass


@pytest.mark.skip(reason="TODO: Implement test for delete_water_log")
async def test_delete_water_log(nutrition_api: NutritionApi) -> None:
    """Test case for delete_water_log - Delete Water Log."""
    pass


@pytest.mark.skip(reason="TODO: Implement test for update_water_log")
async def test_update_water_log(nutrition_api: NutritionApi) -> None:
    """Test case for update_water_log - Update Water Log."""
    pass
