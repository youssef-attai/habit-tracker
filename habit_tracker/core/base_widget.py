from PyQt6.QtWidgets import QWidget, QStyleOption, QStyle
from PyQt6.QtGui import QPainter

# from utils import Logger


class BaseWidget(QWidget):
    def __init__(self, before_init=lambda: None, before_build=lambda: None):
        super().__init__()
        # self.setProperty("class", self.__class__.__name__.lower())
        before_init()
        self.init()
        before_build()
        self.build()

    def paintEvent(self, evt):
        super().paintEvent(evt)
        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(
            QStyle.PrimitiveElement.PE_Widget,
            opt,
            QPainter(self),
            self,
        )

    def init(self):
        # Logger.i(f"Initializing {self.__class__.__name__}")
        pass

    def build(self):
        # Logger.i(f"Building {self.__class__.__name__}")
        if self.layout() is not None:
            while self.layout().count():
                child = self.layout().takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
