"""
Unit tests for WeightLog model.
"""

from collections.abc import Callable
from typing import Any

from fitbit_web_api.models.weight_log import WeightLog


def test_weight_log_model_instantiation() -> None:
    """Test instantiation of WeightLog model."""
    weight_log = WeightLog(
        log_id=1234567890,
        weight=72.5,
        bmi=23.57,
    )
    assert weight_log.log_id == 1234567890
    assert weight_log.weight == 72.5
    assert weight_log.bmi == 23.57


def test_weight_log_model_from_dict(load_test_data: Callable[[str], Any]) -> None:
    """Test creating WeightLog from dictionary."""
    data = load_test_data("weight_log_list.json")
    weight_data = data["weight"][0]
    weight_log = WeightLog.from_dict(weight_data)

    assert weight_log is not None
    assert weight_log.log_id == 1234567890
    assert weight_log.weight == 72.5
    assert weight_log.bmi == 23.57
    assert weight_log.var_date is not None
    assert weight_log.source == "API"
    assert weight_log.time == "23:59:59"


def test_weight_log_model_to_dict(load_test_data: Callable[[str], Any]) -> None:
    """Test converting WeightLog to dictionary."""
    data = load_test_data("weight_log_list.json")
    weight_data = data["weight"][0]
    weight_log = WeightLog.from_dict(weight_data)

    assert weight_log is not None
    weight_dict = weight_log.to_dict()

    assert weight_dict["logId"] == 1234567890
    assert weight_dict["weight"] == 72.5
    assert weight_dict["bmi"] == 23.57
    assert weight_dict["source"] == "API"
