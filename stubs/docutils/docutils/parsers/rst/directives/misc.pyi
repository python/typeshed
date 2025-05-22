from pathlib import Path
from re import Pattern
from typing import ClassVar, Final

from docutils.parsers.rst import Directive
from docutils.parsers.rst.states import SpecializedBody

__docformat__: Final = "reStructuredText"

class Include(Directive):
    standard_include_path: Path

class Raw(Directive): ...
class Replace(Directive): ...

class Unicode(Directive):
    comment_pattern: Pattern[str]

class Class(Directive): ...

class Role(Directive):
    argument_pattern: Pattern[str]

class DefaultRole(Directive): ...
class Title(Directive): ...

class MetaBody(SpecializedBody):
    def field_marker(self, match, context, next_state): ...
    def parsemeta(self, match): ...

class Meta(Directive):
    SMkwargs: ClassVar[dict[str, tuple[MetaBody]]]

class Date(Directive): ...
class TestDirective(Directive): ...
