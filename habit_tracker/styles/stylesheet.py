from utils import Logger


def styleSheet():
    Logger.i("Loading stylesheet")
    return """
.window {
    background-color: #ff0000;
}

.habitwidget {
    background-color: #00ff00;
}

"""
