from __future__ import annotations

from collections.abc import Callable
from typing_extensions import assert_type

assert_type(Callable[[], None], type[Callable[[], None]])


def f(c: Callable[[], None]) -> None:
    assert_type(c.__call__, Callable[[], None])


class C(Callable[[], None]):
    def __call__(self) -> None: ...


isinstance(C(), Callable)
