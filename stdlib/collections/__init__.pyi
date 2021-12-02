import sys
from _collections_abc import dict_items, dict_keys, dict_values
from _typeshed import Self
from typing import Any, Dict, Generic, NoReturn, Tuple, Type, TypeVar, overload
from typing_extensions import SupportsIndex, final

if sys.version_info >= (3, 9):
    from types import GenericAlias

if sys.version_info >= (3, 10):
    from typing import Callable, Iterable, Iterator, Mapping, MutableMapping, MutableSequence, Reversible, Sequence
else:
    from _collections_abc import *

_S = TypeVar("_S")
_T = TypeVar("_T")
_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_KT_co = TypeVar("_KT_co", covariant=True)
_VT_co = TypeVar("_VT_co", covariant=True)

# namedtuple is special-cased in the type checker; the initializer is ignored.
if sys.version_info >= (3, 7):
    def namedtuple(
        typename: str,
        field_names: str | Iterable[str],
        *,
        rename: bool = ...,
        module: str | None = ...,
        defaults: Iterable[Any] | None = ...,
    ) -> Type[Tuple[Any, ...]]: ...

else:
    def namedtuple(
        typename: str, field_names: str | Iterable[str], *, verbose: bool = ..., rename: bool = ..., module: str | None = ...
    ) -> Type[Tuple[Any, ...]]: ...

class UserDict(MutableMapping[_KT, _VT]):
    data: dict[_KT, _VT]
    def __init__(self, __dict: Mapping[_KT, _VT] | None = ..., **kwargs: _VT) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: _KT) -> _VT: ...
    def __setitem__(self, key: _KT, item: _VT) -> None: ...
    def __delitem__(self, key: _KT) -> None: ...
    def __iter__(self) -> Iterator[_KT]: ...
    def __contains__(self, key: object) -> bool: ...
    def copy(self: Self) -> Self: ...
    @classmethod
    def fromkeys(cls: Type[Self], iterable: Iterable[_KT], value: _VT | None = ...) -> Self: ...

class UserList(MutableSequence[_T]):
    data: list[_T]
    def __init__(self, initlist: Iterable[_T] | None = ...) -> None: ...
    def __lt__(self, other: list[_T] | UserList[_T]) -> bool: ...
    def __le__(self, other: list[_T] | UserList[_T]) -> bool: ...
    def __gt__(self, other: list[_T] | UserList[_T]) -> bool: ...
    def __ge__(self, other: list[_T] | UserList[_T]) -> bool: ...
    def __contains__(self, item: object) -> bool: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, i: SupportsIndex) -> _T: ...
    @overload
    def __getitem__(self: Self, i: slice) -> Self: ...
    @overload
    def __setitem__(self, i: SupportsIndex, o: _T) -> None: ...
    @overload
    def __setitem__(self, i: slice, o: Iterable[_T]) -> None: ...
    def __delitem__(self, i: SupportsIndex | slice) -> None: ...
    def __add__(self: _S, other: Iterable[_T]) -> _S: ...
    def __iadd__(self: _S, other: Iterable[_T]) -> _S: ...
    def __mul__(self: _S, n: int) -> _S: ...
    def __imul__(self: _S, n: int) -> _S: ...
    def append(self, item: _T) -> None: ...
    def insert(self, i: int, item: _T) -> None: ...
    def pop(self, i: int = ...) -> _T: ...
    def remove(self, item: _T) -> None: ...
    def clear(self) -> None: ...
    def copy(self: _S) -> _S: ...
    def count(self, item: _T) -> int: ...
    def index(self, item: _T, *args: Any) -> int: ...
    def reverse(self) -> None: ...
    def sort(self, *args: Any, **kwds: Any) -> None: ...
    def extend(self, other: Iterable[_T]) -> None: ...

_UserStringT = TypeVar("_UserStringT", bound=UserString)

