from controllers.habit_controller import HabitController
from repositories.habit_repository import InMemoryHabitRepository


class State:
    instance: 'State' = None

    def __init__(self):
        self.habit_repository = InMemoryHabitRepository()
        self.habit_controller = HabitController(self.habit_repository)

    @staticmethod
    def init():
        if State.instance is None:
            State.instance = State()
