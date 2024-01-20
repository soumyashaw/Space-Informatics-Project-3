from agi.stk12.stkobjects import IAgSatellite, IAgSensor

from spain.config import namespace
from spain.stk import STK
from spain.types import IntervalList
from spain.util import inclinations

__all__ = [
    "initialise_scenario",
    "find_best_inclination",
    "compute_access_intervals",
]


def initialise_scenario():
    """Configures the scenario and initializes it with common properties."""

    # Create a new scenario
    STK.root.NewScenario("MoonColonisation")

    # Set analysis time period
    # TODO

    # Reset to analysis start time
    STK.root.Rewind()

    # Create moon colonies
    # TODO create colony A

    # TODO create colony B

    # Create DSN ground stations
    # TODO


def add_moon_satellite(inclination: int, name: str) -> tuple[IAgSatellite, IAgSensor]:
    """Creates a Moon satellite with the given inclination and name. Sets the initial state, adds a sensor and a range constraint."""

    # Create satellite object
    satellite = None  # TODO

    # Set initial state
    # TODO

    # Add sensor
    sensor = None  # TODO

    # Add range constraint
    # TODO

    return satellite, sensor


def find_best_inclination() -> int:
    """Find the best inclination for a Moon satellite w.r.t. the two colonies."""

    # Create four satellites
    satellites = [add_moon_satellite(inc, f"MoonSat{inc}") for inc in inclinations]

    # Find best inclination
    # TODO

    return -1


def compute_access_intervals() -> tuple[IntervalList, IntervalList, IntervalList]:
    """Extract the access intervals for the Moon satellite with both colonies and the sun."""

    # Get satellite and sensor from STK scenario
    satellite = None  # TODO
    sensor = None  # TODO

    # Compute and extract access intervals
    access_intervals_A: IntervalList = []
    access_intervals_B: IntervalList = []
    access_intervals_sun: IntervalList = []

    # TODO

    return access_intervals_A, access_intervals_B, access_intervals_sun
