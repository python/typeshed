from collections.abc import Sequence
from typing import TypeVar

from docutils.parsers.rst import Directive

_Context = TypeVar("_Context")

class Contents(Directive[_Context]):
    backlinks_values: Sequence[str]

class Sectnum(Directive[_Context]): ...
class Header(Directive[_Context]): ...
class Footer(Directive[_Context]): ...
