"""
Unit tests for the SleepLog model.
"""

from collections.abc import Callable
from datetime import date
from typing import Any, Dict

from fitbit_web_api.models.sleep_log import SleepLog


def test_sleep_log_model_instantiation() -> None:
    """Test that the SleepLog model can be instantiated with required fields."""
    sleep_log = SleepLog(
        date_of_sleep=date(2023, 1, 1),
        duration=28800000,
        is_main_sleep=True,
        log_id=9876543210,
        start_time="2022-12-31T23:00:00.000",
        type="stages",
    )
    assert sleep_log.date_of_sleep == date(2023, 1, 1)
    assert sleep_log.duration == 28800000
    assert sleep_log.is_main_sleep is True
    assert sleep_log.log_id == 9876543210
    assert sleep_log.start_time == "2022-12-31T23:00:00.000"
    assert sleep_log.type == "stages"


def test_sleep_log_model_from_dict(load_test_data: Callable[[str], Any]) -> None:
    """Test that the SleepLog model can be created from a dictionary."""
    data: Dict[str, Any] = load_test_data("sleep_log_list.json")
    sleep_data = data["sleep"][0]
    sleep_log = SleepLog.from_dict(sleep_data)
    
    assert sleep_log is not None
    assert sleep_log.date_of_sleep == date(2023, 1, 1)
    assert sleep_log.efficiency == 95
    assert sleep_log.minutes_asleep == 480
    assert sleep_log.log_type == "auto_detected"


def test_sleep_log_model_to_dict() -> None:
    """Test that the SleepLog model can be serialized to a dictionary."""
    sleep_log = SleepLog(
        date_of_sleep=date(2023, 1, 1),
        duration=28800000,
        is_main_sleep=True,
        log_id=9876543210,
        start_time="2022-12-31T23:00:00.000",
        type="stages",
    )
    data = sleep_log.to_dict()
    assert data["dateOfSleep"] == date(2023, 1, 1)
    assert data["duration"] == 28800000
    assert data["isMainSleep"] is True
    assert data["logId"] == 9876543210
    assert data["startTime"] == "2022-12-31T23:00:00.000"
    assert data["type"] == "stages"
