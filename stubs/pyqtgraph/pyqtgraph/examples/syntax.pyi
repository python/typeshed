from _typeshed import Incomplete

QRegExp: Incomplete
QFont: Incomplete
QColor: Incomplete
QTextCharFormat: Incomplete
QSyntaxHighlighter: Incomplete

def format(color, style: str = ""): ...

class LightThemeColors:
    Red: str
    Pink: str
    Purple: str
    DeepPurple: str
    Indigo: str
    Blue: str
    LightBlue: str
    Cyan: str
    Teal: str
    Green: str
    LightGreen: str
    Lime: str
    Yellow: str
    Amber: str
    Orange: str
    DeepOrange: str
    Brown: str
    Grey: str
    BlueGrey: str

class DarkThemeColors:
    Red: str
    Pink: str
    Purple: str
    DeepPurple: str
    Indigo: str
    Blue: str
    LightBlue: str
    Cyan: str
    Teal: str
    Green: str
    LightGreen: str
    Lime: str
    Yellow: str
    Amber: str
    Orange: str
    DeepOrange: str
    Brown: str
    Grey: str
    BlueGrey: str

LIGHT_STYLES: Incomplete
DARK_STYLES: Incomplete

class PythonHighlighter(QSyntaxHighlighter):
    keywords: Incomplete
    operators: Incomplete
    braces: Incomplete
    tri_single: Incomplete
    tri_double: Incomplete
    rules: Incomplete
    def __init__(self, document) -> None: ...
    @property
    def styles(self): ...
    def highlightBlock(self, text) -> None: ...
    def match_multiline(self, text, delimiter, in_state, style): ...
