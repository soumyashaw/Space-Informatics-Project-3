import gurobipy as gp
from gurobipy import GRB

from spain import namespace
from spain.types import IntervalList

__all__ = [
    "find_schedule_lp",
]


def find_schedule_lp(
    m: gp.Model, access_A: IntervalList, access_B: IntervalList, *args
) -> tuple[IntervalList, IntervalList, None]:
    """Find an optimal schedule for the Moon satellite to connect to both colonies fairly using linear programming."""

    intervals_A: IntervalList = []
    intervals_B: IntervalList = []

    # Compute schedule
    # TODO

    return (
        intervals_A,
        intervals_B,
        None,
    )  # None required to achieve same signature as task 3
