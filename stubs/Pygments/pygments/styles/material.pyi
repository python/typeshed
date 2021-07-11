from pygments.style import Style as Style
from pygments.token import Comment as Comment, Error as Error, Escape as Escape, Generic as Generic, Keyword as Keyword, Literal as Literal, Name as Name, Number as Number, Operator as Operator, Punctuation as Punctuation, String as String, Text as Text
from typing import Any

class MaterialStyle(Style):
    dark_teal: str = ...
    white: str = ...
    black: str = ...
    red: str = ...
    orange: str = ...
    yellow: str = ...
    green: str = ...
    cyan: str = ...
    blue: str = ...
    paleblue: str = ...
    purple: str = ...
    brown: str = ...
    pink: str = ...
    violet: str = ...
    foreground: str = ...
    faded: str = ...
    default_style: str = ...
    background_color: Any = ...
    highlight_color: str = ...
    line_number_color: str = ...
    line_number_background_color: Any = ...
    line_number_special_color: str = ...
    line_number_special_background_color: Any = ...
    styles: Any = ...
