import random
from datetime import datetime
from utils import random_weighted


class SolarCellSensorEvent:
    """
    A class to represent a sensor event emitted by a solar cell.

    Example:
        event = SolarCellSensorEvent("cell-1")

    Attributes:
        cell_id (str): a unique identifier for the solar cell
        timestamp (str): the timestamp when the event was emitted
        voltage (float): the voltage value of the event
        voltage_unit (str): the unit of the voltage value
        current (int): the current value of the event
        current_unit (str): the unit of the current value
        temperature (int): the temperature value of the event
        temperature_unit (str): the unit of the temperature value
    """

    def __init__(self, cell_id):
        self.cell_id = cell_id
        self.timestamp = datetime.now().isoformat()
        self.voltage = random.uniform(0.5, 0.6)
        self.voltage_unit = "V"
        self.current = random_weighted(5, 10, 1)
        self.current_unit = "A"
        self.temperature = random_weighted(25, 50, 5)
        self.temperature_unit = "C"

    def __str__(self):
        """
        Return a string representation of the sensor event.
        """
        return "cell_id: {0}, timestamp: {1}, voltage: {2} {3}, current: {4} {5}, temperature: {6} {7}".format(
            self.cell_id,
            self.timestamp,
            self.voltage,
            self.voltage_unit,
            self.current,
            self.current_unit,
            self.temperature,
            self.temperature_unit,
        )

    def __lt__(self, other):
        """
        Compare two sensor events based on their timestamps.
        """
        return self.timestamp < other.timestamp

    def __eq__(self, other):
        """
        Check if two sensor events are equal based on their cell IDs.
        """
        return self.cell_id == other.cell_id

    def __hash__(self):
        """
        Return a hash value for the sensor event based on its key attributes.
        """
        return hash(
            (self.cell_id, self.timestamp, self.voltage, self.current, self.temperature)
        )
