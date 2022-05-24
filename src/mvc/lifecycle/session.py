from typing import Iterable

from ...info import project_name, version
from ..controller import AbstractBaseController
from ..model import AbstractModel, AbstractModelEvent
from .file import FileController, FileModel

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow

import argparse

# ------------------------------------------------------------------------------
# MODEL
# ------------------------------------------------------------------------------

class FilesOpenedEvent(AbstractModelEvent):
    """
    Fired whenever files are opened in a session.
    """
    _name = 'files_opened'

    def __init__(self, *files: Iterable[FileModel]):
        self._files = files

    @property
    def files(self):
        """
        The files that were opened
        """
        return self._files

class SessionModel(AbstractModel):
    """
    Represents the current session, i.e. an instance of the program
    """
    def __init__(self):
        super().__init__()

        self._files = set()

    @property
    def files(self):
        return self._files

    def open_files(self, *files: Iterable[FileModel]) -> None:
        files_opened = frozenset(*files) - self._files
        if len(files_opened) > 0:
            self._files.add(*files_opened)
            self._emit(FilesOpenedEvent(files_opened))

# ------------------------------------------------------------------------------
# WIDGETS
# ------------------------------------------------------------------------------

class StartWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle(f"{project_name} {version}")

# ------------------------------------------------------------------------------
# CONTROLLER
# ------------------------------------------------------------------------------

class SessionController(AbstractBaseController):
    def __init__(self, argv):
        # -- Parse command line arguments --------------------------------------
        parser = argparse.ArgumentParser(
            description="Launch a (headless) instance of Salt")
        parser.add_argument("--file", "-f",
            type=str,
            required=False,
            help="A path to a Salt recipe file (*.json)")
        parser.add_argument("--gui", "-G",
            action="store_true",
            required=False,
            help="Display the GUI")

        self._args = parser.parse_args(argv[1:])

        # -- Initialise GUI ----------------------------------------------------

        if self._args.gui:
            QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
            self._app = QApplication(argv)

            self._window = StartWindow()
            self._window.show()

        # -- Set up model ------------------------------------------------------

        self._model = SessionModel()

        # map from arg names to function that inserts them into the model
        arg_map = {
            "file": self._open_files
        }

        # -- Set up event handlers for model -----------------------------------

        self._model.register_event_handler("files_opened",
            self._handle_files_opened)

        # -- Transfer parameters from command line args to model ---------------

        for arg in arg_map:
            arg_map[arg](self._args.__dict__[arg])


    def exec(self):
        if self.headless:
            return self.exec_headless()
        else:
            return self._app.exec_()

    def exec_headless(self):
        """
        Run the app in headless mode
        """
        # TODO
        print("exec_headless is not yet implemented...")
        return 0

    @property
    def headless(self):
        return not self._args.gui

    def _open_files(self, *files: Iterable[str]) -> None:
        self._model.open_files([FileController(f, self.headless).model for f in files])
            
    def _handle_files_opened(self, event: FilesOpenedEvent):
        print("files opened:", event.files)
