import contextlib
import os
import sys

from agi.stk12.stkdesktop import STKDesktop, STKDesktopApplication
from agi.stk12.stkobjects import AgStkObjectRoot
from agi.stk12.stkutil import STKInitializationError

from ..config import namespace

__all__ = [
    "STK",
]


class StkWrapper(contextlib.AbstractContextManager):
    """Wrapper around the STK API. Takes care of properly connecting to STK.

    Usage:
        STK = StkWrapper()
        with STK:
            # Do your work.
    """

    __ui_application: STKDesktopApplication | None
    __root: AgStkObjectRoot | None

    def __init__(self):
        self.__ui_application = None
        self.__root = None

    def __enter__(self):
        try:
            self.__ui_application = STKDesktop.AttachToApplication()
        except STKInitializationError:
            # There was no running STK instance, hence we start a new one.
            try:
                self.__ui_application = STKDesktop.StartApplication(
                    visible=namespace.gui, userControl=namespace.gui
                )
            except STKInitializationError:
                # Most likely a license issue, e.g. no VPN connection.
                sys.exit(
                    f"Could neither connect to a running STK instance nor start a new one.{os.linesep}"
                    + "Most likely, this is a license issue. Are you properly connected to the university network?"
                )

        self.__ui_application.Visible = namespace.gui
        self.__ui_application.UserControl = namespace.gui

        self.__root = self.__ui_application.Root

        if self.__root.CurrentScenario:
            self.__root.CloseScenario()

        return super().__enter__()

    def __exit__(self, exc_type, exc_value, traceback):
        if not namespace.gui and self.__ui_application is not None:
            self.__ui_application.ShutDown()

        self.__ui_application = None
        self.__root = None

        return super().__exit__(exc_type, exc_value, traceback)

    @property
    def root(self) -> AgStkObjectRoot:
        """The root of the STK object model as an `AgStkObjectRoot`."""
        return self.__root

    def export_sc(self, path: str):
        """Saves the currently loaded scenario in the location specified by `path`."""
        assert self.root.CurrentScenario
        assert os.path.splitext(path)[1] == ".sc"
        self.__root.SaveScenarioAs(path)

    def export_vdf(self, path: str):
        """Saves the currently loaded scenario in the location specified by `path`."""
        assert self.root.CurrentScenario
        self.__root.SaveVDFAs(path, "", "SpaIn21 Project 3 - MoonColonisation", "")

    def export(self, path: str):
        """Saves the currently loaded scenario in the location specified by `path`.

        Takes care of creating directories and selects the appropriate export method.
        """
        # Check extension -> Is path a file or a directory?
        ext = os.path.splitext(path)[1]
        if ext != "":
            assert ext in (".sc", ".vdf")
            dir = os.path.split(path)[0]
        else:
            dir = path

        # Create directory if necessary, STK won't do that for us.
        os.makedirs(dir, exist_ok=True)

        # Delegate to appropriate export method.
        if ext == 'vdf':
            self.export_vdf(path)
        else:
            if ext == '':
                path = os.path.join(path, f"{self.root.CurrentScenario.InstanceName}{os.extsep}sc")

            self.export_sc(path)

    def import_sc(self, path: str):
        """Loads the scenario located at `path`. Throws an exception if a scenario is already loaded."""
        self.__root.LoadScenario(path)

    def import_vdf(self, path: str):
        """Loads the scenario located at `path`. Throws an exception if a scenario is already loaded."""
        self.__root.LoadVDF(path, "")


STK = StkWrapper()
