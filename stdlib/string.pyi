import sys
from _typeshed import StrOrLiteralStr
from collections.abc import Iterable, Mapping, Sequence
from re import Pattern, RegexFlag
from typing import Any, ClassVar, overload
from typing_extensions import LiteralString, TypeAlias

__all__ = [
    "ascii_letters",
    "ascii_lowercase",
    "ascii_uppercase",
    "capwords",
    "digits",
    "hexdigits",
    "octdigits",
    "printable",
    "punctuation",
    "whitespace",
    "Formatter",
    "Template",
]

ascii_letters: LiteralString
ascii_lowercase: LiteralString
ascii_uppercase: LiteralString
digits: LiteralString
hexdigits: LiteralString
octdigits: LiteralString
punctuation: LiteralString
printable: LiteralString
whitespace: LiteralString

def capwords(s: StrOrLiteralStr, sep: StrOrLiteralStr | None = ...) -> StrOrLiteralStr: ...

if sys.version_info >= (3, 9):
    _TemplateMetaclass: TypeAlias = type
else:
    class _TemplateMetaclass(type):
        pattern: ClassVar[str]
        def __init__(cls, name: str, bases: tuple[type, ...], dct: dict[str, Any]) -> None: ...

class Template(metaclass=_TemplateMetaclass):
    template: str
    delimiter: ClassVar[str]
    idpattern: ClassVar[str]
    braceidpattern: ClassVar[str | None]
    flags: ClassVar[RegexFlag]
    pattern: ClassVar[Pattern[str]]
    def __init__(self, template: str) -> None: ...
    def substitute(self, __mapping: Mapping[str, object] = ..., **kwds: object) -> str: ...
    def safe_substitute(self, __mapping: Mapping[str, object] = ..., **kwds: object) -> str: ...
    if sys.version_info >= (3, 11):
        def get_identifiers(self) -> list[str]: ...
        def is_valid(self) -> bool: ...

class Formatter:
    @overload
    def format(self, __format_string: LiteralString, *args: LiteralString, **kwargs: LiteralString) -> LiteralString: ...
    @overload
    def format(self, __format_string: str, *args: Any, **kwargs: Any) -> str: ...
    @overload
    def vformat(
        self, format_string: LiteralString, args: Sequence[LiteralString], kwargs: Mapping[LiteralString, LiteralString]
    ) -> LiteralString: ...
    @overload
    def vformat(self, format_string: str, args: Sequence[Any], kwargs: Mapping[str, Any]) -> str: ...
    def _vformat(
        self,
        format_string: str,
        args: Sequence[Any],
        kwargs: Mapping[str, Any],
        used_args: Sequence[int | str],
        recursion_depth: int,
        auto_arg_index: int = ...,
    ) -> str | bool: ...
    def parse(
        self, format_string: StrOrLiteralStr
    ) -> Iterable[tuple[StrOrLiteralStr, StrOrLiteralStr | None, StrOrLiteralStr | None, StrOrLiteralStr | None]]: ...
    def get_field(self, field_name: str, args: Sequence[Any], kwargs: Mapping[str, Any]) -> Any: ...
    def get_value(self, key: int | str, args: Sequence[Any], kwargs: Mapping[str, Any]) -> Any: ...
    def check_unused_args(self, used_args: Sequence[int | str], args: Sequence[Any], kwargs: Mapping[str, Any]) -> None: ...
    def format_field(self, value: Any, format_spec: str) -> Any: ...
    def convert_field(self, value: Any, conversion: str) -> Any: ...