class UserString(Sequence[str]):
    data: str
    def __init__(self, seq: object) -> None: ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __complex__(self) -> complex: ...
    def __getnewargs__(self) -> tuple[str]: ...
    def __lt__(self, string: str | UserString) -> bool: ...
    def __le__(self, string: str | UserString) -> bool: ...
    def __gt__(self, string: str | UserString) -> bool: ...
    def __ge__(self, string: str | UserString) -> bool: ...
    def __contains__(self, char: object) -> bool: ...
    def __len__(self) -> int: ...
    # It should return a str to implement Sequence correctly, but it doesn't.
    def __getitem__(self: _UserStringT, i: SupportsIndex | slice) -> _UserStringT: ...  # type: ignore[override]
    def __iter__(self: _UserStringT) -> Iterator[_UserStringT]: ...  # type: ignore[override]
    def __reversed__(self: _UserStringT) -> Iterator[_UserStringT]: ...  # type: ignore[override]
    def __add__(self: _UserStringT, other: object) -> _UserStringT: ...
    def __mul__(self: _UserStringT, n: int) -> _UserStringT: ...
    def __mod__(self: _UserStringT, args: Any) -> _UserStringT: ...
    def capitalize(self: _UserStringT) -> _UserStringT: ...
    def casefold(self: _UserStringT) -> _UserStringT: ...
    def center(self: _UserStringT, width: int, *args: Any) -> _UserStringT: ...
    def count(self, sub: str | UserString, start: int = ..., end: int = ...) -> int: ...
    if sys.version_info >= (3, 8):
        def encode(self: UserString, encoding: str | None = ..., errors: str | None = ...) -> bytes: ...
    else:
        def encode(self: _UserStringT, encoding: str | None = ..., errors: str | None = ...) -> _UserStringT: ...
    def endswith(self, suffix: str | Tuple[str, ...], start: int | None = ..., end: int | None = ...) -> bool: ...
    def expandtabs(self: _UserStringT, tabsize: int = ...) -> _UserStringT: ...
    def find(self, sub: str | UserString, start: int = ..., end: int = ...) -> int: ...
    def format(self, *args: Any, **kwds: Any) -> str: ...
    def format_map(self, mapping: Mapping[str, Any]) -> str: ...
    def index(self, sub: str, start: int = ..., end: int = ...) -> int: ...
    def isalpha(self) -> bool: ...
    def isalnum(self) -> bool: ...
    def isdecimal(self) -> bool: ...
    def isdigit(self) -> bool: ...
    def isidentifier(self) -> bool: ...
    def islower(self) -> bool: ...
    def isnumeric(self) -> bool: ...
    def isprintable(self) -> bool: ...
    def isspace(self) -> bool: ...
    def istitle(self) -> bool: ...
    def isupper(self) -> bool: ...
    if sys.version_info >= (3, 7):
        def isascii(self) -> bool: ...
    def join(self, seq: Iterable[str]) -> str: ...
    def ljust(self: _UserStringT, width: int, *args: Any) -> _UserStringT: ...
    def lower(self: _UserStringT) -> _UserStringT: ...
    def lstrip(self: _UserStringT, chars: str | None = ...) -> _UserStringT: ...
    @staticmethod
    @overload
    def maketrans(x: dict[int, _T] | dict[str, _T] | dict[str | int, _T]) -> dict[int, _T]: ...
    @staticmethod
    @overload
    def maketrans(x: str, y: str, z: str = ...) -> dict[int, int | None]: ...
    def partition(self, sep: str) -> tuple[str, str, str]: ...
    if sys.version_info >= (3, 9):
        def removeprefix(self: _UserStringT, __prefix: str | UserString) -> _UserStringT: ...
        def removesuffix(self: _UserStringT, __suffix: str | UserString) -> _UserStringT: ...
    def replace(self: _UserStringT, old: str | UserString, new: str | UserString, maxsplit: int = ...) -> _UserStringT: ...
    def rfind(self, sub: str | UserString, start: int = ..., end: int = ...) -> int: ...
    def rindex(self, sub: str | UserString, start: int = ..., end: int = ...) -> int: ...
    def rjust(self: _UserStringT, width: int, *args: Any) -> _UserStringT: ...
    def rpartition(self, sep: str) -> tuple[str, str, str]: ...
    def rstrip(self: _UserStringT, chars: str | None = ...) -> _UserStringT: ...
    def split(self, sep: str | None = ..., maxsplit: int = ...) -> list[str]: ...
    def rsplit(self, sep: str | None = ..., maxsplit: int = ...) -> list[str]: ...
    def splitlines(self, keepends: bool = ...) -> list[str]: ...
    def startswith(self, prefix: str | Tuple[str, ...], start: int | None = ..., end: int | None = ...) -> bool: ...
    def strip(self: _UserStringT, chars: str | None = ...) -> _UserStringT: ...
    def swapcase(self: _UserStringT) -> _UserStringT: ...
    def title(self: _UserStringT) -> _UserStringT: ...
    def translate(self: _UserStringT, *args: Any) -> _UserStringT: ...
    def upper(self: _UserStringT) -> _UserStringT: ...
    def zfill(self: _UserStringT, width: int) -> _UserStringT: ...

