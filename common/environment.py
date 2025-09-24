from typing import Any, Iterable, Optional
import sys
import threading
import time
import platform

class Env:

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
    def print(message:Optional[str] = None):
        if message is not None:
            print(message)
        else:
            print()
    
    @staticmethod
    def print_paragraph(*items: Any) -> None:
        for item in items:
            print(item)
