import pytest
from solar_cell import SolarCell
from solar_cell_sensor_event import SolarCellSensorEvent


@pytest.fixture
def solar_cell():
    return SolarCell("cell-1")


def test_init(solar_cell):
    assert isinstance(solar_cell, SolarCell)
    assert solar_cell.cell_id == "cell-1"
    assert isinstance(solar_cell.event, SolarCellSensorEvent)


def test_get_voltage(solar_cell):
    assert isinstance(solar_cell.get_voltage(), float)


def test_get_current(solar_cell):
    assert isinstance(solar_cell.get_current(), int)


def test_get_temperature(solar_cell):
    assert isinstance(solar_cell.get_temperature(), int)
