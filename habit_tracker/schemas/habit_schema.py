from datetime import datetime


class HabitSchema:
    def __init__(self, id, name, description, goal, repeat):
        self.id = id
        self.name = name
        self.description = description
        self.goal = goal
        self.repeat = repeat

        self.progress = 0
        self.streak = 0
        self.created_at = datetime.now()
        self.updated_at = None

    @staticmethod
    def from_model(id, model):
        return HabitSchema(
            id=id,
            name=model.name,
            description=model.description,
            goal=model.goal,
            repeat=model.repeat,
        )
