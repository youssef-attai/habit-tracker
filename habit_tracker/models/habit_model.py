from utils import Logger


class HabitModel:
    def __init__(self, id, name):
        Logger.i(f"Constructing HabitModel(id={id}, name={name})")
        self.id = id
        self.name = name
