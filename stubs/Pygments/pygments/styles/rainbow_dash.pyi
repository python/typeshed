from pygments.style import Style as Style
from pygments.token import Comment as Comment, Error as Error, Generic as Generic, Keyword as Keyword, Name as Name, Number as Number, Operator as Operator, String as String, Text as Text, Whitespace as Whitespace
from typing import Any

BLUE_LIGHT: str
BLUE: str
GREEN: str
GREEN_LIGHT: str
GREEN_NEON: str
GREY: str
GREY_LIGHT: str
GREY_DARK: str
PURPLE: str
RED: str
RED_DARK: str
RED_LIGHT: str
RED_BRIGHT: str
WHITE: str
TURQUOISE: str
ORANGE: str

class RainbowDashStyle(Style):
    background_color: Any = ...
    styles: Any = ...
