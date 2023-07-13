from PyQt6.QtCore import Qt
from core.column_widget import ColumnWidget
from widgets.habit_widget import HabitWidget
from state import State


class HabitListWidget(ColumnWidget):
    def init(self):
        super().init()
        State.instance.habit_controller.add_observer(self)
        State.instance.habit_controller.load_habits()

    def build(self):
        super().build()
        self.layout().setAlignment(Qt.AlignmentFlag.AlignTop)

        for habit in State.instance.habit_controller.habits:
            self.layout().addWidget(HabitWidget(habit))
