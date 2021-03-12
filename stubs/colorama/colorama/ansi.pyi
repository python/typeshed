CSI: str
OSC: str
BEL: str

def code_to_chars(code: int) -> str: ...
def set_title(title: str) -> str: ...
def clear_screen(mode: int = ...) -> str: ...
def clear_line(mode: int = ...) -> str: ...

class AnsiCodes:
    def __init__(self) -> None: ...

class AnsiCursor:
    def UP(self, n: int = ...) -> str: ...
    def DOWN(self, n: int = ...) -> str: ...
    def FORWARD(self, n: int = ...) -> str: ...
    def BACK(self, n: int = ...) -> str: ...
    def POS(self, x: int = ..., y: int = ...) -> str: ...

class AnsiFore(AnsiCodes):
    BLACK: str = ...
    RED: str = ...
    GREEN: str = ...
    YELLOW: str = ...
    BLUE: str = ...
    MAGENTA: str = ...
    CYAN: str = ...
    WHITE: str = ...
    RESET: str = ...
    LIGHTBLACK_EX: str = ...
    LIGHTRED_EX: str = ...
    LIGHTGREEN_EX: str = ...
    LIGHTYELLOW_EX: str = ...
    LIGHTBLUE_EX: str = ...
    LIGHTMAGENTA_EX: str = ...
    LIGHTCYAN_EX: str = ...
    LIGHTWHITE_EX: str = ...

class AnsiBack(AnsiCodes):
    BLACK: str = ...
    RED: str = ...
    GREEN: str = ...
    YELLOW: str = ...
    BLUE: str = ...
    MAGENTA: str = ...
    CYAN: str = ...
    WHITE: str = ...
    RESET: str = ...
    LIGHTBLACK_EX: str = ...
    LIGHTRED_EX: str = ...
    LIGHTGREEN_EX: str = ...
    LIGHTYELLOW_EX: str = ...
    LIGHTBLUE_EX: str = ...
    LIGHTMAGENTA_EX: str = ...
    LIGHTCYAN_EX: str = ...
    LIGHTWHITE_EX: str = ...

class AnsiStyle(AnsiCodes):
    BRIGHT: str = ...
    DIM: str = ...
    NORMAL: str = ...
    RESET_ALL: str = ...

Fore: AnsiFore
Back: AnsiBack
Style: AnsiStyle
Cursor: AnsiCursor
