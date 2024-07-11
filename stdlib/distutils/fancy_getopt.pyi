from collections.abc import Iterable, Mapping
from re import Pattern
from typing import Any, Final, overload
from typing_extensions import TypeAlias

_Option: TypeAlias = tuple[str, str | None, str]
_GR: Final[TypeAlias] = tuple[list[str], OptionDummy]

longopt_pat: str
longopt_re: Pattern[str]
neg_alias_re: Pattern[str]
longopt_xlate: dict[int, int]

class FancyGetopt:
    def __init__(self, option_table: list[_Option] | None = None) -> None: ...
    # TODO kinda wrong, `getopt(object=object())` is invalid
    @overload
    def getopt(self, args: list[str] | None = None) -> _GR: ...
    @overload
    def getopt(self, args: list[str] | None, object: Any) -> list[str]: ...
    def get_option_order(self) -> list[tuple[str, str]]: ...
    def generate_help(self, header: str | None = None) -> list[str]: ...

def fancy_getopt(
    options: list[_Option], negative_opt: Mapping[_Option, _Option], object: Any, args: list[str] | None
) -> list[str] | _GR: ...

WS_TRANS: dict[int, str]

def wrap_text(text: str, width: int) -> list[str]: ...
def translate_longopt(opt: str) -> str: ...

class OptionDummy:
    def __init__(self, options: Iterable[str] = []) -> None: ...
