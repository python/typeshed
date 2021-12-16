import sys
from _typeshed import StrOrBytesPath
from cProfile import Profile as _cProfile
from profile import Profile
from typing import IO, Any, Iterable, Tuple, TypeVar,  overload

_Selector = str | float | int
_T = TypeVar("_T", bound=Stats)

if sys.version_info >= (3, 7):
    from enum import Enum
    class SortKey(str, Enum):
        CALLS: str
        CUMULATIVE: str
        FILENAME: str
        LINE: str
        NAME: str
        NFL: str
        PCALLS: str
        STDNAME: str
        TIME: str

class Stats:
    sort_arg_dict_default: dict[str, tuple[Any, str]]
    def __init__(
        self: _T,
        __arg: None | str | Profile | _cProfile = ...,
        *args: None | str | Profile | _cProfile | _T,
        stream: IO[Any] | None = ...,
    ) -> None: ...
    def init(self, arg: None | str | Profile | _cProfile) -> None: ...
    def load_stats(self, arg: None | str | Profile | _cProfile) -> None: ...
    def get_top_level_stats(self) -> None: ...
    def add(self: _T, *arg_list: None | str | Profile | _cProfile | _T) -> _T: ...
    def dump_stats(self, filename: StrOrBytesPath) -> None: ...
    def get_sort_arg_defs(self) -> dict[str, tuple[Tuple[tuple[int, int], ...], str]]: ...
    @overload
    def sort_stats(self: _T, field: int) -> _T: ...
    @overload
    def sort_stats(self: _T, *field: str) -> _T: ...
    def reverse_order(self: _T) -> _T: ...
    def strip_dirs(self: _T) -> _T: ...
    def calc_callees(self) -> None: ...
    def eval_print_amount(self, sel: _Selector, list: list[str], msg: str) -> tuple[list[str], str]: ...
    def get_print_list(self, sel_list: Iterable[_Selector]) -> tuple[int, list[str]]: ...
    def print_stats(self: _T, *amount: _Selector) -> _T: ...
    def print_callees(self: _T, *amount: _Selector) -> _T: ...
    def print_callers(self: _T, *amount: _Selector) -> _T: ...
    def print_call_heading(self, name_size: int, column_title: str) -> None: ...
    def print_call_line(self, name_size: int, source: str, call_dict: dict[str, Any], arrow: str = ...) -> None: ...
    def print_title(self) -> None: ...
    def print_line(self, func: str) -> None: ...
