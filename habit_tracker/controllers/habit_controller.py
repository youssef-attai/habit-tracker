from core.change_notifier import ChangeNotifier
from models.habit_model import HabitModel
from repositories.habit_repository import HabitRepository


class HabitController(ChangeNotifier):
    def __init__(self, habit_repository: HabitRepository):
        super().__init__()
        self.habit_repository: HabitRepository = habit_repository
        self.habits: list[HabitModel] = []

    def load_habits(self):
        self.habits = self.habit_repository.find_all()
        self.notify()

    def create_habit(self, habit: dict):
        self.habit_repository.add(habit)
        self.load_habits()

    def update_habit(self, habit_id: int, habit: dict):
        self.habit_repository.update(habit_id, habit)
        self.load_habits()

    def delete_habit(self, habit_id: int):
        self.habit_repository.delete(habit_id)
        self.load_habits()
