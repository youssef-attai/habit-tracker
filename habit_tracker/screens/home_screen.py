from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt
from core.column_widget import ColumnWidget
from navigator import Navigator
from screens.create_habit_screen import CreateHabitScreen
from widgets.habit_list_widget import HabitListWidget


class HomeScreen(ColumnWidget):
    def init(self):
        return super().init()

    def build(self):
        super().build()
        self.layout().setAlignment(Qt.AlignmentFlag.AlignTop)

        self.habit_list_widget = HabitListWidget()
        self.layout().addWidget(self.habit_list_widget)

        self.add_new_habit_button = QPushButton("Add new habit")
        self.add_new_habit_button.clicked.connect(self.on_add_new_habit_button_clicked)
        self.layout().addWidget(self.add_new_habit_button)

    def on_add_new_habit_button_clicked(self):
        Navigator.instance.push(CreateHabitScreen())
