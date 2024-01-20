import csv
import datetime
import os

from ..config import namespace
from ..types import IntervalList

__all__ = [
    "read_access_intervals",
    "write_access_intervals",
]


__intervals_files_names = ["baseA", "baseB", "sun"]
__intervals_files = map(
    lambda name: os.path.join(namespace.access, f"{name}.csv"), __intervals_files_names
)


def read_access_intervals() -> tuple[IntervalList, IntervalList, IntervalList]:
    """Reads the access intervals for the Moon satellite with the colonies and the sun from the disk."""

    def read_access_intervals_from_disk(file: str) -> IntervalList:
        with open(file, newline="") as access_intervals_file:
            return [
                tuple(map(datetime.datetime.fromisoformat, r))
                for r in csv.reader(access_intervals_file)
            ]

    return tuple(map(read_access_intervals_from_disk, __intervals_files))


def write_access_intervals(
    intervals_A: IntervalList, intervals_B: IntervalList, intervals_sun: IntervalList
):
    """Writes the access intervals for the Moon satellite with the colonies and the sun to the disk."""

    def write_access_intervals_to_disk(file: str, intervals: IntervalList):
        with open(file, "w", newline="") as access_intervals_file:
            csv.writer(access_intervals_file, lineterminator="\n").writerows(intervals)

    for f, intervals in zip(
        __intervals_files, [intervals_A, intervals_B, intervals_sun]
    ):
        write_access_intervals_to_disk(f, intervals)
