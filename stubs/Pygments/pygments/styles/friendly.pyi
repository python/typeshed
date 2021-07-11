from pygments.style import Style as Style
from pygments.token import Comment as Comment, Error as Error, Generic as Generic, Keyword as Keyword, Name as Name, Number as Number, Operator as Operator, String as String, Whitespace as Whitespace
from typing import Any

class FriendlyStyle(Style):
    background_color: str = ...
    default_style: str = ...
    line_number_color: str = ...
    styles: Any = ...
