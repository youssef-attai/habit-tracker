from PyQt6.QtWidgets import QLabel
from core.base_widget import BaseWidget


class HabitWidget(BaseWidget):
    def __init__(self, habit):
        super().__init__()
        self.habit = habit

        self.label = QLabel(habit.name)
        self.layout().addWidget(self.label)
