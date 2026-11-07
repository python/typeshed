from __future__ import annotations

import copy
import sys
from typing import Generic, TypeVar
from typing_extensions import Self, assert_type


class ReplaceableClass:
    def __init__(self, val: int) -> None:
        self.val = val

    def __replace__(self, /, *, val: int) -> Self:
        cpy = copy.copy(self)
        cpy.val = val
        return cpy


if sys.version_info >= (3, 13):
    obj = ReplaceableClass(42)
    cpy = copy.replace(obj, val=23)
    assert_type(cpy, ReplaceableClass)


_T_co = TypeVar("_T_co", covariant=True)


class Box(Generic[_T_co]):
    def __init__(self, value: _T_co, /) -> None:
        self.value = value

    def __replace__(self, /, *, value: str) -> Box[str]:
        return Box(value)


if sys.version_info >= (3, 13):
    box1: Box[int] = Box(42)
    box2 = copy.replace(box1, value="spam")
    assert_type(box2, Box[str])


if sys.version_info >= (3, 13):
    # Regression for #16582: a union whose members each have a field the
    # others lack must not be rejected.
    from dataclasses import dataclass

    @dataclass(frozen=True)
    class Circle:
        name: str
        radius: float

    @dataclass(frozen=True)
    class Square:
        name: str
        side: float

    def rename(shape: Circle | Square) -> Circle | Square:
        return copy.replace(shape, name="renamed")

    def wrong(shape: Circle | Square) -> Circle | Square:
        return copy.replace(shape, name=1)  # E: invalid-argument-type
