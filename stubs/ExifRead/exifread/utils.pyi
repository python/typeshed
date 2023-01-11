from _typeshed import Self
from collections.abc import Mapping
from fractions import Fraction
from typing import Any, TypeVar, overload

_T = TypeVar("_T")

@overload
def ord_(dta: str) -> int: ...  # type: ignore[misc]
@overload
def ord_(dta: _T) -> _T: ...
def make_string(seq: str | list[int]) -> str: ...
def make_string_uc(seq: str | list[int]) -> str: ...
def get_gps_coords(tags: Mapping[str, Any]) -> tuple[float, float]: ...

class Ratio(Fraction):
    def __new__(cls: type[Self], numerator: int = ..., denominator: int | None = ...) -> Self: ...
    @property
    def num(self) -> int: ...
    @property
    def den(self) -> int: ...
    def decimal(self) -> float: ...
