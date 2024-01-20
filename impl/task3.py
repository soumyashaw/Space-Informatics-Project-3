import gurobipy as gp
from gurobipy import GRB

from spain import namespace
from spain.types import IntervalList

__all__ = [
    "find_schedule_with_battery_lp",
]


def find_schedule_with_battery_lp(
    m: gp.Model,
    access_A: IntervalList,
    access_B: IntervalList,
    access_sun: IntervalList,
) -> tuple[IntervalList, IntervalList, IntervalList]:
    """Find an optimal schedule for the Moon satellite to connect to both colonies fairly using linear programming while not depleting the battery."""

    intervals_A: IntervalList = []
    intervals_B: IntervalList = []

    intervals_sun: IntervalList = []

    # Compute battery-aware schedule
    # TODO

    return intervals_A, intervals_B, intervals_sun
