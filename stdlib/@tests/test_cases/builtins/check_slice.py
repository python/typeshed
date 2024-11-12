"""
- The type hint `slice` should be compatible with the *all slices*:
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
"""

from datetime import datetime as DT, timedelta as TD
from typing import Any, Union
from typing_extensions import assert_type

# region Tests for slice constructor overloads -----------------------------------------
assert_type(slice(None), "slice[Any, Any, Any]")
assert_type(slice(None, None), "slice[Any, Any, Any]")
assert_type(slice(None, None, None), "slice[Any, Any, Any]")

assert_type(slice(1), "slice[Union[int, Any], int, Any]")
assert_type(slice(None, 1), "slice[Union[int, Any], int, Any]")
assert_type(slice(None, 1, None), "slice[Union[int, Any], int, Any]")

assert_type(slice(1, None), "slice[int, Union[int, Any], Any]")
assert_type(slice(1, None, None), "slice[int, Union[int, Any], Any]")

assert_type(slice(1, 1), "slice[int, int, Any]")
assert_type(slice(1, 1, None), "slice[int, int, Any]")

assert_type(slice(1, 1, 1), "slice[int, int, int]")
# endregion Tests for slice constructor overloads --------------------------------------

# region Tests for slice[T] assignments ------------------------------------------------
s0: "slice[int]" = slice(None)
s1: "slice[int]" = slice(None, None)
s2: "slice[int]" = slice(None, None, None)
s3: "slice[int]" = slice(None, None, "foo")

s4: "slice[int]" = slice(1)
s5: "slice[int]" = slice(None, 1)
s6: "slice[int]" = slice(None, 1, None)
s7: "slice[int]" = slice(1, None, "foo")

s8: "slice[int]" = slice(1, None)
s9: "slice[int]" = slice(1, None, None)
s10: "slice[int]" = slice(1, None, "foo")

s11: "slice[int]" = slice(1, 1)
s12: "slice[int]" = slice(1, 1, None)
s13: "slice[int]" = slice(1, 1, "foo")
# endregion Tests for slice[T] assignments ---------------------------------------------

# region Tests for slice[X, Y] assignments ---------------------------------------------
t0: "slice[int, int]" = slice(None)
t1: "slice[int, int]" = slice(None, None)
t2: "slice[int, int]" = slice(None, None, None)
t3: "slice[int, int]" = slice(None, None, "foo")

t4: "slice[int, int]" = slice(1)
t5: "slice[int, int]" = slice(None, 1)
t6: "slice[int, int]" = slice(None, 1, None)
t7: "slice[int, int]" = slice(1, None, "foo")

t8: "slice[int, int]" = slice(1, None)
t9: "slice[int, int]" = slice(1, None, None)
t10: "slice[int, int]" = slice(1, None, "foo")

t11: "slice[int, int]" = slice(1, 1)
t12: "slice[int, int]" = slice(1, 1, None)
t13: "slice[int, int]" = slice(1, 1, "foo")
# endregion Tests for slice[X, Y] assignments ------------------------------------------

# region Tests for slice[X, Y, Z] assignments ------------------------------------------
u0: "slice[int, int, int]" = slice(None)
u1: "slice[int, int, int]" = slice(None, None)
u2: "slice[int, int, int]" = slice(None, None, None)
u3: "slice[int, int, int]" = slice(None, None, 1)

u4: "slice[int, int, int]" = slice(1)
u5: "slice[int, int, int]" = slice(None, 1)
u6: "slice[int, int, int]" = slice(None, 1, None)
u7: "slice[int, int, int]" = slice(None, 1, 1)

u8: "slice[int, int, int]" = slice(1, None)
u9: "slice[int, int, int]" = slice(1, None, None)
u10: "slice[int, int, int]" = slice(1, None, 1)

u11: "slice[int, int, int]" = slice(1, 1)
u12: "slice[int, int, int]" = slice(1, 1, None)
u13: "slice[int, int, int]" = slice(1, 1, 1)
# endregion Tests for slice[X, Y, Z] assignments ---------------------------------------

# region Tests for slice properties ----------------------------------------------------
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
start = DT(2021, 1, 1)
stop = DT(2021, 1, 10)
step = TD(days=1)
# see: https://pandas.pydata.org/docs/user_guide/timeseries.html#partial-string-indexing
series = TimeSeries()
series[slice(None, "2022-01-10")]
series[slice("2022-01-01", None)]
series[slice("2022-01-01", "2022-01-10")]
series[slice(None, stop)]
series[slice(start, None)]
series[slice(start, stop)]
series[slice()]

model = TimeSeriesInterpolator()
model[slice(start, stop)]
model[slice(start, stop, step)]
model[slice(start, stop, None)]


# test slices as a return type
def foo(flag: bool, value: DT) -> "slice[DT, None] | slice[None, DT]":
    if flag:
        return slice(value, None)  # slice[DT, DT|Any, Any] incompatible
    else:
        return slice(None, value)  # slice[DT|Any, DT, Any] incompatible


# endregion Integration tests for slices with datetimes --------------------------------
