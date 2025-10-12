from typing import Any, Iterable, Optional
import sys
import threading
import time
import platform

class Env:

    _ansi_colors = {
        "black": "30",
        "red": "31",
        "green": "32",
        "yellow": "33",
        "blue": "34",
        "magenta": "35",
        "cyan": "36",
        "white": "37",
        "bright_black": "90",
        "bright_red": "91",
        "bright_green": "92",
        "bright_yellow": "93",
        "bright_blue": "94",
        "bright_magenta": "95",
        "bright_cyan": "96",
        "bright_white": "97"
    }

    @staticmethod
    def monitor_until_keypress(callback, interval_seconds: int = 5):
        stop_event = threading.Event()
        system = platform.system()

        def key_listener():
            if system == "Windows":
                import msvcrt
                while not stop_event.is_set():
                    if msvcrt.kbhit():
                        msvcrt.getch()
                        stop_event.set()
            else:
                import tty
                import termios
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)
                try:
                    tty.setcbreak(fd)
                    while not stop_event.is_set():
                        if sys.stdin.read(1):
                            stop_event.set()
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        listener_thread = threading.Thread(target=key_listener, daemon=True)
        listener_thread.start()        

        counter = 0
        while not stop_event.is_set():
            counter += 1
            callback(counter)
            time.sleep(interval_seconds)

        stop_event.set()
        listener_thread.join(timeout=1)

    @staticmethod
    def clear_screan():
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def color_wrap(text: str, color: Optional[str] = None) -> str:
        if color is None:
            return text
        color_code = Env._ansi_colors.get(color.lower())
        if not color_code:
            return text  # Unknown color, return unmodified
        return f"\033[{color_code}m{text}\033[0m"
    
    @staticmethod
    def print(message: Optional[str] = None, color: Optional[str] = None):
        if message is not None:
            print(Env.color_wrap(message, color))
        else:
            print()

    @staticmethod
    def print_paragraph(*items: Any, color: Optional[str] = None) -> None:
        for item in items:
            Env.print(str(item), color=color)
