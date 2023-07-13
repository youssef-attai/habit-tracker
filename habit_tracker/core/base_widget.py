from PyQt6.QtWidgets import QVBoxLayout, QWidget, QStyleOption, QStyle
from PyQt6.QtGui import QPainter

from utils import Logger


class BaseWidget(QWidget):
    def __init__(self):
        super().__init__()
        Logger.i(f"Constructing {self.__class__.__name__}")
        self.setProperty("class", self.__class__.__name__.lower())
        self.setLayout(QVBoxLayout())
        self.init()
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
        Logger.i(f"Initializing {self.__class__.__name__}")

    def build(self):
        Logger.i(f"Building {self.__class__.__name__}")
        if self.layout() is not None:
            while self.layout().count():
                child = self.layout().takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
