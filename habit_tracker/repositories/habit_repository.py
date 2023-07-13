from models.habit_model import HabitModel


class HabitRepository:
    def __init__(self) -> None:
        self.__last_id: int = 0
        self.collection: list[dict] = []

    def __next_id(self) -> int:
        self.__last_id += 1
        return self.__last_id

    def add(self, habit: dict) -> None:
        self.collection.append(
            {
                "id": self.__next_id(),
                "title": habit["title"],
                "description": habit["description"],
                "goal": habit["goal"],
                "repeat": habit["repeat"],
            }
        )

    def delete(self, habit_id: int) -> None:
        self.collection = [i for i in self.collection if i["id"] != habit_id]

    def update(self, habit_id: int, habit: dict) -> None:
        for i in range(len(self.collection)):
            if self.collection[i]["id"] == habit_id:
                self.collection[i].update(habit)
                break

    def find(self, habit_id: int) -> HabitModel | None:
        for habit in self.collection:
            if habit["id"] == habit_id:
                return HabitModel.from_json(habit)
        return None

    def find_all(self) -> list[HabitModel]:
        return [HabitModel.from_json(habit) for habit in self.collection]
