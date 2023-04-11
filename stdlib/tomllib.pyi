from _typeshed import SupportsRead
from collections.abc import Callable
from datetime import date, datetime, time
from typing import Any, TypeAlias

__all__ = ("loads", "load", "TOMLDecodeError")

class TOMLDecodeError(ValueError): ...

TOMLValue: TypeAlias = int | float | str | bool | list["TOMLValue"] | dict["TOMLValue", "TOMLValue"] | datetime | date | time

def load(__fp: SupportsRead[bytes], *, parse_float: Callable[[str], Any] = ...) -> dict[str, TOMLValue]: ...
def loads(__s: str, *, parse_float: Callable[[str], Any] = ...) -> dict[str, TOMLValue]: ...
