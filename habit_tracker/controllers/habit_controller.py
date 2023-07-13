from core.change_notifier import ChangeNotifier
from models.habit_model import HabitModel
from repositories.habit_repository.base import HabitRepository
from utils import Logger


class HabitController(ChangeNotifier):
    def __init__(self, habit_repository: HabitRepository):
        super().__init__()
        Logger.i("Constructing HabitController")
        self.habit_repository: HabitRepository = habit_repository
        self.habits: list[HabitModel] = []

    def load_habits(self):
        Logger.i("Loading habits")
        self.habits = self.habit_repository.find_all()
        self.notify()

    def create_habit(self, name):
        Logger.i("Creating habit")
        self.habit_repository.add(name)
        self.load_habits()
