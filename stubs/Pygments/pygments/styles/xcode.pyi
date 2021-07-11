from pygments.style import Style as Style
from pygments.token import Comment as Comment, Error as Error, Keyword as Keyword, Literal as Literal, Name as Name, Number as Number, Operator as Operator, String as String
from typing import Any

class XcodeStyle(Style):
    default_style: str = ...
    styles: Any = ...
