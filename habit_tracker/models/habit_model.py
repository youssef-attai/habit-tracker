class HabitModel:
    def __init__(self, id, title, description, goal, repeat):
        self.id = id
        self.title = title
        self.description = description
        self.goal = goal
        self.repeat = repeat

    @staticmethod
    def from_json(json: dict) -> "HabitModel":
        return HabitModel(
            id=json["id"],
            title=json["title"],
            description=json["description"],
            goal=json["goal"],
            repeat=json["repeat"],
        )
