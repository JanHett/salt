from ..model import AbstractModel, AbstractModelEvent
from ..controller import AbstractController

from PySide2.QtWidgets import QMainWindow

# ------------------------------------------------------------------------------
# MODEL
# ------------------------------------------------------------------------------

class FileModel(AbstractModel):
    pass

# ------------------------------------------------------------------------------
# WIDGETS
# ------------------------------------------------------------------------------

class EditorWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Salt - TODO.filename")

# ------------------------------------------------------------------------------
# CONTROLLER
# ------------------------------------------------------------------------------

class FileController(AbstractController):
    def __init__(self, filename: str, headless: bool):
        super().__init__(headless)
        # TODO
        self._model = FileModel()

        if not self.headless:
            self._window = EditorWindow()
            self._window.show()
