from solar_cell_sensor_event import SolarCellSensorEvent
from faults import SolarCellFault


class SolarCell:
    """
    A class to represent a solar cell that emits a sensor event.

    Example:
        solar_cell = SolarCell("cell-1")

    Attributes:
        cell_id (str): a unique identifier for the solar cell
        event (SolarCellSensorEvent): a sensor event emitted by the solar cell
    """

    def __init__(self, cell_id):
        self.cell_id = cell_id
        self.event = SolarCellSensorEvent(self.cell_id)

    def get_voltage(self):
        """
        Get the voltage value of the solar cell sensor event.
        """
        return self.event.voltage

    def get_current(self):
        """
        Get the current value of the solar cell sensor event.
        """
        return self.event.current

    def get_temperature(self):
        """
        Get the temperature value of the solar cell sensor event.
        """
        return self.event.temperature

    def check_faults(self):
        """
        Check for faults in the solar cell based on the sensor event data.
        """
        if self.event.temperature > 45:
            print(
                f"Fault detected: {SolarCellFault.HOT_SPOT.value}, Cell ID: {self.cell_id}"
            )
