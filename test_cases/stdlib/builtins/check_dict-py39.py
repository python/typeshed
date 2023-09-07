"""
Tests for `dict.__(r)or__`.

`dict.__or__` and `dict.__ror__` were only added in py39,
hence why these are in a separate file to the other test cases for `dict`.
"""
from __future__ import annotations

import os
import sys
from typing import Mapping, TypeVar, Union
from typing_extensions import assert_type

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

if sys.version_info >= (3, 9):

    class CustomDictSubclass(dict[_KT, _VT]):
        pass

    def test_dict_dot_or(a: dict[int, int], b: CustomDictSubclass[int, int], c: dict[str, str], d: Mapping[int, int]) -> None:
        # dict.__(r)or__ always returns a dict, even if called on a subclass of dict:
        assert_type(a | b, dict[int, int])
        assert_type(b | a, dict[int, int])

        assert_type(a | c, dict[Union[int, str], Union[int, str]])

        # arbitrary mappings are not accepted by `dict.__or__`;
        # it has to be a subclass of `dict`
        a | d  # type: ignore

        # but Mappings such as `os._Environ`,
        # which define `__ror__` methods that accept `dict`, are fine:
        assert_type(a | os.environ, dict[Union[str, int], Union[str, int]])
        assert_type(os.environ | a, dict[Union[str, int], Union[str, int]])
        assert_type(c | os.environ, dict[str, str])
        assert_type(os.environ | c, dict[str, str])

        os.environ |= c
        os.environ |= a  # type: ignore
        c |= os.environ
        c |= a  # type: ignore
