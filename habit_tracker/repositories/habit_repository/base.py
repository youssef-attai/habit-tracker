import abc

from utils import Logger


class HabitRepository(abc.ABC):
    def __init__(self):
        Logger.i("Constructing HabitRepository")

    @abc.abstractmethod
    def add(self, name):
        Logger.i(f"Adding habit with name {name}")

    @abc.abstractmethod
    def update(self, habit):
        Logger.i(f"Updating habit: {habit}")

    @abc.abstractmethod
    def delete(self, habit_id):
        Logger.i(f"Deleting habit with id {habit_id}")

    @abc.abstractmethod
    def find(self, habit_id):
        Logger.i(f"Finding habit with id {habit_id}")

    @abc.abstractmethod
    def find_all(self):
        Logger.i("Finding all habits")
