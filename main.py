import signal
import sys
import time
from solar_array import SolarArray


def main():
    """
    Main function to read the aggregated sensor event data from the solar arrays and print to stdout.

    As a proxy for actual parallelism in the system (e.g. via threading), we instantiate new SolarArray objects
    on an interval and read the sensor data from them.

    We also do not introduce any complexity for managing state (e.g. observer pattern) so that students can focus on
    the core concepts of how Python programs work without getting bogged down in another abstraction layer.
    """
    solar_array_a = SolarArray("array-1")
    solar_array_b = SolarArray("array-2")
    solar_array_c = SolarArray("array-3")

    solar_arrays = [solar_array_a, solar_array_b, solar_array_c]

    for solar_array in solar_arrays:
        solar_array.log()


def signal_handler(sig, frame):
    """
    Handle SIGINT (CTRL+C) signal to exit the program gracefully.
    """
    signal_name = signal.Signals(sig).name
    print(f"\n{signal_name} received, exiting.")
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        main()
        time.sleep(0.5)