class deque(MutableSequence[_T], Generic[_T]):
    @property
    def maxlen(self) -> int | None: ...
    def __init__(self, iterable: Iterable[_T] = ..., maxlen: int | None = ...) -> None: ...
    def append(self, __x: _T) -> None: ...
    def appendleft(self, __x: _T) -> None: ...
    def clear(self) -> None: ...
    def copy(self: _S) -> _S: ...
    def count(self, __x: _T) -> int: ...
    def extend(self, __iterable: Iterable[_T]) -> None: ...
    def extendleft(self, __iterable: Iterable[_T]) -> None: ...
    def insert(self, __i: int, __x: _T) -> None: ...
    def index(self, __x: _T, __start: int = ..., __stop: int = ...) -> int: ...
    def pop(self) -> _T: ...  # type: ignore[override]
    def popleft(self) -> _T: ...
    def remove(self, __value: _T) -> None: ...
    def reverse(self) -> None: ...
    def rotate(self, __n: int = ...) -> None: ...
    def __copy__(self: _S) -> _S: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __str__(self) -> str: ...
    # These methods of deque don't really take slices, but we need to
    # define them as taking a slice to satisfy MutableSequence.
    @overload
    def __getitem__(self, __index: SupportsIndex) -> _T: ...
    @overload
    def __getitem__(self, __s: slice) -> MutableSequence[_T]: ...
    @overload
    def __setitem__(self, __i: SupportsIndex, __x: _T) -> None: ...
    @overload
    def __setitem__(self, __s: slice, __o: Iterable[_T]) -> None: ...
    @overload
    def __delitem__(self, __i: SupportsIndex) -> None: ...
    @overload
    def __delitem__(self, __s: slice) -> None: ...
    def __contains__(self, __o: object) -> bool: ...
    def __reduce__(self: Self) -> tuple[Type[Self], tuple[()], None, Iterator[_T]]: ...
    def __reversed__(self) -> Iterator[_T]: ...
    def __iadd__(self: _S, __iterable: Iterable[_T]) -> _S: ...
    def __add__(self: _S, __other: _S) -> _S: ...
    def __mul__(self: _S, __other: int) -> _S: ...
    def __imul__(self: _S, __other: int) -> _S: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, __item: Any) -> GenericAlias: ...

class Counter(Dict[_T, int], Generic[_T]):
    @overload
    def __init__(self, __iterable: None = ..., **kwargs: int) -> None: ...
    @overload
    def __init__(self, __mapping: Mapping[_T, int]) -> None: ...
    @overload
    def __init__(self, __iterable: Iterable[_T]) -> None: ...
    def copy(self: Self) -> Self: ...
    def elements(self) -> Iterator[_T]: ...
    def most_common(self, n: int | None = ...) -> list[tuple[_T, int]]: ...
    @classmethod
    def fromkeys(cls, iterable: Any, v: int | None = ...) -> NoReturn: ...  # type: ignore[override]
    @overload
    def subtract(self, __iterable: None = ...) -> None: ...
    @overload
    def subtract(self, __mapping: Mapping[_T, int]) -> None: ...
    @overload
    def subtract(self, __iterable: Iterable[_T]) -> None: ...
    # The Iterable[Tuple[...]] argument type is not actually desirable
    # (the tuples will be added as keys, breaking type safety) but
    # it's included so that the signature is compatible with
    # Dict.update. Not sure if we should use '# type: ignore' instead
    # and omit the type from the union.
    @overload
    def update(self, __m: Mapping[_T, int], **kwargs: int) -> None: ...
    @overload
    def update(self, __m: Iterable[_T] | Iterable[tuple[_T, int]], **kwargs: int) -> None: ...
    @overload
    def update(self, __m: None = ..., **kwargs: int) -> None: ...
    def __add__(self, other: Counter[_T]) -> Counter[_T]: ...
    def __sub__(self, other: Counter[_T]) -> Counter[_T]: ...
    def __and__(self, other: Counter[_T]) -> Counter[_T]: ...
    def __or__(self, other: Counter[_T]) -> Counter[_T]: ...  # type: ignore[override]
    def __pos__(self) -> Counter[_T]: ...
    def __neg__(self) -> Counter[_T]: ...
    def __iadd__(self, other: Counter[_T]) -> Counter[_T]: ...
    def __isub__(self, other: Counter[_T]) -> Counter[_T]: ...
    def __iand__(self, other: Counter[_T]) -> Counter[_T]: ...
    def __ior__(self, other: Counter[_T]) -> Counter[_T]: ...  # type: ignore[override]
    if sys.version_info >= (3, 10):
        def total(self) -> int: ...

