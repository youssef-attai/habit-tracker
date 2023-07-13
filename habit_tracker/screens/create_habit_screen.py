from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLineEdit, QPushButton
from core.base_widget import BaseWidget
from state import State
from navigator import Navigator


class CreateHabitScreen(BaseWidget):
    def init(self):
        return super().init()

    def build(self):
        super().build()
        self.layout().setAlignment(Qt.AlignmentFlag.AlignTop)

        self.title = QLineEdit()
        self.title.setPlaceholderText("Title")
        self.layout().addWidget(self.title)

        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.on_add_button_clicked)
        self.layout().addWidget(self.add_button)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.on_back_button_clicked)
        self.layout().addWidget(self.back_button)

    def on_add_button_clicked(self):
        State.instance.habit_controller.create_habit(self.title.text())
        Navigator.instance.pop()

    def on_back_button_clicked(self):
        Navigator.instance.pop()
