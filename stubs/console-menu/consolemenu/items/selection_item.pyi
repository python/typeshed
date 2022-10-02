from _typeshed import Incomplete

from consolemenu.console_menu import ConsoleMenu
from consolemenu.items import MenuItem as MenuItem

class SelectionItem(MenuItem):
    index: int
    def __init__(self, text: str, index: int, menu: ConsoleMenu | None = ...) -> None: ...
    def get_return(self) -> int: ...
