from _typeshed import SupportsRead
from collections.abc import Callable
from datetime import date, datetime, time
from typing import Any
from typing_extensions import TypeAlias

__all__ = ("loads", "load", "TOMLDecodeError")

class TOMLDecodeError(ValueError): ...

_TOMLValue: TypeAlias = int | float | str | bool | list[_TOMLValue] | dict[_TOMLValue, _TOMLValue] | datetime | date | time

def load(__fp: SupportsRead[bytes], *, parse_float: Callable[[str], Any] = ...) -> dict[str, _TOMLValue]: ...
def loads(__s: str, *, parse_float: Callable[[str], Any] = ...) -> dict[str, _TOMLValue]: ...
