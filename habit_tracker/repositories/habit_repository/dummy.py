from utils import Logger
from repositories.habit_repository import HabitRepository
from models.habit_model import HabitModel


class DummyHabitRepository(HabitRepository):
    def __init__(self):
        super().__init__()
        self.__last_id = 0
        self.collection = [
            HabitModel(1, "Read"),
            HabitModel(2, "Exercise"),
            HabitModel(3, "Meditate"),
        ]

    def __next_id(self):
        Logger.i("Generating next id")
        self.__last_id += 1
        return self.__last_id

    def add(self, name):
        super().add(name)
        self.collection.append(HabitModel(self.__next_id(), name))

    def delete(self, habit_id):
        super().delete(habit_id)
        self.collection = [i for i in self.collection if i.id != habit_id]

    def update(self, habit):
        super().update(habit)
        for i in range(len(self.collection)):
            if self.collection[i].id == habit.id:
                self.collection[i] = habit
                break

    def find(self, habit_id):
        super().find(habit_id)
        for habit in self.collection:
            if habit.id == habit_id:
                return habit
        return None

    def find_all(self):
        super().find_all()
        return self.collection
