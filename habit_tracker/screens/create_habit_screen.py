from PyQt6.QtWidgets import (
    QComboBox,
    QLineEdit,
    QPushButton,
    QTextEdit,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator, QKeySequence, QShortcut
from core.column_widget import ColumnWidget
from core.row_widget import RowWidget
from models.habit_model import HabitModel
from state import State
from navigator import Navigator


class CreateHabitScreen(ColumnWidget):
    def __init__(self, existing_habit: HabitModel = None) -> None:
        self.existing_habit = existing_habit
        super().__init__()

    def init(self):
        super().init()
        # Create a QShortcut object with ESC as the key sequence
        shortcut = QShortcut(QKeySequence(Qt.Key.Key_Escape), self)
        # Connect the shortcut to a slot
        shortcut.activated.connect(self._cancel)

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

        if self.existing_habit is not None:
            self.title.setText(self.existing_habit.title)
            self.description.setText(self.existing_habit.description)
            self.goal.setText(str(self.existing_habit.goal))
            self.repeat.setCurrentText(self.existing_habit.repeat)

        if self.existing_habit is not None:
            self.main_action_button = QPushButton("Update")
            self.main_action_button.clicked.connect(self._update_habit)
        else:
            self.main_action_button = QPushButton("Add")
            self.main_action_button.clicked.connect(self._add_new_habit)

        self.buttons_row = RowWidget()

        self.buttons_row.layout().addWidget(self.main_action_button)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self._cancel)
        self.buttons_row.layout().addWidget(self.cancel_button)

        self.layout().addWidget(self.buttons_row)

    def _update_habit(self):
        title = self.title.text()
        description = self.description.toPlainText()
        goal = int(self.goal.text())
        repeat = self.repeat.currentText()

        State.instance.habit_controller.update_habit(
            self.existing_habit.id,
            {
                "title": title,
                "description": description,
                "goal": goal,
                "repeat": repeat,
            },
        )
        Navigator.instance.pop()

    def _add_new_habit(self):
        title = self.title.text()
        description = self.description.toPlainText()
        goal = int(self.goal.text())
        repeat = self.repeat.currentText()

        State.instance.habit_controller.create_habit(
            {
                "title": title,
                "description": description,
                "goal": goal,
                "repeat": repeat,
            }
        )
        Navigator.instance.pop()

    def _cancel(self):
        Navigator.instance.pop()
