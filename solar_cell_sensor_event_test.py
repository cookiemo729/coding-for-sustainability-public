from datetime import datetime
from solar_cell_sensor_event import SolarCellSensorEvent


def test_solar_cell_sensor_event_init():
    event = SolarCellSensorEvent("cell-1")
    assert event.cell_id == "cell-1"
    assert isinstance(event.timestamp, str)
    assert datetime.fromisoformat(event.timestamp)
    assert isinstance(event.temperature, int)
    assert 25 <= event.temperature <= 50
    assert event.temperature_unit == "C"


def test_solar_cell_sensor_event_str():
    event = SolarCellSensorEvent("cell-1")
    expected_str = f"cell_id: cell-1, timestamp: {event.timestamp}, voltage: {event.voltage} V, current: {event.current} A, temperature: {event.temperature} C"
    assert str(event) == expected_str


def test_solar_cell_sensor_event_lt():
    event1 = SolarCellSensorEvent("cell-1")
    event2 = SolarCellSensorEvent("cell-2")
    assert (event1 < event2) == (event1.timestamp < event2.timestamp)


def test_solar_cell_sensor_event_eq():
    event1 = SolarCellSensorEvent("cell-1")
    event2 = SolarCellSensorEvent("cell-1")
    event3 = SolarCellSensorEvent("cell-2")
    assert event1 == event2
    assert event1 != event3


def test_solar_cell_sensor_event_hash():
    event = SolarCellSensorEvent("cell-1")
    assert isinstance(hash(event), int)
