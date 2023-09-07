from __future__ import annotations

import os
from typing import Dict, Generic, Iterable, Mapping, TypeVar
from typing_extensions import assert_type

# These do follow `__init__` overloads order:
# mypy and pyright have different opinions about this one:
# mypy raises: 'Need type annotation for "bad"'
# pyright is fine with it.
# bad = dict()
good: dict[str, str] = dict()
assert_type(good, Dict[str, str])

assert_type(dict(arg=1), Dict[str, int])

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")


class KeysAndGetItem(Generic[_KT, _VT]):
    data: dict[_KT, _VT]

    def __init__(self, data: dict[_KT, _VT]) -> None:
        self.data = data

    def keys(self) -> Iterable[_KT]:
        return self.data.keys()

    def __getitem__(self, __k: _KT) -> _VT:
        return self.data[__k]


kt1: KeysAndGetItem[int, str] = KeysAndGetItem({0: ""})
assert_type(dict(kt1), Dict[int, str])
dict(kt1, arg="a")  # type: ignore

kt2: KeysAndGetItem[str, int] = KeysAndGetItem({"": 0})
assert_type(dict(kt2, arg=1), Dict[str, int])


def test_iterable_tuple_overload(x: Iterable[tuple[int, str]]) -> dict[int, str]:
    return dict(x)


i1: Iterable[tuple[int, str]] = [(1, "a"), (2, "b")]
test_iterable_tuple_overload(i1)
dict(i1, arg="a")  # type: ignore

i2: Iterable[tuple[str, int]] = [("a", 1), ("b", 2)]
assert_type(dict(i2, arg=1), Dict[str, int])

i3: Iterable[str] = ["a.b"]
i4: Iterable[bytes] = [b"a.b"]
assert_type(dict(string.split(".") for string in i3), Dict[str, str])
assert_type(dict(string.split(b".") for string in i4), Dict[bytes, bytes])

dict(["foo", "bar", "baz"])  # type: ignore
dict([b"foo", b"bar", b"baz"])  # type: ignore


############################
# Tests for `dict.__(r)or__`
###########################


class CustomDictSubclass(Dict[_KT, _VT]):
    pass


def test_dict_dot_or(a: dict[int, int], b: CustomDictSubclass[int, int], c: dict[str, str], d: Mapping[int, int]) -> None:
    # dict.__(r)or__ always returns a dict, even if called on a subclass of dict:
    assert_type(a | b, Dict[int, int])
    assert_type(b | a, Dict[int, int])

    assert_type(a | c, Dict[int | str, int | str])

    # arbitrary mappings are not accepted by `dict.__or__`;
    # it has to be a subclass of `dict`
    a | d  # type: ignore

    # but Mappings such as `os._Environ`,
    # which define `__ror__` methods that accept `dict`, are fine:
    assert_type(a | os.environ, Dict[str | int, str | int])
    assert_type(os.environ | a, Dict[str | int, str | int])
    assert_type(c | os.environ, Dict[str, str])
    assert_type(os.environ | c, Dict[str, str])

    os.environ |= c
    os.environ |= a  # type: ignore
    c |= os.environ
    c |= a  # type: ignore
