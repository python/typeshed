from pygments.style import Style as Style
from pygments.token import Comment as Comment, Error as Error, Keyword as Keyword, Name as Name, Number as Number, Operator as Operator, String as String, Text as Text, Whitespace as Whitespace
from typing import Any

class StataLightStyle(Style):
    default_style: str = ...
    styles: Any = ...