@final
class _OrderedDictKeysView(dict_keys[_KT_co, _VT_co], Reversible[_KT_co]):  # type: ignore[misc]
    def __reversed__(self) -> Iterator[_KT_co]: ...

@final
class _OrderedDictItemsView(dict_items[_KT_co, _VT_co], Reversible[Tuple[_KT_co, _VT_co]]):  # type: ignore[misc]
    def __reversed__(self) -> Iterator[tuple[_KT_co, _VT_co]]: ...

@final
class _OrderedDictValuesView(dict_values[_KT_co, _VT_co], Reversible[_VT_co], Generic[_KT_co, _VT_co]):  # type: ignore[misc]
    def __reversed__(self) -> Iterator[_VT_co]: ...

class OrderedDict(Dict[_KT, _VT], Reversible[_KT], Generic[_KT, _VT]):
    def popitem(self, last: bool = ...) -> tuple[_KT, _VT]: ...
    def move_to_end(self, key: _KT, last: bool = ...) -> None: ...
    def copy(self: Self) -> Self: ...
    def __reversed__(self) -> Iterator[_KT]: ...
    def keys(self) -> _OrderedDictKeysView[_KT, _VT]: ...
    def items(self) -> _OrderedDictItemsView[_KT, _VT]: ...
    def values(self) -> _OrderedDictValuesView[_KT, _VT]: ...

class defaultdict(Dict[_KT, _VT], Generic[_KT, _VT]):
    default_factory: Callable[[], _VT] | None
    @overload
    def __init__(self, **kwargs: _VT) -> None: ...
    @overload
    def __init__(self, __default_factory: Callable[[], _VT] | None) -> None: ...
    @overload
    def __init__(self, __default_factory: Callable[[], _VT] | None, **kwargs: _VT) -> None: ...
    @overload
    def __init__(self, __default_factory: Callable[[], _VT] | None, __map: Mapping[_KT, _VT]) -> None: ...
    @overload
    def __init__(self, __default_factory: Callable[[], _VT] | None, __map: Mapping[_KT, _VT], **kwargs: _VT) -> None: ...
    @overload
    def __init__(self, __default_factory: Callable[[], _VT] | None, __iterable: Iterable[tuple[_KT, _VT]]) -> None: ...
    @overload
    def __init__(
        self, __default_factory: Callable[[], _VT] | None, __iterable: Iterable[tuple[_KT, _VT]], **kwargs: _VT
    ) -> None: ...
    def __missing__(self, __key: _KT) -> _VT: ...
    def __copy__(self: _S) -> _S: ...
    def copy(self: _S) -> _S: ...

class ChainMap(MutableMapping[_KT, _VT], Generic[_KT, _VT]):
    maps: list[MutableMapping[_KT, _VT]]
    def __init__(self, *maps: MutableMapping[_KT, _VT]) -> None: ...
    def new_child(self: Self, m: MutableMapping[_KT, _VT] | None = ...) -> Self: ...
    @property
    def parents(self: Self) -> Self: ...
    def __setitem__(self, k: _KT, v: _VT) -> None: ...
    def __delitem__(self, v: _KT) -> None: ...
    def __getitem__(self, k: _KT) -> _VT: ...
    def __iter__(self) -> Iterator[_KT]: ...
    def __len__(self) -> int: ...
    def __missing__(self, key: _KT) -> _VT: ...  # undocumented
    def setdefault(self, key: _KT, default: _VT = ...) -> _VT: ...
    @overload
    def pop(self, key: _KT) -> _VT: ...
    @overload
    def pop(self, key: _KT, default: _VT | _T = ...) -> _VT | _T: ...
    def copy(self: Self) -> Self: ...
    @classmethod
    @overload
    def fromkeys(cls, iterable: Iterable[_T], __value: None = ...) -> ChainMap[_T, Any | None]: ...
    @classmethod
    @overload
    def fromkeys(cls, __iterable: Iterable[_T], __value: _S) -> ChainMap[_T, _S]: ...
