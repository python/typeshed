"""
Tests for `defaultdict.__or__` and `defaultdict.__ror__`.
These methods were only added in py39.
"""

from __future__ import annotations

import os
import sys
from collections import defaultdict
from typing import Mapping, TypeVar, Union
from typing_extensions import assert_type

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")


if sys.version_info >= (3, 9):
    class CustomDefaultDictSubclass(defaultdict[_KT, _VT]):
        pass


    def test_defaultdict_dot_or(
        a: defaultdict[int, int], b: CustomDefaultDictSubclass[int, int], c: defaultdict[str, str], d: Mapping[int, int]
    ) -> None:
        # In contrast to `dict.__or__`, `defaultdict.__or__` returns `Self` if called on a subclass of `defaultdict`:
        assert_type(b | a, CustomDefaultDictSubclass[int, int])

        assert_type(a | c, defaultdict[Union[int, str], Union[int, str]])

        # arbitrary mappings are not accepted by `defaultdict.__or__`;
        # it has to be a subclass of `dict`
        a | d  # type: ignore

        # but Mappings such as `os._Environ`,
        # which define `__ror__` methods that accept `dict`, are fine
        # (`os._Environ.__(r)or__` always returns `dict`, even if a `defaultdict` is passed):
        assert_type(a | os.environ, dict[Union[str, int], Union[str, int]])
        assert_type(os.environ | a, dict[Union[str, int], Union[str, int]])
        assert_type(c | os.environ, dict[str, str])
        assert_type(os.environ | c, dict[str, str])

        os.environ |= c
        os.environ |= a  # type: ignore
        c |= os.environ
        c |= a  # type: ignore
