from pygments.style import Style as Style
from pygments.token import Comment as Comment, Error as Error, Generic as Generic, Keyword as Keyword, Name as Name, Number as Number, Operator as Operator, String as String, Whitespace as Whitespace
from typing import Any

class ManniStyle(Style):
    background_color: str = ...
    styles: Any = ...
