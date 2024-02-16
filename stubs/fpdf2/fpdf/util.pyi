from collections.abc import Iterable
from typing import Any, AnyStr, Final, Literal, NamedTuple
from typing_extensions import TypeAlias

_Unit: TypeAlias = Literal["pt", "mm", "cm", "in"]

PIL_MEM_BLOCK_SIZE_IN_MIB: Final = 16

class Padding(NamedTuple):
    top: float = 0
    right: float = 0
    bottom: float = 0
    left: float = 0
    @classmethod
    def new(cls, padding: float | tuple[float, ...] | list[float]): ...

def buffer_subst(buffer: bytearray, placeholder: str, value: str) -> bytearray: ...
def escape_parens(s: AnyStr) -> AnyStr: ...
def get_scale_factor(unit: _Unit | float) -> float: ...
def convert_unit(
    # to_convert has a recursive type
    to_convert: float | Iterable[float | Iterable[Any]],
    old_unit: str | float,
    new_unit: str | float,
) -> float | tuple[float, ...]: ...
def print_mem_usage(prefix: str) -> None: ...
def get_mem_usage(prefix: str) -> str: ...
def get_process_rss() -> str: ...
def get_process_rss_as_mib() -> float | None: ...
def get_process_heap_and_stack_sizes() -> tuple[str, str]: ...
def get_pymalloc_allocated_over_total_size() -> str: ...
def get_gc_managed_objs_total_size() -> str: ...
def get_tracemalloc_traced_memory() -> str: ...
def get_pillow_allocated_memory() -> str: ...
