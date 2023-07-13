from PyQt6.QtWidgets import QMainWindow

from constants import APP_NAME
from navigator import Navigator


class BaseWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(APP_NAME)

        Navigator.init(self)
