class State:
    instance: 'State' = None

    @staticmethod
    def init():
        if State.instance is None:
            State.instance = State()
