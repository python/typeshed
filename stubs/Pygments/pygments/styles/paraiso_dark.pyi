from pygments.style import Style as Style
from pygments.token import Comment as Comment, Error as Error, Generic as Generic, Keyword as Keyword, Literal as Literal, Name as Name, Number as Number, Operator as Operator, Other as Other, Punctuation as Punctuation, String as String, Text as Text, Whitespace as Whitespace
from typing import Any

BACKGROUND: str
CURRENT_LINE: str
SELECTION: str
FOREGROUND: str
COMMENT: str
RED: str
ORANGE: str
YELLOW: str
GREEN: str
AQUA: str
BLUE: str
PURPLE: str

class ParaisoDarkStyle(Style):
    default_style: str = ...
    background_color: Any = ...
    highlight_color: Any = ...
    styles: Any = ...
