from PyQt6.QtWidgets import QApplication
from core.base_window import BaseWindow
from screens.home_screen import HomeScreen
from state import State
from navigator import Navigator
from config import APP_NAME
from utils import Logger
import sys


class App(QApplication):
    def __init__(self, app_name, stylesheet):
        # This will make sure that uncaught exceptions do not crash the app
        # instead, they will be logged to the console
        sys.excepthook = Logger.e
        # TODO: pass the error to a global error handler that will display a popup
        # with the error message, for better UX

        super().__init__([])
        State.init()

        self.setApplicationName(APP_NAME)
        self.setStyleSheet(stylesheet)

        self.window = BaseWindow(app_name)

        Navigator.init(self.window)
        Navigator.push(HomeScreen())

        self.window.show()

        self.exec()
