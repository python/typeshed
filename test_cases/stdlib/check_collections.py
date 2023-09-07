from __future__ import annotations

import os
from collections import defaultdict
from typing import DefaultDict, Dict, Mapping, TypeVar
from typing_extensions import assert_type

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")


class CustomDefaultDictSubclass(DefaultDict[_KT, _VT]):
    pass


def test_defaultdict_dot_or(
    a: defaultdict[int, int], b: CustomDefaultDictSubclass[int, int], c: defaultdict[str, str], d: Mapping[int, int]
) -> None:
    # In contrast to `dict.__or__`, `defaultdict.__or__` returns `Self` if called on a subclass of `defaultdict`:
    assert_type(b | a, CustomDefaultDictSubclass[int, int])

    assert_type(a | c, DefaultDict[int | str, int | str])

    # arbitrary mappings are not accepted by `defaultdict.__or__`;
    # it has to be a subclass of `dict`
    a | d  # type: ignore

    # but Mappings such as `os._Environ`,
    # which define `__ror__` methods that accept `dict`, are fine
    # (`os._Environ.__(r)or__` always returns `dict`, even if a `defaultdict` is passed):
    assert_type(a | os.environ, Dict[str | int, str | int])
    assert_type(os.environ | a, Dict[str | int, str | int])
    assert_type(c | os.environ, Dict[str, str])
    assert_type(os.environ | c, Dict[str, str])

    os.environ |= c
    os.environ |= a  # type: ignore
    c |= os.environ
    c |= a  # type: ignore
