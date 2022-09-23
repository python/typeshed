from collections.abc import Iterable
from typing import Any
from typing_extensions import Literal, TypeAlias

_Unit: TypeAlias = Literal["pt", "mm", "cm", "in"]

def enclose_in_parens(s): ...
def escape_parens(s): ...
def b(s): ...
def get_scale_factor(unit: _Unit | float) -> float: ...
def convert_unit(
    # to_convert has a recursive type
    to_convert: float | Iterable[float | Iterable[Any]],
    old_unit: str | float,
    new_unit: str | float,
) -> float | tuple[float, ...]: ...
def dochecks() -> None: ...
