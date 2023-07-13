from schemas.habit_schema import HabitSchema


class HabitModel:
    def __init__(self, name, description, goal, repeat):
        self.name = name
        self.description = description
        self.goal = goal
        self.repeat = repeat

    @staticmethod
    def from_schema(schema: HabitSchema):
        return HabitModel(
            schema.name,
            schema.description,
            schema.goal,
            schema.repeat,
        )
