from PyQt6.QtWidgets import QMainWindow


class Navigator:
    instance: "Navigator" = None

    def __init__(self, window):
        self.window: QMainWindow = window
        self.stack = []

    @staticmethod
    def init(window):
        if Navigator.instance is None:
            Navigator.instance = Navigator(window)

    @staticmethod
    def update():
        Navigator.instance.window.setCentralWidget(Navigator.instance.stack[-1])
        Navigator.instance.stack[-1].show()

    @staticmethod
    def pop():
        if len(Navigator.instance.stack) > 1:
            Navigator.instance.stack[-1].hide()
            Navigator.instance.stack.pop()
            Navigator.update()
        # else:
        #     Navigator.instance.window.close()

    @staticmethod
    def push(widget):
        Navigator.instance.stack.append(widget)
        Navigator.update()
