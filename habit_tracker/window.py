from core.base_window import BaseWindow
from navigator import Navigator


class Window(BaseWindow):
    def __init__(self, home):
        super().__init__()

        Navigator.push(home)
