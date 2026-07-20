from typing import Any


def check_gradual_guarantee(arg: Any) -> int:
    # if Any materialized to `Callable[[], int] | None`, this function type checks
    if callable(arg):
        return arg()  # OK
    return -1
