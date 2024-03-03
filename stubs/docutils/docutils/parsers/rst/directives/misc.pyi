from _typeshed import Incomplete
from collections.abc import Callable
from pathlib import Path
from re import Pattern
from typing import Any, ClassVar

from docutils.parsers.rst import Directive
from docutils.parsers.rst.states import SpecializedBody

__docformat__: str

class Include(Directive):
    required_arguments: ClassVar[int]
    optional_arguments: ClassVar[int]
    final_argument_whitespace: ClassVar[bool]
    option_spec: dict[str, Callable[[str], Any]]
    standard_include_path: Path

class Raw(Directive):
    required_arguments: ClassVar[int]
    optional_arguments: ClassVar[int]
    final_argument_whitespace: ClassVar[bool]
    option_spec: dict[str, Callable[[str], Any]]
    has_content: ClassVar[bool]

class Replace(Directive):
    has_content: ClassVar[bool]

class Unicode(Directive):
    required_arguments: ClassVar[int]
    optional_arguments: ClassVar[int]
    final_argument_whitespace: ClassVar[bool]
    option_spec: dict[str, Callable[[str], Any]]
    comment_pattern: Pattern[str]

class Class(Directive):
    required_arguments: ClassVar[int]
    optional_arguments: ClassVar[int]
    final_argument_whitespace: ClassVar[bool]
    has_content: ClassVar[bool]

class Role(Directive):
    has_content: ClassVar[bool]
    argument_pattern: Pattern[str]

class DefaultRole(Directive):
    optional_arguments: ClassVar[int]
    final_argument_whitespace: ClassVar[bool]

class Title(Directive):
    required_arguments: ClassVar[int]
    optional_arguments: ClassVar[int]
    final_argument_whitespace: ClassVar[bool]

class MetaBody(SpecializedBody):
    def __getattr__(self, name: str) -> Incomplete: ...

class Meta(Directive):
    has_content: ClassVar[bool]
    SMkwargs: ClassVar[dict[str, tuple[MetaBody]]]

class Date(Directive):
    has_content: bool

class TestDirective(Directive):
    optional_arguments: ClassVar[int]
    final_argument_whitespace: ClassVar[bool]
    option_spec: dict[str, Callable[[str], Any]]
    has_content: ClassVar[bool]
