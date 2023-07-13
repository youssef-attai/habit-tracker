from core.base_window import BaseWindow


class Navigator:
    instance: "Navigator" = None

    def __init__(self, window):
        self.window: BaseWindow = window

    @staticmethod
    def init(window):
        if Navigator.instance is None:
            Navigator.instance = Navigator(window)

    @staticmethod
    def pop():
        Navigator.instance.window.stacked_widget.removeWidget(
            Navigator.instance.window.stacked_widget.currentWidget()
        )

    @staticmethod
    def push(widget):
        Navigator.instance.window.stacked_widget.addWidget(widget)
        Navigator.instance.window.stacked_widget.setCurrentWidget(widget)
