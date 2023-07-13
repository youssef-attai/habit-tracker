import abc

from models.habit_model import HabitModel


class HabitRepository(abc.ABC):
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def add(self, name) -> None:
        pass

    @abc.abstractmethod
    def update(self, habit) -> None:
        pass

    @abc.abstractmethod
    def delete(self, habit_id) -> None:
        pass

    @abc.abstractmethod
    def find(self, habit_id) -> HabitModel:
        pass

    @abc.abstractmethod
    def find_all(self) -> list[HabitModel]:
        pass
