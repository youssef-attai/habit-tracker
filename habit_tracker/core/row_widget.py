from PyQt6.QtWidgets import QHBoxLayout
from core.base_widget import BaseWidget


class RowWidget(BaseWidget):
    def __init__(self):
        super().__init__(before_init=self.before_init)

    def before_init(self):
        self.setLayout(QHBoxLayout())
