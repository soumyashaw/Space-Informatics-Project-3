from agi.stk12.stkobjects import IAgSatellite, IAgSensor, AgEVePropagatorType, AgESTKObjectType, AgEAccessConstraints
from agi.stk12.stkobjects import AgEOrbitStateType, AgEClassicalLocation, AgEClassicalSizeShape, AgEYPRAnglesSequence

from spain.config import namespace
from spain.stk import STK
from spain.types import IntervalList
from spain.util import inclinations, parse_stk_date, unparse_date_stk

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
    startTime = unparse_date_stk(namespace.start)
    endTime = unparse_date_stk(namespace.stop)

    STK.root.UnitPreferences.SetCurrentUnit("DateFormat", "UTCG")
    STK.root.CurrentScenario.SetTimePeriod(startTime, endTime)


    # Reset to analysis start time
    STK.root.Rewind()

    # Create moon colonies
    # Colony A
    targetNameA = "MoonBaseA"
    moonLatitudeA = namespace.base_A.lat
    moonLongitudeA = namespace.base_A.lon
    moonAltitudeA = namespace.base_A.alt

    targetA = STK.root.CurrentScenario.Children.NewOnCentralBody(AgESTKObjectType.eTarget, targetNameA, 'Moon')
    targetA.Position.AssignGeodetic(moonLatitudeA, moonLongitudeA, moonAltitudeA)

    # Colony B
    targetNameB = "MoonBaseB"
    moonLatitudeB = namespace.base_B.lat
    moonLongitudeB = namespace.base_B.lon
    moonAltitudeB = namespace.base_B.alt

    targetB = STK.root.CurrentScenario.Children.NewOnCentralBody(AgESTKObjectType.eTarget, targetNameB, 'Moon')
    targetB.Position.AssignGeodetic(moonLatitudeB, moonLongitudeB, moonAltitudeB)

    # Create DSN ground stations
    facilityName1 = "DSS_14_Goldstone_STDN_DS14"
    latitude1 = 35.425901
    longitude1 = -116.889538
    altitude1 = 1001.39
    facility1 = STK.root.CurrentScenario.Children.New(AgESTKObjectType.eFacility, facilityName1)
    facility1.Position.AssignGeodetic(latitude1, longitude1, altitude1)

    facilityName2 = "DSS_43_Tidbinbilla_STDN_DS43"
    latitude2 = -35.402424
    longitude2 = 148.981267
    altitude2 = 688.867
    facility2 = STK.root.CurrentScenario.Children.New(AgESTKObjectType.eFacility, facilityName2)
    facility2.Position.AssignGeodetic(latitude2, longitude2, altitude2)

    facilityName3 = "DSS_63_Robledo_STDN_DS63"
    latitude3 = 40.43121
    longitude3 = -4.248009
    altitude3 = 864.816
    facility3 = STK.root.CurrentScenario.Children.New(AgESTKObjectType.eFacility, facilityName3)
    facility3.Position.AssignGeodetic(latitude3, longitude3, altitude3)


def add_moon_satellite(inclination: int, name: str) -> tuple[IAgSatellite, IAgSensor]:
    """Creates a Moon satellite with the given inclination and name. Sets the initial state, adds a sensor and a range constraint."""

    # Create satellite object
    satellite = STK.root.CurrentScenario.Children.NewOnCentralBody(AgESTKObjectType.eSatellite, name, 'Moon')
    satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorTwoBody)

    # Set initial state
    keplerian = satellite.Propagator.InitialState.Representation.ConvertTo(AgEOrbitStateType.eOrbitStateClassical)
    keplerian.SizeShapeType = AgEClassicalSizeShape.eSizeShapeSemimajorAxis
    keplerian.LocationType = AgEClassicalLocation.eLocationTrueAnomaly
    keplerian.Orientation.AscNodeType = 1

    keplerian.SizeShape.SemiMajorAxis = namespace.sma  # km
    keplerian.SizeShape.Eccentricity = namespace.ecc
    keplerian.Orientation.ArgOfPerigee = namespace.aop  # deg
    keplerian.Orientation.AscNode.Value = namespace.raan  # deg
    keplerian.Orientation.Inclination = inclination  # deg
    keplerian.Location.Value = namespace.ta  # deg

    # Apply the changes made to the satellite's state and propagate:
    satellite.Propagator.InitialState.Representation.Assign(keplerian)
    satellite.Propagator.Propagate()


    # Add sensor
    sensor = satellite.Children.New(AgESTKObjectType.eSensor, "MoonSatAntenna")

    # Add range constraint
    rangeConstraint = sensor.AccessConstraints.AddConstraint(AgEAccessConstraints.eCstrRange)
    rangeConstraint.EnableMax = True
    rangeConstraint.Max = 1000

    sensor.Pattern.ConeAngle = namespace.ang / 2  # deg

    (yaw, pitch, roll) = namespace.ypr
    sensor.CommonTasks.SetPointingFixedYPR(AgEYPRAnglesSequence.eRPY, yaw, pitch, roll)

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
