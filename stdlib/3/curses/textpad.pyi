from _curses import _CursesWindow
from typing import Callable, Union

def rectangle(win: _CursesWindow, uly: int, ulx: int, lry: int, lrx: int) -> None: ...

class Textbox:
    stripspaces: bool
    def __init__(self, w: _CursesWindow) -> None: ...
    def edit(self, validator: Callable[[int], int]) -> str: ...
    def do_command(self, ch: Union[str,int]) -> None: ...
    def gather(self) -> str: ...
