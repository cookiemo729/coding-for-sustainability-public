from unittest.mock import patch
from solar_array import SolarArray
from solar_panel import SolarPanel


def test_init():
    array = SolarArray("array-1", 5)
    assert array.array_id == "array-1"
    assert len(array.panels) == 5
    for i, panel in enumerate(array.panels):
        assert isinstance(panel, SolarPanel)
        assert panel.panel_id == f"array-1-panel-{i}"


def test_get_voltage():
    with patch.object(SolarPanel, "get_voltage", return_value=5):
        array = SolarArray("array-1", 5)
        assert array.get_voltage() == 25


def test_get_current():
    with patch.object(SolarPanel, "get_current", return_value=5):
        array = SolarArray("array-1", 5)
        assert array.get_current() == 5


def test_get_temperature():
    with patch.object(SolarPanel, "get_temperature", return_value=20):
        array = SolarArray("array-1", 5)
        assert array.get_temperature() == 20


def test_log():
    with patch("builtins.print") as mock_print, patch.object(
        SolarArray, "get_voltage", return_value=25
    ), patch.object(SolarArray, "get_current", return_value=5), patch.object(
        SolarArray, "get_temperature", return_value=20
    ):
        array = SolarArray("array-1", 5)
        array.log()
        mock_print.assert_called_once_with(
            "Array ID: array-1, Voltage: 25.00 V, Current: 5.00 A, Temperature: 20.00 C"
        )
