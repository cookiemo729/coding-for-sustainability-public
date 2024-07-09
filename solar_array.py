from solar_panel import SolarPanel
from utils import average


class SolarArray:
    """
    A class to represent a solar array composed of multiple solar panels.

    Example:
        solar_array = SolarArray("array-1")

    Attributes:
        array_id (str): a unique identifier for the solar array
        panels (list): a list of SolarPanel objects
    """

    def __init__(self, array_id, panel_count=10):
        self.array_id = array_id
        self.panels = [
            SolarPanel(f"{self.array_id}-panel-{i}") for i in range(panel_count)
        ]

    def get_voltage(self):
        """
        Get the aggregated voltage value of the solar array.
        """
        panel_voltages = [panel.get_voltage() for panel in self.panels]
        return sum(panel_voltages)

    def get_current(self):
        """
        Get the aggregated current value of the solar array.
        """
        panel_currents = [panel.get_current() for panel in self.panels]
        return average(panel_currents)

    def get_temperature(self):
        """
        Get the aggregated temperature value of the solar array.
        """
        panel_temperatures = [panel.get_temperature() for panel in self.panels]
        return average(panel_temperatures)

    def log(self):
        """
        Log the aggregated sensor data of the solar array.
        """
        voltage = self.get_voltage()
        current = self.get_current()
        temperature = self.get_temperature()

        print(
            f"Array ID: {self.array_id}, Voltage: {voltage:.2f} V, Current: {current:.2f} A, Temperature: {temperature:.2f} C"
        )
