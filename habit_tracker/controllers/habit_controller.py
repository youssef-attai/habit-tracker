from core.change_notifier import ChangeNotifier
from utils import Logger


class HabitController(ChangeNotifier):
    def __init__(self, habit_repository):
        super().__init__()
        Logger.i("Constructing HabitController")
        self.habit_repository = habit_repository
        self.habits = []

    def load_habits(self):
        Logger.i("Loading habits")
        self.habits = self.habit_repository.find_all()
        self.notify()

    def create_habit(self, name):
        Logger.i("Creating habit")
        self.habit_repository.add(name)
        self.load_habits()
