from __future__ import annotations

import copy
import sys
from dataclasses import dataclass
from typing import Generic, TypeVar
from typing_extensions import Self, assert_type


class ReplaceableClass:
    def __init__(self, val: int) -> None:
        self.val = val

    def __replace__(self, val: int) -> Self:
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

    def __replace__(self, value: str) -> Box[str]:
        return Box(value)


if sys.version_info >= (3, 13):
    box1: Box[int] = Box(42)
    box2 = copy.replace(box1, val="spam")
    assert_type(box2, Box[str])


# Regression test for #15973: replace() must preserve a bound TypeVar whose
# __replace__ returns Self (the dataclass/namedtuple case), rather than widening
# to the bound.
@dataclass(frozen=True)
class BaseConfig:
    pg_ssl_key: str | None = None


@dataclass(frozen=True)
class SubConfig(BaseConfig):
    pg_host: str = "localhost"


_ConfigT = TypeVar("_ConfigT", bound=BaseConfig)

if sys.version_info >= (3, 13):

    def replace_config(config: _ConfigT) -> _ConfigT:
        result = copy.replace(config, pg_ssl_key="replaced")
        assert_type(result, _ConfigT)
        return result

    assert_type(copy.replace(SubConfig(), pg_host="example.com"), SubConfig)
