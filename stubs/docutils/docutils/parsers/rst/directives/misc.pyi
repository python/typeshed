from _typeshed import StrPath
from collections.abc import Callable, Sequence
from pathlib import Path
from re import Match, Pattern
from typing import ClassVar, Final

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst.states import SpecializedBody

__docformat__: Final = "reStructuredText"

def adapt_path(path: str, source: StrPath = "", root_prefix: StrPath = "") -> str: ...

class Include(Directive):
    option_spec: ClassVar[dict[str, Callable[[str], object]]]
    standard_include_path: ClassVar[Path]
    def run(self) -> Sequence[nodes.Node]: ...
    def read_file(self, path: StrPath) -> str: ...
    def as_literal_block(self, text: str) -> list[nodes.literal_block]: ...
    def as_code_block(self, text: str) -> list[nodes.literal_block]: ...
    def custom_parse(self, text: str) -> Sequence[nodes.Node]: ...
    def insert_into_input_lines(self, text: str) -> None: ...

class Raw(Directive):
    option_spec: ClassVar[dict[str, Callable[[str], object]]]
    def run(self) -> Sequence[nodes.Node]: ...

class Replace(Directive):
    def run(self) -> Sequence[nodes.Node]: ...

class Unicode(Directive):
    option_spec: ClassVar[dict[str, Callable[[str], object]]]
    comment_pattern: ClassVar[Pattern[str]]
    def run(self) -> Sequence[nodes.Node]: ...

class Class(Directive):
    def run(self) -> Sequence[nodes.Node]: ...

class Role(Directive):
    argument_pattern: ClassVar[Pattern[str]]
    def run(self) -> Sequence[nodes.Node]: ...

class DefaultRole(Directive):
    def run(self) -> Sequence[nodes.Node]: ...

class Title(Directive):
    def run(self) -> Sequence[nodes.Node]: ...

class MetaBody(SpecializedBody):
    def field_marker(
        self, match: Match[str], context: list[str], next_state: str | None
    ) -> tuple[list[str], str | None, list[str]]: ...
    def parsemeta(self, match: Match[str]) -> tuple[nodes.meta | nodes.system_message, bool]: ...

class Meta(Directive):
    SMkwargs: ClassVar[dict[str, tuple[type[MetaBody]]]]
    def run(self) -> Sequence[nodes.Node]: ...

class Date(Directive):
    def run(self) -> Sequence[nodes.Node]: ...

class TestDirective(Directive):
    option_spec: ClassVar[dict[str, Callable[[str], object]]]
    def run(self) -> Sequence[nodes.Node]: ...
