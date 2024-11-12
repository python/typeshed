"""
Assuming X, Y and Z are types other than None, the following rules apply to the slice type:

- The type hint `slice` should be compatible with all slices, including:
    - `slice(None)`, `slice(None, None)` and `slice(None, None, None)`. (⟿ `slice[?, ?, ?]`)
- The type hint `slice[T]` should be compatible with:
    - `slice(None)`, `slice(None, None)` and `slice(None, None, None)` (⟿ `slice[?, ?, ?]`)
    - `slice(t)`, `slice(None, t)` and `slice(None, t, None)`.  (⟿ `slice[?, T, ?]`)
    - `slice(t, None)` and `slice(t, None, None)`.  (⟿ `slice[T, ?, ?]`)
    - `slice(t, t)` and `slice(t, t, None)`.  (⟿ `slice[T, T, ?]`)
- The type hint `slice[X, Y]` should be compatible with:
    - `slice(None)`, `slice(None, None)` and `slice(None, None, None)` (⟿ `slice[?, ?, ?]`)
    - `slice(y)`, `slice(None, y)` and `slice(None, y, None)`.  (⟿ `slice[?, Y, ?]`)
    - `slice(x, None)` and `slice(x, None, None)` (⟿ `slice[X, ?, ?]`)
    - `slice(x, y)` and `slice(x, y, None)`.  (⟿ `slice[X, Y, ?]`)
-  The type hint `slice[X, Y, Z]` should be compatible with:
    - `slice(None)`, `slice(None, None)` and `slice(None, None, None)`. (⟿ `slice[?, ?, ?]`)
    - `slice(y)`, `slice(None, y)` and `slice(None, y, None)`.   (⟿ `slice[?, Y, ?]`)
    - `slice(x, None)` and `slice(x, None, None)` (⟿ `slice[X, ?, ?]`)
    - `slice(x, y)` and `slice(x, y, None)`.  (⟿ `slice[X, Y, ?]`)
    - `slice(None, None, z)`  (⟿ `slice[?, ?, Z]`)
    - `slice(None, y, z)`   (⟿ `slice[?, Y, Z]`)
    - `slice(x, None, z)`   (⟿ `slice[X, ?, Z]`)
    - `slice(x, y, z)`  (⟿ `slice[X, Y, Z]`)

Consistency criterion: Assuming now X, Y, Z can potentially be None, the following rules apply:

- `slice(x)` must be compatible with `slice[None, X, None]`, even if X is None.
- `slice(x, y)` must be compatible with `slice[X,Y,None]`, even if X is None or Y is None.
- `slice(x, y, z)` must be compatible with `slice[X, Y, Z]`, even if X, Y, or Z are `None`.
"""

from datetime import datetime as DT, timedelta as TD
from typing import Any
from typing_extensions import assert_type

# region Tests for slice constructor overloads -----------------------------------------
assert_type(slice(None), "slice[Any, Any, Any]")
assert_type(slice(None, None), "slice[Any, Any, Any]")
assert_type(slice(None, None, None), "slice[Any, Any, Any]")

assert_type(slice(1), "slice[Any, int, Any]")
assert_type(slice(None, 1), "slice[Any, int, Any]")
assert_type(slice(None, 1, None), "slice[Any, int, Any]")

assert_type(slice(1, None), "slice[int, Any, Any]")
assert_type(slice(1, None, None), "slice[int, Any, Any]")

assert_type(slice(1, 1), "slice[int, int, Any]")
assert_type(slice(1, 1, None), "slice[int, int, Any]")

assert_type(slice(1, 1, 1), "slice[int, int, int]")
# endregion Tests for slice constructor overloads --------------------------------------

# region Test for slice assignments ----------------------------------------------------
# exhaustively test all possible assignments: miss (X), None (N), int (I), and str (S)
rXNX: slice = slice(None)
rXIX: slice = slice(1)
rXSX: slice = slice("1970-01-01")

rNNX: slice = slice(None, None)
rINX: slice = slice(1, None)
rSNX: slice = slice("1970-01-01", None)

