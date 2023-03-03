from __future__ import annotations

import sys
from functools import wraps
from typing import Callable, TypeVar
from typing_extensions import ParamSpec, assert_type

P = ParamSpec("P")
T_co = TypeVar("T_co", covariant=True)


def my_decorator(func: Callable[P, T_co]) -> Callable[P, T_co]:
    func_name = func.__name__

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs):
        print(args)
        return func(*args, **kwargs)

    wrapper.__name__ = func_name
    return wrapper


if sys.version_info >= (3, 8):
    from functools import cached_property

    class A:
        def __init__(self, x: int):
            self.x = x

        @cached_property
        def x(self) -> int:
            return 0

    assert_type(A(x=1).x, int)

    class B:
        @cached_property
        def x(self) -> int:
            return 0

    def check_cached_property_settable(x: int) -> None:
        b = B()
        assert_type(b.x, int)
        b.x = x
        assert_type(b.x, int)
