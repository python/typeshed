import sqlite3
import sys


class WindowSumInt:
    def __init__(self) -> None:
        self.count = 0

    def step(self, param: int) -> None:
        self.count += param

    def value(self) -> int:
        return self.count

    def inverse(self, param: int) -> None:
        self.count -= param

    def finalize(self) -> int:
        return self.count


con = sqlite3.connect(":memory:")
cur = con.execute("CREATE TABLE test(x, y)")
values = [("a", 4), ("b", 5), ("c", 3), ("d", 8), ("e", 1)]
cur.executemany("INSERT INTO test VALUES(?, ?)", values)

if sys.version_info >= (3, 11):
    con.create_window_function("sumint", 1, WindowSumInt)

con.create_aggregate("sumint", 1, WindowSumInt)
cur.execute(
    """
    SELECT x, sumint(y) OVER (
        ORDER BY x ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) AS sum_y
    FROM test ORDER BY x
"""
)
con.close()


def _create_window_function() -> WindowSumInt:
    return WindowSumInt()


# A callable should work as well.
if sys.version_info >= (3, 11):
    con.create_window_function("sumint", 1, _create_window_function)
    con.create_aggregate("sumint", 1, _create_window_function)

# With num_args set to 1, the callable should not be called with more than one.


class WindowSumIntMultiArgs:
    def __init__(self) -> None:
        self.count = 0

    def step(self, *args: int) -> None:
        self.count += sum(args)

    def value(self) -> int:
        return self.count

    def inverse(self, *args: int) -> None:
        self.count -= sum(args)

    def finalize(self) -> int:
        return self.count


if sys.version_info >= (3, 11):
    con.create_window_function("sumint", 1, WindowSumIntMultiArgs)
    con.create_window_function("sumint", 2, WindowSumIntMultiArgs)

con.create_aggregate("sumint", 1, WindowSumIntMultiArgs)
con.create_aggregate("sumint", 2, WindowSumIntMultiArgs)

# n_arg=-1 requires *args to handle any number of arguments
if sys.version_info >= (3, 11):
    con.create_window_function("sumint_varargs", -1, WindowSumIntMultiArgs)

con.create_aggregate("sumint_varargs", -1, WindowSumIntMultiArgs)


# n_arg=-1 should reject fixed-arity methods
class FixedArityAggregate:
    def __init__(self) -> None:
        self.total = 0

    def step(self, a: int, b: int) -> None:
        self.total += a + b

    def finalize(self) -> int:
        return self.total


con.create_aggregate("bad_varargs", -1, FixedArityAggregate)  # type: ignore[arg-type]


class FixedArityWindowAggregate:
    def __init__(self) -> None:
        self.total = 0

    def step(self, a: int, b: int) -> None:
        self.total += a + b

    def inverse(self, a: int, b: int) -> None:
        self.total -= a + b

    def value(self) -> int:
        return self.total

    def finalize(self) -> int:
        return self.total


if sys.version_info >= (3, 11):
    con.create_window_function("bad_varargs", -1, FixedArityWindowAggregate)  # type: ignore[arg-type]


# Test case: Fixed parameter aggregates (the common case in practice)
class FixedTwoParamAggregate:
    def __init__(self) -> None:
        self.total = 0

    def step(self, a: int, b: int) -> None:
        self.total += a + b

    def finalize(self) -> int:
        return self.total


con.create_aggregate("sum2", 2, FixedTwoParamAggregate)


class FixedThreeParamWindowAggregate:
    def __init__(self) -> None:
        self.total = 0

    def step(self, a: int, b: int, c: int) -> None:
        self.total += a + b + c

    def inverse(self, a: int, b: int, c: int) -> None:
        self.total -= a + b + c

    def value(self) -> int:
        return self.total

    def finalize(self) -> int:
        return self.total


if sys.version_info >= (3, 11):
    con.create_window_function("sum3", 3, FixedThreeParamWindowAggregate)


# What do protocols still catch?


# Missing required method
class MissingStep:
    def __init__(self) -> None:
        self.total = 0

    def finalize(self) -> int:
        return self.total


con.create_aggregate("bad", 2, MissingStep)  # type: ignore[arg-type]  # missing step method


# Invalid return type from finalize (not a valid SQLite type)
class BadFinalizeReturn:
    def __init__(self) -> None:
        self.items: list[int] = []

    def step(self, x: int) -> None:
        self.items.append(x)

    def finalize(self) -> list[int]:  # list is not a valid SQLite type
        return self.items


con.create_aggregate("bad2", 1, BadFinalizeReturn)  # type: ignore[arg-type]  # bad return type
