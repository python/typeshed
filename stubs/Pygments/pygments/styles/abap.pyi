from pygments.style import Style as Style
from pygments.token import Comment as Comment, Error as Error, Keyword as Keyword, Name as Name, Number as Number, Operator as Operator, String as String
from typing import Any

class AbapStyle(Style):
    default_style: str = ...
    styles: Any = ...
