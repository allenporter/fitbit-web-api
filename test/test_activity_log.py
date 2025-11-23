"""
Unit tests for the ActivityLog model.
"""

from collections.abc import Callable
from datetime import date
from typing import Any, Dict, List

from fitbit_web_api.models.activity_log import ActivityLog


def test_activity_log_model_instantiation() -> None:
    """Test that the ActivityLog model can be instantiated with required fields."""
    activity_log = ActivityLog(
        activity_id=12345,
        duration=3600000,
        name="Walking",
        start_date=date(2023, 1, 1),
        start_time="12:00:00",
    )
    assert activity_log.activity_id == 12345
    assert activity_log.duration == 3600000
    assert activity_log.name == "Walking"
    assert activity_log.start_date == date(2023, 1, 1)
    assert activity_log.start_time == "12:00:00"


def test_activity_log_model_from_dict(load_test_data: Callable[[str], Any]) -> None:
    """Test that the ActivityLog model can be created from a dictionary."""
    data: Dict[str, Any] = load_test_data("activity_log_list.json")
    activity_data = data["activities"][0]
    activity_log = ActivityLog.from_dict(activity_data)
    
    assert activity_log is not None
    assert activity_log.activity_id == 51007
    assert activity_log.name == "Walking"
    assert activity_log.calories == 545
    assert activity_log.steps == 10000


def test_activity_log_model_to_dict() -> None:
    """Test that the ActivityLog model can be serialized to a dictionary."""
    activity_log = ActivityLog(
        activity_id=12345,
        duration=3600000,
        name="Walking",
        start_date=date(2023, 1, 1),
        start_time="12:00:00",
    )
    data = activity_log.to_dict()
    assert data["activityId"] == 12345
    assert data["duration"] == 3600000
    assert data["name"] == "Walking"
    assert data["startDate"] == date(2023, 1, 1)
    assert data["startTime"] == "12:00:00"
