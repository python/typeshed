from collections.abc import Callable, Container, Iterable, Sequence
from re import Pattern
from typing import Literal

from docutils.languages import _LanguageModule
from docutils.nodes import document
from docutils.parsers import Parser
from docutils.parsers.rst import Directive
from docutils.utils import SystemMessage

def register_directive(name: str, directive: type[Directive]) -> None: ...
def directive(
    directive_name: str, language_module: _LanguageModule, document: document
) -> tuple[type[Directive] | None, list[SystemMessage]]: ...
def flag(argument: str | None) -> None: ...
def unchanged_required(argument: str) -> str: ...
def unchanged(argument: str | None) -> str: ...
def path(argument: str) -> str: ...
def uri(argument: str) -> str: ...
def nonnegative_int(argument: str) -> int: ...
def percentage(argument: str) -> int: ...

length_units: list[str]

def get_measure(argument: str, units: Iterable[str]) -> str: ...
def length_or_unitless(argument: str) -> str: ...
def length_or_percentage_or_unitless(argument: str, default: str = "") -> str: ...
def class_option(argument: str) -> list[str]: ...

unicode_pattern: Pattern[str]

def unicode_code(code: str) -> str: ...
def single_char_or_unicode(argument: str) -> str: ...
def single_char_or_whitespace_or_unicode(argument: str | Literal["tab", "space"]) -> str: ...
def positive_int(argument: str) -> int: ...
def positive_int_list(argument: str) -> list[int]: ...
def encoding(argument: str) -> str: ...
def choice(argument: str, values: Sequence[str]) -> str: ...
def format_values(values: Sequence[str]) -> str: ...
def value_or(values: Container[str], other: Callable[[str], str]) -> Callable[[str], str]: ...
def parser_name(argument: str | None) -> type[Parser] | None: ...
