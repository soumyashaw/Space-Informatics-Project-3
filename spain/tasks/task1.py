from ..config import namespace
from ..internal.access import write_access_intervals
from ..util import inclinations

__all__ = [
    "task1",
]


def task1():
    # 0. Import STK
    from agi.stk12.stkobjects import AgESTKObjectType

    from impl.task1 import (
        compute_access_intervals,
        find_best_inclination,
        initialise_scenario,
    )

    from ..stk import STK, timeline

    with STK:
        # 1. Initialise scenario
        initialise_scenario()

        # 2. Create four satellites and determine the best inclination
        inclination = find_best_inclination()

        assert inclination in inclinations

        print(f"Chosen inclination: {inclination:>2d}°")

        # 3. Rename chosen satellite
        STK.root.CurrentScenario.Children.Item(
            f"MoonSat{inclination}"
        ).InstanceName = "MoonSat"

        # 4. Remove useless satellites
        for inc in inclinations:
            if inc == inclination:
                # Obviously, we do not want to remove the chosen satellite.
                continue

            assert STK.root.CurrentScenario.Children.Contains(
                AgESTKObjectType.eSatellite, f"MoonSat{inc}"
            )
            STK.root.CurrentScenario.Children.Unload(
                AgESTKObjectType.eSatellite, f"MoonSat{inc}"
            )

        # 5. Export scenario
        STK.export(namespace.scenario)

        # 6. Compute access intervals
        intervals_A, intervals_B, intervals_sun = compute_access_intervals()

        # 7. Export access intervals
        write_access_intervals(intervals_A, intervals_B, intervals_sun)

        # 8. Show access intervals if GUI is activated
        if namespace.gui:
            timeline.show_access_intervals()
