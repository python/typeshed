from typing import Any
from typing_extensions import assert_type


def lists(li: list[int], ls: list[str]) -> None:
    assert_type(zip(li), zip[tuple[int]])
    assert_type(zip(li, li), zip[tuple[int, int]])
    assert_type(zip(ls, li), zip[tuple[str, int]])
    assert_type(zip(li, ls), zip[tuple[int, str]])
    assert_type(zip(ls, li, li), zip[tuple[str, int, int]])

    assert_type(zip(ls, li, li, li, li, li, li, li, li, ls, li, ls), zip[tuple[object, ...]])


def lists_any(la: list[Any], li: list[int]) -> None:
    assert_type(zip(la), zip[tuple[Any]])
    assert_type(zip(la, li), zip[tuple[Any, int]])
    assert_type(zip(li, la), zip[tuple[int, Any]])

    assert_type(zip(la, li, li, li, li, li, li, li, li, la, li, la), zip[tuple[Any, ...]])


def star_lists(ltii: list[tuple[int, int]], ltis: list[tuple[int, str]]) -> None:
    assert_type(zip(*ltii), zip[tuple[int, ...]])
    assert_type(zip(*ltis), zip[tuple[object, ...]])
