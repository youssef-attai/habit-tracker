from PyQt6.QtWidgets import QPushButton, QScrollArea
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

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.habit_list_widget = HabitListWidget()
        self.scroll_area.setWidget(self.habit_list_widget)

        self.layout().addWidget(self.scroll_area)

        self.new_habit_button = QPushButton("New habit")
        self.new_habit_button.clicked.connect(self._new_habit_button_clicked)
        self.layout().addWidget(self.new_habit_button)

    def _new_habit_button_clicked(self):
        Navigator.instance.push(CreateHabitScreen())
