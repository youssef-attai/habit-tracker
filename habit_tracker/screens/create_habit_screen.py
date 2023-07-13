from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QComboBox, QLineEdit, QPushButton, QTextEdit
from core.row_widget import RowWidget
from models.habit_model import HabitModel
from state import State
from navigator import Navigator


class CreateHabitScreen(ColumnWidget):
    def init(self):
        return super().init()

    def build(self):
        super().build()
        self.layout().setAlignment(Qt.AlignmentFlag.AlignTop)

        self.title = QLineEdit()
        self.title.setPlaceholderText("Title")
        self.layout().addWidget(self.title)

        self.description = QTextEdit()
        self.description.setPlaceholderText("Description")
        self.layout().addWidget(self.description)

        self.goal = QLineEdit()
        self.goal.setPlaceholderText("Goal")
        self.goal.setValidator(QIntValidator())
        self.layout().addWidget(self.goal)

        self.repeat = QComboBox()
        self.repeat.addItems(["Daily", "Weekly", "Monthly"])
        self.layout().addWidget(self.repeat)

        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.on_add_button_clicked)
        self.layout().addWidget(self.add_button)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.on_back_button_clicked)
        self.layout().addWidget(self.back_button)

    def on_add_button_clicked(self):
        State.instance.habit_controller.create_habit(
            HabitModel(
                self.title.text(),
                self.description.toPlainText(),
                int(self.goal.text()),
                self.repeat.currentText(),
            )
        )
        Navigator.instance.pop()

    def on_back_button_clicked(self):
        Navigator.instance.pop()
