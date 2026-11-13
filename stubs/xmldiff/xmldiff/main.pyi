from _typeshed import StrOrBytesPath, SupportsRead
from argparse import ArgumentParser
from collections.abc import Iterable, Mapping, Sequence
from typing import Any, TypeAlias, overload

from xmldiff.actions import _Action
from xmldiff.formatting import BaseFormatter

__version__: str
FORMATTERS: Mapping[str, BaseFormatter]

_ACTIONS: TypeAlias = _Action
_ET: TypeAlias = Any  # lxml.etree._ElementTree

@overload
def diff_trees(left: _ET, right: _ET, *, diff_options: dict[str, Any] | None = None, formatter: BaseFormatter) -> str: ...
@overload
def diff_trees(
    left: _ET, right: _ET, diff_options: dict[str, Any] | None = None, formatter: None = None
) -> Iterable[_ACTIONS]: ...

@overload
def diff_texts(
    left: str | bytes, right: str | bytes, *, diff_options: dict[str, Any] | None = None, formatter: BaseFormatter
) -> str: ...
@overload
def diff_texts(
    left: str | bytes, right: str | bytes, diff_options: dict[str, Any] | None = None, formatter: None = None
) -> Iterable[_ACTIONS]: ...

@overload
def diff_files(left: str, right: str, *, diff_options: dict[str, Any] | None = None, formatter: BaseFormatter) -> str: ...
@overload
def diff_files(
    left: str, right: str, diff_options: dict[str, Any] | None = None, formatter: None = None
) -> Iterable[_ACTIONS]: ...

def validate_F(arg: float | str) -> float: ...
def make_diff_parser() -> ArgumentParser: ...
def diff_command(args: Sequence[str] | None = None) -> int | None: ...
def patch_tree(actions: Iterable[_ACTIONS], tree: _ET) -> _ET: ...
def patch_text(actions: str, tree: str | bytes) -> str: ...
def patch_file(
    actions: str | SupportsRead[str], tree: StrOrBytesPath | SupportsRead[bytes | str], diff_encoding: str | None = None
) -> str: ...
def make_patch_parser() -> ArgumentParser: ...
def patch_command(args: Sequence[str] | None = None) -> None: ...
