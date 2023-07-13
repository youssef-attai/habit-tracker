from PyQt6.QtWidgets import QLabel, QPushButton
from core.row_widget import RowWidget
from state import State
from navigator import Navigator
from screens.create_habit_screen import CreateHabitScreen


class HabitWidget(RowWidget):
    def __init__(self, habit):
        self.habit = habit
        super().__init__()

    def build(self):
        super().build()
        self.label = QLabel(self.habit.title)
        self.layout().addWidget(self.label)

        self.edit_button = QPushButton("Edit")
        self.edit_button.clicked.connect(self._edit_button_clicked)
        self.layout().addWidget(self.edit_button)

        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self._delete_button_clicked)
        self.layout().addWidget(self.delete_button)

    def _edit_button_clicked(self):
        Navigator.instance.push(CreateHabitScreen(self.habit))

    def _delete_button_clicked(self):
        State.instance.habit_controller.delete_habit(self.habit.id)
