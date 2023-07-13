from utils import Logger


class HabitSchema:
    def __init__(self, id, name):
        Logger.i(f"Constructing HabitSchema(id={id}, name={name})")
        self.id = id
        self.name = name
