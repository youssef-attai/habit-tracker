from PyQt6.QtWidgets import QMainWindow, QStackedWidget


class BaseWindow(QMainWindow):
    def __init__(self, window_title: str):
        super().__init__()
        self.setWindowTitle(window_title)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
