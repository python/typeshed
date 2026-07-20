from typing import Any


def check_gradual_guarantee(arg: Any) -> int:
    # if Any materialized to `Callable[[], int] | None`, this function type checks
    if callable(arg):
        return arg()  # type: ignore[no-any-return]  # pyright: ignore[reportUnnecessaryTypeIgnoreComment]
    return -1
