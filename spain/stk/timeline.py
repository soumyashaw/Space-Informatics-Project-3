from agi.stk12.stkutil import AgEExecMultiCmdResultAction

from ..stk import STK


def show_access_intervals():
    """Create a timeline view for the Moon satellite and its access periods to the ground stations."""
    commands = [
        'Timeline * ContentView Add "MoonSat Access"',
        'Timeline * ContentView Select "MoonSat Access"',
        'Timeline * TimeView Add "Day 1"',
        'Timeline * TimeView Add "Week 1"',
        'Timeline * TimeView Add "12 hours"',
        'Timeline * TimeView Edit "Day 1" ViewPortInterval "UseAnalysisStartTime" "+1day"',
        'Timeline * TimeView Edit "Week 1" ViewPortInterval "UseAnalysisStartTime" "+1week"',
        'Timeline * TimeView Edit "12 hours" ViewPortInterval "UseAnalysisStartTime" "+12hours"',
        'Timeline * TimeView Select "Day 1"',
        'Timeline * TimeComponent Add ContentView "MoonSat Access" DisplayName "Colony A" "Access/Satellite-MoonSat-Sensor-MoonSatAntenna-To-Target-MoonBaseA AccessIntervals Interval List"',
        'Timeline * TimeComponent Add ContentView "MoonSat Access" DisplayName "Colony B" "Access/Satellite-MoonSat-Sensor-MoonSatAntenna-To-Target-MoonBaseB AccessIntervals Interval List"',
        'Timeline * TimeComponent Add ContentView "MoonSat Access" DisplayName "DSS 14" "Access/Satellite-MoonSat-To-Facility-DSS_14_Goldstone_STDN_DS14 AccessIntervals Interval List"',
        'Timeline * TimeComponent Add ContentView "MoonSat Access" DisplayName "DSS 43" "Access/Satellite-MoonSat-To-Facility-DSS_43_Tidbinbilla_STDN_DS43 AccessIntervals Interval List"',
        'Timeline * TimeComponent Add ContentView "MoonSat Access" DisplayName "DSS 63" "Access/Satellite-MoonSat-To-Facility-DSS_63_Robledo_STDN_DS63 AccessIntervals Interval List"',
        'Timeline * Refresh',
    ]

    STK.root.ExecuteMultipleCommands(
        commands, AgEExecMultiCmdResultAction.eContinueOnError
    )
