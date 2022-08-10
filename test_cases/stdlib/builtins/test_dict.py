# pyright: reportUnnecessaryTypeIgnoreComment=true

from typing import Dict, Generic, Iterable, Tuple, TypeVar
from typing_extensions import assert_type

# These do follow `__init__` overloads order:
bad = dict()  # type: ignore
good: Dict[str, str] = dict()
assert_type(good, Dict[str, str])

assert_type(dict(arg=1), Dict[str, int])

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")


class KeysAndGetItem(Generic[_KT, _VT]):
    def keys(self) -> Iterable[_KT]:
        ...

    def __getitem__(self, __k: _KT) -> _VT:
        ...


kt1: KeysAndGetItem[int, str] = KeysAndGetItem()
assert_type(dict(kt1), Dict[int, str])
dict(kt1, arg="a")  # type: ignore

kt2: KeysAndGetItem[str, int] = KeysAndGetItem()
assert_type(dict(kt2, arg=1), Dict[str, int])

i1: Iterable[Tuple[int, str]] = [(1, "a"), (2, "b")]
# Hack to pass `pyright`. It was failing like:
# expected "Dict[int, str]" but received "dict[Literal[1, 2], Literal['a', 'b']]"
# See https://github.com/python/typeshed/pull/8517
# It used to be:
# assert_type(dict(i1), Dict[int, str])
d = dict(i1)
assert_type(next(iter(d.keys())), int)
assert_type(d[1], str)

dict(i1, arg="a")  # type: ignore

i2: Iterable[Tuple[str, int]] = [("a", 1), ("b", 2)]
assert_type(dict(i2, arg=1), Dict[str, int])

i3: Iterable[str] = ["a"]
assert_type(dict(string.split(".") for string in i3), Dict[str, str])
