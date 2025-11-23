"""
Unit tests for the User model.
"""

from collections.abc import Callable
from datetime import date
from typing import Any, Dict

from fitbit_web_api.models.user import User


def test_user_model_instantiation() -> None:
    """Test that the User model can be instantiated with required fields."""
    user = User(
        encoded_id="12345",
        display_name="Test User",
        full_name="Test User Full",
    )
    assert user.encoded_id == "12345"
    assert user.display_name == "Test User"
    assert user.full_name == "Test User Full"


def test_user_model_from_dict(load_test_data: Callable[[str], Any]) -> None:
    """Test that the User model can be created from a dictionary."""
    data: Dict[str, Any] = load_test_data("user_profile.json")
    user = User.from_dict(data["user"])
    assert user.encoded_id == "some-profile-id"
    assert user.display_name == "Display name"
    assert user.full_name == "Full name"
    assert user.date_of_birth == date(1990, 1, 1)
    assert user.average_daily_steps == 10000
    assert user.height == 180.0
    assert user.weight == 75.0


def test_user_model_to_dict() -> None:
    """Test that the User model can be serialized to a dictionary."""
    user = User(
        encoded_id="12345",
        display_name="Test User",
        full_name="Test User Full",
        date_of_birth=date(1990, 1, 1),
    )
    data = user.to_dict()
    assert data["encodedId"] == "12345"
    assert data["displayName"] == "Test User"
    assert data["fullName"] == "Test User Full"
    assert data["dateOfBirth"] == date(1990, 1, 1)
