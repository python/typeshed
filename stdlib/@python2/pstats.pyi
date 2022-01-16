from _typeshed import Self
from cProfile import Profile as _cProfile
from profile import Profile
from typing import IO, Any, Dict, Iterable, List, Text, Tuple, TypeVar, Union, overload

_Selector = Union[str, float, int]
_T = TypeVar("_T", bound=Stats)

class Stats:
    sort_arg_dict_default: Dict[str, Tuple[Any, str]]
    def __init__(
        self: _T,
        __arg: None | str | Text | Profile | _cProfile = ...,
        *args: None | str | Text | Profile | _cProfile | _T,
        stream: IO[Any] | None = ...,
    ) -> None: ...
    def init(self, arg: None | str | Text | Profile | _cProfile) -> None: ...
    def load_stats(self, arg: None | str | Text | Profile | _cProfile) -> None: ...
    def get_top_level_stats(self) -> None: ...
    def add(self: Self, *arg_list: None | str | Text | Profile | _cProfile | Self) -> Self: ...
    def dump_stats(self, filename: Text) -> None: ...
    def get_sort_arg_defs(self) -> Dict[str, Tuple[Tuple[Tuple[int, int], ...], str]]: ...
    @overload
    def sort_stats(self: Self, field: int) -> Self: ...
    @overload
    def sort_stats(self: Self, *field: str) -> Self: ...
    def reverse_order(self: Self) -> Self: ...
    def strip_dirs(self: Self) -> Self: ...
    def calc_callees(self) -> None: ...
    def eval_print_amount(self, sel: _Selector, list: List[str], msg: str) -> Tuple[List[str], str]: ...
    def get_print_list(self, sel_list: Iterable[_Selector]) -> Tuple[int, List[str]]: ...
    def print_stats(self: Self, *amount: _Selector) -> Self: ...
    def print_callees(self: Self, *amount: _Selector) -> Self: ...
    def print_callers(self: Self, *amount: _Selector) -> Self: ...
    def print_call_heading(self, name_size: int, column_title: str) -> None: ...
    def print_call_line(self, name_size: int, source: str, call_dict: Dict[str, Any], arrow: str = ...) -> None: ...
    def print_title(self) -> None: ...
    def print_line(self, func: str) -> None: ...
