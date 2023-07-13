from PyQt6.QtWidgets import QApplication
from core.base_window import BaseWindow
from screens.home_screen import HomeScreen
from state import State
from navigator import Navigator
from config import APP_NAME


class App(QApplication):
    def __init__(self, app_name: str, stylesheet: str):
        super().__init__([])
        State.init()

        self.setApplicationName(APP_NAME)
        self.setStyleSheet(stylesheet)

        self.window = BaseWindow(app_name)

        Navigator.init(self.window)
        Navigator.push(HomeScreen())

        self.window.show()

        self.exec()
