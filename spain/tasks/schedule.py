import contextlib
import csv
import datetime
from collections.abc import Iterator
from dataclasses import dataclass

import gurobipy as gp
from gurobipy import GRB

from impl.task2 import find_schedule_lp
from impl.task3 import find_schedule_with_battery_lp

from ..config import namespace
from ..internal.access import read_access_intervals
from ..types import IntervalList
from ..util import collected_data

__all__ = [
    "schedule",
]


@dataclass(repr=False, eq=False, frozen=True)
class Scheduler(contextlib.AbstractContextManager):
    """Abstract scheduler class.

    Provides access intervals as class variables and requires a single method to be overwritten: `schedule`.

    Implements a context manager for individual setup and teardown.
    """

    access_intervals_A: IntervalList
    access_intervals_B: IntervalList
    access_intervals_sun: IntervalList

    def __enter__(self):
        return self

    def schedule(self) -> tuple[IntervalList, IntervalList, IntervalList | None]:
        """Find an optimal schedule for the Moon satellite.

        RAISES:
            NotImplementedError
        """
        raise NotImplementedError()

    def __exit__(self, __exc_type, __exc_value, __traceback) -> bool | None:
        return super().__exit__(__exc_type, __exc_value, __traceback)

    def _access_intervals(self) -> Iterator[IntervalList]:
        yield self.access_intervals_A
        yield self.access_intervals_B
        yield self.access_intervals_sun


class LPScheduler(Scheduler):
    """Scheduler using linear programming.

    Uses Gurobi internally. Configuration of Gurobi and teardown using context manager.
    """

    m: gp.Model

    def __enter__(self):
        gurobi_log_file = "out/gurobi.log"
        with open(gurobi_log_file, "w"):
            pass  # Clear the log file!

        self.m = gp.Model("MoonSat Scheduler")
        self.m.setParam(GRB.Param.LogFile, gurobi_log_file)
        # avoid solutions that exploit integrality tolerances
        self.m.setParam(GRB.Param.IntegralityFocus, 1)

        return super().__enter__()

    def __exit__(self, __exc_type, __exc_value, __traceback):
        if self.m is not None:
            self.m.write("out/schedule/schedule.lp")
            if self.m.Status != GRB.LOADED:
                self.m.write("out/schedule/schedule.sol")

            self.m = None

        return super().__exit__(__exc_type, __exc_value, __traceback)


class LPSchedulerT2(LPScheduler):
    def schedule(self) -> tuple[IntervalList, IntervalList, None]:
        return find_schedule_lp(self.m, *self._access_intervals())


class LPSchedulerT3(LPScheduler):
    def schedule(self) -> tuple[IntervalList, IntervalList, IntervalList]:
        return find_schedule_with_battery_lp(self.m, *self._access_intervals())


def _select_lp_scheduler(with_battery: bool, *args) -> Scheduler:
    return LPSchedulerT3(*args) if with_battery else LPSchedulerT2(*args)


def schedule(with_battery: bool):
    with _select_lp_scheduler(with_battery, *read_access_intervals()) as scheduler:
        intervals_A, intervals_B, intervals_sun = scheduler.schedule()

    duration_A = sum((e - s for s, e in intervals_A), datetime.timedelta())
    duration_B = sum((e - s for s, e in intervals_B), datetime.timedelta())

    data_A = sum(collected_data(s, e) for s, e in intervals_A)
    data_B = sum(collected_data(s, e) for s, e in intervals_B)

    print(
        f"Connection to base A is scheduled for {duration_A.total_seconds():>10.3f} seconds, "
        f"collecting {data_A:>12.3f} kb of data."
    )
    print(
        f"Connection to base B is scheduled for {duration_B.total_seconds():>10.3f} seconds, "
        f"collecting {data_B:>12.3f} kb of data."
    )
    print(
        "Difference in collected data: {data} {cmp} ε = {eps} {warn}".format(
            data=abs(data_A - data_B),
            cmp="≤" if abs(data_A - data_B) <= namespace.epsilon else ">",
            eps=namespace.epsilon,
            warn="✅" if abs(data_A - data_B) <= namespace.epsilon else "⚠️",
        )
    )

    # Export computed schedule
    with open(
        f"out/schedule/intervals{3 if with_battery else 2}.csv", "w", newline=""
    ) as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerows(
            ((*tuple(map(lambda d: d.isoformat(), iv)), "A") for iv in intervals_A)
        )
        writer.writerows(
            ((*tuple(map(lambda d: d.isoformat(), iv)), "B") for iv in intervals_B)
        )
        if with_battery:
            writer.writerows(
                (
                    (*tuple(map(lambda d: d.isoformat(), iv)), "S")
                    for iv in intervals_sun
                )
            )
