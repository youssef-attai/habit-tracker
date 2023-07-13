from schemas.habit_schema import HabitSchema
from utils import Logger


class HabitModel:
    def __init__(self, name):
        Logger.i(f"Constructing HabitModel(name={name})")

        self.name = name

    @staticmethod
    def from_schema(schema: HabitSchema):
        Logger.i(f"Constructing HabitModel from schema {schema}")

        return HabitModel(
            schema.name,
        )
