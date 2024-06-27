from __future__ import annotations

from typing import Any, Iterable, List
from typing_extensions import assert_type

from decouple import Choices, Csv, config


def _test_cast(_: str) -> int:
    return 0


def _test_post_process(_: Iterable[Any]) -> int:
    return 0


assert_type(config("NAME"), str)
assert_type(config("NAME", cast=int), int)
assert_type(config("NAME", cast=_test_cast), int)
assert_type(config("NAME", default="localhost"), str)
assert_type(config("NAME", cast=bool, default="false"), bool)
assert_type(config("NAME", cast=Csv(), default="foo,bar"), List[str])
assert_type(config("NAME", cast=Csv(int), default="1,2"), List[int])
assert_type(config("NAME", cast=Csv(int, post_process=_test_post_process), default="1,2"), int)
assert_type(config("NAME", cast=Choices([1, 2], int)), int)
assert_type(config("NAME", cast=Choices(["foo", "bar"])), str)
