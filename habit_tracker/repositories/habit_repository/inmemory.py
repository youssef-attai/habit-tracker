from models.habit_model import HabitModel
from repositories.habit_repository import HabitRepository
from schemas.habit_schema import HabitSchema


class InMemoryHabitRepository(HabitRepository):
    def __init__(self) -> None:
        super().__init__()
        self.__last_id: int = 0
        self.collection: list[HabitSchema] = []

    def __next_id(self) -> int:
        self.__last_id += 1
        return self.__last_id

    def add(self, habit: HabitModel) -> None:
        super().add(habit)
        self.collection.append(
            HabitSchema.from_model(self.__next_id(), habit)
        )

    def delete(self, habit_id) -> None:
        super().delete(habit_id)
        self.collection = [i for i in self.collection if i.id != habit_id]

    def update(self, habit) -> None:
        super().update(habit)
        for i in range(len(self.collection)):
            if self.collection[i].id == habit.id:
                self.collection[i] = habit
                break

    def find(self, habit_id) -> HabitModel | None:
        super().find(habit_id)
        for habit in self.collection:
            if habit.id == habit_id:
                return HabitModel.from_schema(habit)
        return None

    def find_all(self) -> list[HabitModel]:
        super().find_all()
        return [HabitModel.from_schema(habit) for habit in self.collection]
