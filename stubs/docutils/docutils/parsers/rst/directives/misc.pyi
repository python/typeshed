from _typeshed import Incomplete
from pathlib import Path
from re import Pattern
from typing import ClassVar, TypeVar

from docutils.parsers.rst import Directive
from docutils.parsers.rst.states import SpecializedBody

__docformat__: str

_Context = TypeVar("_Context")

class Include(Directive[_Context]):
    standard_include_path: Path

class Raw(Directive[_Context]): ...
class Replace(Directive[_Context]): ...

class Unicode(Directive[_Context]):
    comment_pattern: Pattern[str]

class Class(Directive[_Context]): ...

class Role(Directive[_Context]):
    argument_pattern: Pattern[str]

class DefaultRole(Directive[_Context]): ...
class Title(Directive[_Context]): ...

# SpecializedBody has not yet been stubbed
class MetaBody(SpecializedBody):  # pyright: ignore[reportUntypedBaseClass]
    def __getattr__(self, name: str) -> Incomplete: ...

class Meta(Directive[_Context]):
    SMkwargs: ClassVar[dict[str, tuple[MetaBody]]]

class Date(Directive[_Context]): ...
class TestDirective(Directive[_Context]): ...
