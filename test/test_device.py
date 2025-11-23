"""
Unit tests for the Device model.
"""

from collections.abc import Callable
from typing import Any, Dict, List

from fitbit_web_api.models.device import Device


def test_device_model_instantiation() -> None:
    """Test that the Device model can be instantiated with required fields."""
    device = Device(
        battery="High",
        battery_level=95,
        device_version="Charge 5",
        id="12345",
        mac="AA:BB:CC:DD:EE:FF",
        type="TRACKER",
    )
    assert device.battery == "High"
    assert device.battery_level == 95
    assert device.device_version == "Charge 5"
    assert device.id == "12345"
    assert device.mac == "AA:BB:CC:DD:EE:FF"
    assert device.type == "TRACKER"


def test_device_model_from_dict(load_test_data: Callable[[str], Any]) -> None:
    """Test that the Device model can be created from a dictionary."""
    data: List[Dict[str, Any]] = load_test_data("devices.json")
    # Test with the second device in the list which has different values
    device_data = data[1]
    device = Device.from_dict(device_data)
    assert device.battery == "High"
    assert device.battery_level == 95
    assert device.device_version == "Versa 3"
    assert device.id == "123456789"
    assert device.mac == "AA:BB:CC:DD:EE:FF"
    assert device.type == "TRACKER"


def test_device_model_to_dict():
    """Test that the Device model can be serialized to a dictionary."""
    device = Device(
        battery="Low",
        battery_level=10,
        device_version="Inspire 2",
        id="54321",
        mac="FF:EE:DD:CC:BB:AA",
        type="TRACKER",
    )
    data = device.to_dict()
    assert data["battery"] == "Low"
    assert data["batteryLevel"] == 10
    assert data["deviceVersion"] == "Inspire 2"
    assert data["id"] == "54321"
    assert data["mac"] == "FF:EE:DD:CC:BB:AA"
    assert data["type"] == "TRACKER"
