from __future__ import annotations

from collections.abc import Awaitable, Callable, Coroutine
from inspect import iscoroutinefunction
from types import CoroutineType
from typing import Any
from typing_extensions import assert_type


def test_iscoroutinefunction(
    x: Callable[[str, int], Coroutine[str, int, bytes]],
    y: Callable[[str, int], Awaitable[bytes]],
    z: Callable[[str, int], str | Awaitable[bytes]],
    xx: object,
) -> None:
    if iscoroutinefunction(x):
        assert_type(x, Callable[[str, int], Coroutine[str, int, bytes]])

    if iscoroutinefunction(y):
        assert_type(y, Callable[[str, int], CoroutineType[Any, Any, bytes]])

    if iscoroutinefunction(z):
        assert_type(z, Callable[[str, int], CoroutineType[Any, Any, Any]])

    if iscoroutinefunction(xx):
        assert_type(xx, Callable[..., CoroutineType[Any, Any, Any]])
