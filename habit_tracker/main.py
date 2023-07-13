from PyQt6.QtWidgets import QApplication
from constants import APP_NAME
from state import State


def main():
    State.init()
    app = QApplication([])
    app.setApplicationName(APP_NAME)
    app.exec()


if __name__ == "__main__":
    main()
