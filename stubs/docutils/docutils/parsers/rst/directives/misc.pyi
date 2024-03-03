from _typeshed import Incomplete
from collections.abc import Callable
from pathlib import Path
from re import Pattern
from typing import Any, ClassVar, Literal

from docutils.parsers.rst import Directive
from docutils.parsers.rst.states import SpecializedBody

__docformat__: str

class Include(Directive):
    required_arguments: ClassVar[Literal[1]]
    optional_arguments: ClassVar[Literal[0]]
    final_argument_whitespace: ClassVar[Literal[True]]
    option_spec: dict[str, Callable[[str], Any]]
    standard_include_path: Path

class Raw(Directive):
    required_arguments: ClassVar[Literal[1]]
    optional_arguments: ClassVar[Literal[0]]
    final_argument_whitespace: ClassVar[Literal[True]]
    option_spec: dict[str, Callable[[str], Any]]
    has_content: ClassVar[Literal[True]]

class Replace(Directive):
    has_content: ClassVar[Literal[True]]

class Unicode(Directive):
    required_arguments: ClassVar[Literal[1]]
    optional_arguments: ClassVar[Literal[0]]
    final_argument_whitespace: ClassVar[Literal[True]]
    option_spec: dict[str, Callable[[str], Any]]
    comment_pattern: Pattern[str]

class Class(Directive):
    required_arguments: ClassVar[Literal[1]]
    optional_arguments: ClassVar[Literal[0]]
    final_argument_whitespace: ClassVar[Literal[True]]
    has_content: ClassVar[Literal[True]]

class Role(Directive):
    has_content: ClassVar[Literal[True]]
    argument_pattern: Pattern[str]

class DefaultRole(Directive):
    optional_arguments: ClassVar[Literal[1]]
    final_argument_whitespace: ClassVar[Literal[True]]

class Title(Directive):
    required_arguments: ClassVar[Literal[1]]
    optional_arguments: ClassVar[Literal[0]]
    final_argument_whitespace: ClassVar[Literal[True]]

class MetaBody(SpecializedBody):
    def __getattr__(name: str) -> Incomplete: ...

class Meta(Directive):
    has_content: ClassVar[Literal[True]]
    SMkwargs: ClassVar[dict[str, tuple[MetaBody]]]

class Date(Directive):
    has_content: bool

class TestDirective(Directive):
    optional_arguments: ClassVar[Literal[1]]
    final_argument_whitespace: ClassVar[Literal[True]]
    option_spec: dict[str, Callable[[str], Any]]
    has_content: ClassVar[Literal[True]]
