from pygments.style import Style as Style
from pygments.token import Comment as Comment, Error as Error, Generic as Generic, Keyword as Keyword, Literal as Literal, Name as Name, Number as Number, Operator as Operator, Other as Other, Punctuation as Punctuation, String as String, Whitespace as Whitespace
from typing import Any

class TangoStyle(Style):
    background_color: str = ...
    default_style: str = ...
    styles: Any = ...
