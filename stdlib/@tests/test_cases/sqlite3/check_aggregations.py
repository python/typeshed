import sqlite3


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


def create_window_function() -> WindowSumInt:
    return WindowSumInt()


# A callable should work as well.
con.create_window_function("sumint", 1, create_window_function)
con.create_aggregate("sumint", 1, create_window_function)

# With num_args set to 1, the callable should not be called with more than one.


class WindowSumIntMultiArgs:
    def __init__(self) -> None:
        self.count = 0

    def step(self, arg_1: int, arg_2: int) -> None:
        self.count += arg_1 + arg_2

    def value(self) -> int:
        return self.count

    def inverse(self, arg_1: int, arg_2: int) -> None:
        self.count -= arg_1 + arg_2

    def finalize(self) -> int:
        return self.count


# This should fail because the callable is called with more than one argument.
con.create_window_function("sumint", 1, WindowSumIntMultiArgs)  # type: ignore
con.create_aggregate("sumint", 1, WindowSumIntMultiArgs)  # type: ignore

# With num_args set to -1, this should work.
con.create_window_function("sumint", 2, WindowSumIntMultiArgs)
con.create_aggregate("sumint", 2, WindowSumIntMultiArgs)
