# pyright: reportUnnecessaryTypeIgnoreComment=true

from typing import Dict, Generic, Iterable, NoReturn, Tuple, TypeVar
from typing_extensions import assert_type

# These do follow `__init__` overloads order:
assert_type(dict(), Dict[NoReturn, NoReturn])
assert_type(dict(arg=1), Dict[str, int])

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")


class KeysAndGetItem(Generic[_KT, _VT]):
    def keys(self) -> Iterable[_KT]:
        ...

    def __getitem__(self, __k: _KT) -> _VT:
        ...


kt1: KeysAndGetItem[int, str]
assert_type(dict(kt1), Dict[int, str])
dict(kt1, arg="a")  # type: ignore

kt2: KeysAndGetItem[str, int]
assert_type(dict(kt2, arg=1), Dict[str, int])

i1: Iterable[Tuple[int, str]]
assert_type(dict(i1), Dict[int, str])
dict(i1, arg="a")  # type: ignore

i2: Iterable[Tuple[str, int]]
assert_type(dict(i2, arg=1), Dict[str, int])

i3: Iterable[str]
assert_type(dict(string.split(".") for string in i3), Dict[str, str])
