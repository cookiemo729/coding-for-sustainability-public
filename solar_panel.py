from solar_cell import SolarCell
from utils import average


class SolarPanel:
    """
    A class to represent a solar panel composed of multiple solar cells.

    Example:
        solar_panel = SolarPanel("panel-1")

    Attributes:
        panel_id (str): a unique identifier for the solar panel
        cells (list): a list of SolarCell objects
    """

    def __init__(self, panel_id, cell_count=60):
        self.panel_id = panel_id
        self.cells = []

        for i in range(cell_count):
            cell = SolarCell(f"{self.panel_id}-cell-{i}")
            cell.check_faults()
            self.cells.append(cell)

    def get_voltage(self):
        """
        Get the aggregated voltage value of the solar panel.
        """
        cell_voltages = [cell.get_voltage() for cell in self.cells]
        return sum(cell_voltages)

    def get_current(self):
        """
        Get the aggregated current value of the solar panel.
        """
        cell_currents = [cell.get_current() for cell in self.cells]
        return average(cell_currents)

    def get_temperature(self):
        """
        Get the aggregated temperature value of the solar panel.
        """
        cell_temperatures = [cell.get_temperature() for cell in self.cells]
        return average(cell_temperatures)
