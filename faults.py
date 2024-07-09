from enum import Enum


class SolarCellFault(Enum):
    HOT_SPOT = "HOT_SPOT"
    """
    A fault condition where the temperature of the solar cell exceeds a certain threshold.
    """


class SolarPanelFault(Enum):
    OPEN_CIRCUIT = "OPEN_CIRCUIT"
    """
    A fault condition where the circuit is open, resulting in no current flow.
    """

    SHORT_CIRCUIT = "SHORT_CIRCUIT"
    """
    A fault condition where the circuit is shorted, resulting in excessive current flow.
    """


class SolarArrayFault(Enum):
    UNDERVOLTAGE = "UNDERVOLTAGE"
    """
    A fault condition where the voltage of the solar array is below a certain threshold.
    """

    OVERVOLTAGE = "OVERVOLTAGE"
    """
    A fault condition where the voltage of the solar array exceeds a certain threshold.
    """

    UNDERCURRENT = "UNDERCURRENT"
    """
    A fault condition where the current of the solar array is below a certain threshold.
    """

    OVERCURRENT = "OVERCURRENT"
    """
    A fault condition where the current of the solar array exceeds a certain threshold.
    """