rNIX: slice = slice(None, 2)
rIIX: slice = slice(1, 2)
rSIX: slice = slice("1970-01-01", 2)

rNSX: slice = slice(None, "1971-01-01")
rISX: slice = slice(1, "1971-01-01")
rSSX: slice = slice("1970-01-01", "1971-01-01")

rNNN: slice = slice(None, None, None)
rINN: slice = slice(1, None, None)
rSNN: slice = slice("1970-01-01", None, None)
rNIN: slice = slice(None, 2, None)
rIIN: slice = slice(1, 2, None)
rSIN: slice = slice("1970-01-01", 2, None)
rNSN: slice = slice(None, "1971-01-01", None)
rISN: slice = slice(1, "1971-01-01", None)
rSSN: slice = slice("1970-01-01", "1971-01-01", None)

rNNI: slice = slice(None, None, 3)
rINI: slice = slice(1, None, 3)
rSNI: slice = slice("1970-01-01", None, 3)
rNII: slice = slice(None, 2, 3)
rIII: slice = slice(1, 2, 3)
rSII: slice = slice("1970-01-01", 2, 3)
rNSI: slice = slice(None, "1971-01-01", 3)
rISI: slice = slice(1, "1971-01-01", 3)
rSSI: slice = slice("1970-01-01", "1971-01-01", 3)

rNNS: slice = slice(None, None, "1d")
rINS: slice = slice(1, None, "1d")
rSNS: slice = slice("1970-01-01", None, "1d")
rNIS: slice = slice(None, 2, "1d")
rIIS: slice = slice(1, 2, "1d")
rSIS: slice = slice("1970-01-01", 2, "1d")
rNSS: slice = slice(None, "1971-01-01", "1d")
rISS: slice = slice(1, "1971-01-01", "1d")
rSSS: slice = slice("1970-01-01", "1971-01-01", "1d")
# endregion Test for slice assignments -------------------------------------------------


# region Tests for slice[T] assignments ------------------------------------------------
sXNX: "slice[int]" = slice(None)
sXIX: "slice[int]" = slice(1)

sNNX: "slice[int]" = slice(None, None)
sNIX: "slice[int]" = slice(None, 2)
sINX: "slice[int]" = slice(1, None)
sIIX: "slice[int]" = slice(1, 2)

sNNN: "slice[int]" = slice(None, None, None)
sNIN: "slice[int]" = slice(None, 2, None)
sNNS: "slice[int]" = slice(None, None, "1d")
sINN: "slice[int]" = slice(1, None, None)
sINS: "slice[int]" = slice(1, None, "1d")
sIIN: "slice[int]" = slice(1, 2, None)
sIIS: "slice[int]" = slice(1, 2, "1d")
# endregion Tests for slice[T] assignments ---------------------------------------------


# region Tests for slice[X, Y] assignments ---------------------------------------------
# Note: start=int is illegal and hence we add an explicit "type: ignore" comment.
tXNX: "slice[None, int]" = slice(None)  # since slice(None) is slice[Any, Any, Any]
tXIX: "slice[None, int]" = slice(1)

tNNX: "slice[None, int]" = slice(None, None)
tNIX: "slice[None, int]" = slice(None, 2)
tINX: "slice[None, int]" = slice(1, None)  # type: ignore
tIIX: "slice[None, int]" = slice(1, 2)  # type: ignore

tNNN: "slice[None, int]" = slice(None, None, None)
tNIN: "slice[None, int]" = slice(None, 2, None)
tINN: "slice[None, int]" = slice(1, None, None)  # type: ignore
tIIN: "slice[None, int]" = slice(1, 2, None)  # type: ignore
tNNS: "slice[None, int]" = slice(None, None, "1d")
tINS: "slice[None, int]" = slice(None, 2, "1d")
tNIS: "slice[None, int]" = slice(1, None, "1d")  # type: ignore
tIIS: "slice[None, int]" = slice(1, 2, "1d")  # type: ignore
# endregion Tests for slice[X, Y] assignments ------------------------------------------


# region Tests for slice[X, Y, Z] assignments ------------------------------------------
uXNX: "slice[int, int, int]" = slice(None)
uXIX: "slice[int, int, int]" = slice(1)

