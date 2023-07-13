from PyQt6.QtWidgets import QLabel
from core.base_widget import BaseWidget


class HabitWidget(BaseWidget):
    def __init__(self, habit):
        self.habit = habit
        super().__init__()

    def build(self):
        super().build()
        self.label = QLabel(self.habit.name)
        self.layout().addWidget(self.label)
