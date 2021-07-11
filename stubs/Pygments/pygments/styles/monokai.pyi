from pygments.style import Style as Style
from pygments.token import Comment as Comment, Error as Error, Generic as Generic, Keyword as Keyword, Literal as Literal, Name as Name, Number as Number, Operator as Operator, Other as Other, Punctuation as Punctuation, String as String, Text as Text, Whitespace as Whitespace
from typing import Any

class MonokaiStyle(Style):
    background_color: str = ...
    highlight_color: str = ...
    styles: Any = ...
