from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt
from core.base_widget import BaseWidget
from widgets.habit_list_widget import HabitListWidget
from state import State
import random


class HomeScreen(BaseWidget):
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
        random_name = random.choice(
            [
                "Go to the gym",
                "Eat healthy",
                "Drink water",
                "Read a book",
                "Meditate",
            ]
        )
        State.instance.habit_controller.create_habit(random_name)
