from pygments.style import Style as Style
from pygments.token import Comment as Comment, Error as Error, Generic as Generic, Keyword as Keyword, Name as Name, Number as Number, Operator as Operator, String as String, Whitespace as Whitespace
from typing import Any

class TracStyle(Style):
    default_style: str = ...
    styles: Any = ...
