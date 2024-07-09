import pytest
from unittest.mock import MagicMock
from solar_panel import SolarPanel
from solar_cell import SolarCell


@pytest.fixture
def solar_panel():
    return SolarPanel("panel-1", 5)


def test_init(solar_panel):
    assert solar_panel.panel_id == "panel-1"
    assert len(solar_panel.cells) == 5
    assert all(isinstance(cell, SolarCell) for cell in solar_panel.cells)


def test_get_voltage(solar_panel):
    SolarCell.get_voltage = MagicMock(return_value=5)
    assert solar_panel.get_voltage() == 25


def test_get_current(solar_panel):
    SolarCell.get_current = MagicMock(return_value=7.5)
    assert solar_panel.get_current() == 7.5


def test_get_temperature(solar_panel):
    SolarCell.get_temperature = MagicMock(return_value=20)
    assert solar_panel.get_temperature() == 20
