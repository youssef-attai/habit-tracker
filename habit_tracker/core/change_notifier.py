from utils import Logger


class ChangeNotifier:
    def __init__(self):
        Logger.i("Constructing ChangeNotifier")
        self.__widgets = set()

    def add_observer(self, observer):
        Logger.i(f"Adding observer {observer}")
        self.__widgets.add(observer)

    def remove_observer(self, observer):
        Logger.i(f"Removing observer {observer}")
        self.__widgets.remove(observer)

    def notify(self):
        Logger.i("Notifying observers")
        for widget in self.__widgets:
            widget.build()
