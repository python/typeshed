from __future__ import annotations

from typing import Any, Callable, Iterable, List, Set, Tuple
from typing_extensions import assert_type

from decouple import Csv


def _test_post_process(_: Iterable[Any] = ()) -> int:
    return 0


assert_type(Csv()(""), List[str])
assert_type(Csv(cast=int)(""), List[int])
assert_type(Csv(cast=int, post_process=_test_post_process)(""), int)

assert_type(Csv[str, Set[str], Callable[[Iterable[str]], Set[str]]](post_process=set)(""), Set[str])
assert_type(Csv[int, Set[int], Callable[[Iterable[int]], Set[int]]](cast=int, post_process=set)(""), Set[int])
assert_type(Csv[int, Set[int], Callable[[Iterable[int]], Set[int]]](int, ",", "", set)(""), Set[int])

assert_type(Csv[str, Tuple[str, ...], Callable[[Iterable[int]], Tuple[str, ...]]](post_process=tuple)(""), Tuple[str, ...])
assert_type(
    Csv[int, Tuple[int, ...], Callable[[Iterable[int]], Tuple[int, ...]]](cast=int, post_process=tuple)(""), Tuple[int, ...]
)
assert_type(Csv[int, Tuple[int, ...], Callable[[Iterable[int]], Tuple[int, ...]]](int, ",", "", tuple)(""), Tuple[int, ...])
