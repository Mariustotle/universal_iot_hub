from typing import Any, Iterable, Optional

class Env:

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
