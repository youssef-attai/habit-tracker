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
    def e(msg):
        if DEBUG:
            print("\033[91m", end="")
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}", end="")
            print("\033[0m")
