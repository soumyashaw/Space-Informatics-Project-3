import argparse
import collections
import datetime
import os

from typing import Any, NamedTuple, Sequence, Type

__all__ = [
    "namespace",
    "parse_arguments",
    "Location",
    "Pointing",
    "Load",
]


# Utility classes for naming fields of multi-value arguments
Location = NamedTuple("Location", [("lat", float), ("lon", float), ("alt", float)])
Location.__doc__ = "Location type providing latitude, longitude and altitude values"

Pointing = NamedTuple("Pointing", [("yaw", float), ("pitch", float), ("roll", float)])
Pointing.__doc__ = "Antenna pointing type providing yaw, pitch and roll values"

Load = NamedTuple("Load", [("charge_rate", float), ("discharge_rate", float)])
Load.__doc__ = "Battery load parameters for charging (`charge_rate`) and consuming (`discharge_rate`)"


# Action classes for parsing arguments into the utility classes defined above
class NamedTupleAction(argparse.Action):
    namedTupleClass: Type[collections.namedtuple]

    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: str | Sequence[Any] | None,
        option_string: str | None = None,
    ) -> None:
        assert len(values) == self.nargs
        setattr(namespace, self.dest, self.namedTupleClass(*values))


class LocationAction(NamedTupleAction):
    namedTupleClass = Location


class PointingAction(NamedTupleAction):
    namedTupleClass = Pointing


class LoadAction(NamedTupleAction):
    namedTupleClass = Load


# Command-line arguments
parser = argparse.ArgumentParser()

# General parameters
parser.add_argument(
    "--access",
    metavar="path/to/access/folder",
    type=os.path.abspath,
    default=os.path.abspath("lib/access"),
    help="folder where the access intervals should be stored or loaded from",
)
parser.add_argument(
    "--start",
    metavar="date",
    type=datetime.datetime.fromisoformat,
    default=datetime.datetime(2026, 5, 27, 14, 1),
    help="scenario start time",
)
parser.add_argument(
    "--stop",
    metavar="date",
    type=datetime.datetime.fromisoformat,
    default=datetime.datetime(2026, 6, 25, 2, 1),  # +28.5days
    help="scenario stop time",
)

# Subcommands for each task
subparsers = parser.add_subparsers(
    title="tasks",
    metavar="taskN",
    dest="task",
    required=True,
    help="project task to be executed",
)

# Task 1
task_1 = subparsers.add_parser(
    "task1", aliases=["t1"], help="task 1 - create scenario and determine best orbit"
)
task_1.set_defaults(access=os.path.abspath("out/access"))
task_1.add_argument("--gui", action="store_true", help="show STK GUI")
task_1.add_argument(
    "--scenario",
    metavar="path/to/scenario/folder",
    type=os.path.abspath,
    default=os.path.abspath("out/scenario"),
    help="location where the scenario should be stored",
)

# Colonies parameters
group_bases = task_1.add_argument_group("bases", "parameters for the moon colonies")
group_bases.add_argument(
    "--baseA",
    dest="base_A",
    nargs=3,
    metavar=("lat", "lon", "alt"),
    type=float,
    default=Location(0.0, 170.0, 0.0),
    help="geodetic position of the first moon base",
    action=LocationAction,
)
group_bases.add_argument(
    "--baseB",
    dest="base_B",
    nargs=3,
    metavar=("lat", "lon", "alt"),
    type=float,
    default=Location(0.0, -170.0, 0.0),
    help="geodetic position of the second moon base",
    action=LocationAction,
)

# Satellite parameters
group_satellite = task_1.add_argument_group(
    "satellite", "parameters for the moon satellite"
)
group_satellite.add_argument(
    "--sma", metavar="a", default=2037.0, type=float, help="semi-major axis [km]"
)
group_satellite.add_argument(
    "--ecc", metavar="e", default=0.0, type=float, help="eccentricity"
)
group_satellite.add_argument(
    "--aop", metavar="\u03c9", default=0.0, type=float, help="argument of perigee [deg]"
)
group_satellite.add_argument(
    "--raan",
    metavar="\u03a9",
    default=80.0,
    type=float,
    help="right ascension of the ascending node [deg]",
)
group_satellite.add_argument(
    "--ta", metavar="\u03bd", default=0.0, type=float, help="true anomaly [deg]"
)

# Satellite antenna
group_antenna = task_1.add_argument_group(
    "antenna", "parameters for the moon satellite's antenna"
)
group_antenna.add_argument(
    "--ang", metavar="\u03b1", default=120.0, help="cone angle [deg]", type=float
)
group_antenna.add_argument(
    "--rng", metavar="d", default=1000.0, help="maximum range [km]", type=float
)
group_antenna.add_argument(
    "--ypr",
    nargs=3,
    metavar=("y", "p", "r"),
    default=Pointing(0.0, 0.0, 0.0),
    help="antenna pointing (yaw, pitch, roll) [deg]",
    type=float,
    action=PointingAction,
)

# Common arguments for tasks 2 and 3
schedule_parser = argparse.ArgumentParser(add_help=False)
schedule_parser.add_argument(
    "--epsilon",
    metavar="\u03b5",
    type=float,
    default=0.5,
    help="ensure fairness up to \u03b5 kbit",
)

# Task 2
task_2 = subparsers.add_parser(
    "task2",
    aliases=["t2"],
    parents=[schedule_parser],
    help="task 2 - schedule fair access intervals",
)

# Task 3
task_3 = subparsers.add_parser(
    "task3",
    aliases=["t3"],
    parents=[schedule_parser],
    help="task 3 - keep an eye on the battery",
)

# Satellite battery
group_battery = task_3.add_argument_group(
    "battery", "parameters for the satellite's battery"
)
group_battery.add_argument(
    "--charge",
    metavar="c",
    type=float,
    default=50.0,
    help="threshold for battery charge [%%]",
)
group_battery.add_argument(
    "--initial",
    metavar="c",
    type=float,
    default=75.0,
    help="initial battery charge [%%]",
)
group_battery.add_argument(
    "--load",
    nargs=2,
    metavar=("in", "out"),
    type=float,
    default=Load(-0.0027, 0.0208),
    help="load for charging and draining the battery [%%/s]",
    action=LoadAction,
)


class TypedNamespace(argparse.Namespace):
    """Extended namespace with definitions of all arguments with type hints.

    Caution: This class defines all arguments as attributes,
    but only the task specific arguments will be available at runtime.
    """

    access: str
    start: datetime.datetime
    stop: datetime.datetime

    gui: bool
    scenario: str

    base_A: Location
    base_B: Location

    sma: float
    ecc: float
    aop: float
    raan: float
    ta: float

    ang: float
    rng: float
    ypr: Pointing

    epsilon: float

    charge: float
    initial: float
    load: Load


# Global namespace providing access to the command line arguments.
namespace = TypedNamespace()
namespace.__doc__ = "Global namespace providing access to the command line arguments."


def parse_arguments():
    """Parses the command line arguments and stores them in `namespace`."""
    parser.parse_args(namespace=namespace)
