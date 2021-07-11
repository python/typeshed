from pygments.style import Style as Style
from pygments.token import Comment as Comment, Keyword as Keyword, Name as Name, String as String
from typing import Any

class IgorStyle(Style):
    default_style: str = ...
    styles: Any = ...
