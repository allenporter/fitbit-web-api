"""
Unit tests for FoodLogEntry model.
"""

from collections.abc import Callable
from typing import Any

from fitbit_web_api.models.food_log_entry import FoodLogEntry


def test_food_log_entry_model_instantiation() -> None:
    """Test instantiation of FoodLogEntry model."""
    food_log_entry = FoodLogEntry(
        log_id=12345,
        is_favorite=True,
    )
    assert food_log_entry.log_id == 12345
    assert food_log_entry.is_favorite is True


def test_food_log_entry_model_from_dict(load_test_data: Callable[[str], Any]) -> None:
    """Test creating FoodLogEntry from dictionary."""
    data = load_test_data("food_log_list.json")
    food_entry_data = data["foods"][0]
    food_log_entry = FoodLogEntry.from_dict(food_entry_data)

    assert food_log_entry is not None
    assert food_log_entry.log_id == 12345
    assert food_log_entry.is_favorite is True
    assert food_log_entry.logged_food is not None
    assert food_log_entry.logged_food.name == "Apple"
    assert food_log_entry.nutritional_values is not None
    assert food_log_entry.nutritional_values.calories == 150


def test_food_log_entry_model_to_dict(load_test_data: Callable[[str], Any]) -> None:
    """Test converting FoodLogEntry to dictionary."""
    data = load_test_data("food_log_list.json")
    food_entry_data = data["foods"][0]
    food_log_entry = FoodLogEntry.from_dict(food_entry_data)

    assert food_log_entry is not None
    food_entry_dict = food_log_entry.to_dict()

    assert food_entry_dict["logId"] == 12345
    assert food_entry_dict["isFavorite"] is True
    assert food_entry_dict["loggedFood"]["name"] == "Apple"