uNNX: "slice[int, int, int]" = slice(None, None)
uNIX: "slice[int, int, int]" = slice(None, 2)
uINX: "slice[int, int, int]" = slice(1, None)
uIIX: "slice[int, int, int]" = slice(1, 2)

uNNN: "slice[int, int, int]" = slice(None, None, None)
uNNI: "slice[int, int, int]" = slice(None, None, 3)
uNIN: "slice[int, int, int]" = slice(None, 2, None)
uNII: "slice[int, int, int]" = slice(None, 2, 3)
uINN: "slice[int, int, int]" = slice(1, None, None)
uINI: "slice[int, int, int]" = slice(1, None, 3)
uIIN: "slice[int, int, int]" = slice(1, 2, None)
uIII: "slice[int, int, int]" = slice(1, 2, 3)
# endregion Tests for slice[X, Y, Z] assignments ---------------------------------------


# region Test for slice consistency criterion ------------------------------------------
vXNX: "slice[None, None, None]" = slice(None)
vXIX: "slice[None, int, None]" = slice(1)

vNNX: "slice[None, None, None]" = slice(None, None)
vNIX: "slice[None, int, None]" = slice(None, 2)
vINX: "slice[int, None, None]" = slice(1, None)
vIIX: "slice[int, int, None]" = slice(1, 2)

vNNN: "slice[None, None, None]" = slice(None, None, None)
vNNI: "slice[None, None, int]" = slice(None, None, 3)
vNIN: "slice[None, int, None]" = slice(None, 2, None)
vNII: "slice[None, int, int]" = slice(None, 2, 3)
vINN: "slice[int, None, None]" = slice(1, None, None)
vINI: "slice[int, None, int]" = slice(1, None, 3)
vIIN: "slice[int, int, None]" = slice(1, 2, None)
vIII: "slice[int, int, int]" = slice(1, 2, 3)
# endregion Test for slice consistency criterion ---------------------------------------


# region Tests for slice properties ----------------------------------------------------
# Note: if an argument is not None, we should get precisely the same type back
assert_type(slice(1).stop, int)
assert_type(slice(None, 1).stop, int)
assert_type(slice(None, 1, None).stop, int)

assert_type(slice(1, None).start, int)
assert_type(slice(1, None, None).start, int)

assert_type(slice(None, None, 1).step, int)
# endregion Tests for slice properties -------------------------------------------------


# region Integration tests for slices with datetimes -----------------------------------
class TimeSeries:  # similar to pandas.Series with datetime index
    def __getitem__(self, key: "slice[DT | str | None, DT | str | None]") -> Any:
        """Subsample the time series at the given dates."""
        ...


class TimeSeriesInterpolator:  # similar to pandas.Series with datetime index
    def __getitem__(self, key: "slice[DT, DT, TD | None]") -> Any:
        """Subsample the time series at the given dates."""
        ...


# tests slices as an argument
start = DT(1970, 1, 1)
stop = DT(1971, 1, 10)
step = TD(days=1)
# see: https://pandas.pydata.org/docs/user_guide/timeseries.html#partial-string-indexing
# FIXME: https://github.com/python/mypy/issues/2410 (use literal slices)
series = TimeSeries()
_ = series[slice(None, "1970-01-10")]
_ = series[slice("1970-01-01", None)]
_ = series[slice("1970-01-01", "1971-01-10")]
_ = series[slice(None, stop)]
_ = series[slice(start, None)]
_ = series[slice(start, stop)]
_ = series[slice(None)]

model = TimeSeriesInterpolator()
_ = model[slice(start, stop)]
_ = model[slice(start, stop, step)]
_ = model[slice(start, stop, None)]


# test slices as a return type
def foo(flag: bool, value: DT) -> "slice[DT, None] | slice[None, DT]":
    if flag:
        return slice(value, None)  # slice[DT, DT|Any, Any] incompatible
    else:
        return slice(None, value)  # slice[DT|Any, DT, Any] incompatible


# endregion Integration tests for slices with datetimes --------------------------------
