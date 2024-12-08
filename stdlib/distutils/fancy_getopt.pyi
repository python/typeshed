from collections.abc import Iterable, Mapping, Sequence
from re import Pattern
from typing import Any, Final, TypeVar, overload
from typing_extensions import TypeAlias

_Option: TypeAlias = tuple[str, str | None, str]
_StrSequenceT = TypeVar("_StrSequenceT", bound=Sequence[str], default=list[str])
_GR: TypeAlias = tuple[_StrSequenceT, OptionDummy]

longopt_pat: Final = r"[a-zA-Z](?:[a-zA-Z0-9-]*)"
longopt_re: Final[Pattern[str]]
neg_alias_re: Final[Pattern[str]]
longopt_xlate: Final[dict[int, int]]

class FancyGetopt:
    def __init__(self, option_table: list[_Option] | None = None) -> None: ...
    # TODO kinda wrong, `getopt(object=object())` is invalid
    @overload
    def getopt(self, args: _StrSequenceT | None = None, object: None = None) -> _GR[_StrSequenceT]: ...
    @overload
    def getopt(self, args: _StrSequenceT | None, object: Any) -> _StrSequenceT: ...
    def get_option_order(self) -> list[tuple[str, str]]: ...
    def generate_help(self, header: str | None = None) -> list[str]: ...

# Same note as FancyGetopt.getopt
@overload
def fancy_getopt(
    options: list[_Option], negative_opt: Mapping[_Option, _Option], object: None, args: _StrSequenceT | None
) -> _GR[_StrSequenceT]: ...
@overload
def fancy_getopt(
    options: list[_Option], negative_opt: Mapping[_Option, _Option], object: Any, args: _StrSequenceT | None
) -> _StrSequenceT: ...

WS_TRANS: Final[dict[int, str]]

def wrap_text(text: str, width: int) -> list[str]: ...
def translate_longopt(opt: str) -> str: ...

class OptionDummy:
    def __init__(self, options: Iterable[str] = []) -> None: ...
