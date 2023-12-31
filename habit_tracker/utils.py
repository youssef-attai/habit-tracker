from env import DEBUG
from datetime import datetime


class Logger:
    @staticmethod
    def i(msg):
        if DEBUG:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

    @staticmethod
    def w(msg):
        if DEBUG:
            print("\033[93m", end="")
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}", end="")
            print("\033[0m")

    @staticmethod
    def e(type, value, traceback):
        file = traceback.tb_frame.f_code.co_filename
        line = traceback.tb_lineno
        msg = f"({type.__name__}) {value}\n"
        msg += f"at {file}:{line}"
        if DEBUG:
            print("\033[91m", end="")
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}", end="")
            print("\033[0m")


def class_name_to_css_class(class_name):
    # CamelCase -> camel-case
    return "".join(["-" + c.lower() if c.isupper() else c for c in class_name]).lstrip(
        "-"
    )
