from __future__ import annotations

from typing import Any, Union
from typing_extensions import assert_type


def check_update_method__int_key() -> None:
    d: dict[int, int] = {}
    d.update({1: 2})
    d.update([(1, 2)])
    d.update(a=3)  # type: ignore
    d.update({1: 2}, a=3)  # type: ignore
    d.update([(1, 2)], a=3)  # type: ignore
    d.update({"": 3})  # type: ignore
    d.update({1: ""})  # type: ignore
    d.update([("", 3)])  # type: ignore
    d.update([(3, "")])  # type: ignore


def check_update_method__str_key() -> None:
    d: dict[str, int] = {}
    d.update({"": 2})
    d.update([("", 2)])
    d.update(a=3)
    d.update({"": 2}, a=3)
    d.update([("", 2)], a=3)
    d.update({1: 3})  # type: ignore
    d.update({"": ""})  # type: ignore
    d.update([(1, 3)])  # type: ignore
    d.update([("", "")])  # type: ignore


def check_update_kwarg_key_type_accepts_str() -> None:
    d1: dict[str | int, int] = {}
    d1.update(a=1)

    d2: dict[object, int] = {}
    d2.update(a=1)


def check_setdefault_method() -> None:
    d: dict[int, str] = {}
    d2: dict[int, str | None] = {}
    d3: dict[int, Any] = {}

    d.setdefault(1)  # type: ignore
    assert_type(d.setdefault(1, "x"), str)
    assert_type(d2.setdefault(1), Union[str, None])
    assert_type(d2.setdefault(1, None), Union[str, None])
    assert_type(d2.setdefault(1, "x"), Union[str, None])
    assert_type(d3.setdefault(1), Union[Any, None])
    assert_type(d3.setdefault(1, "x"), Any)
