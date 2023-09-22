from __future__ import annotations

from typing import Any, Iterable, List
from typing_extensions import assert_type

from decouple import Choices, Csv, config


def _test_cast(_: str) -> int:
    return 0


def _test_post_process(_: Iterable[Any]) -> int:
    return 0


assert_type(config(""), str)
assert_type(config("", cast=int), int)
assert_type(config("", cast=_test_cast), int)
assert_type(config("", default="localhost"), str)
assert_type(config("", cast=bool, default="false"), bool)
assert_type(config("", cast=Csv(), default="foo,bar"), List[str])
assert_type(config("", cast=Csv(int), default="1,2"), List[int])
assert_type(config("", cast=Csv(int, post_process=_test_post_process), default="1,2"), int)
assert_type(config("", cast=Choices([1, 2], int)), int)
assert_type(config("", cast=Choices(["foo", "bar"])), str)
