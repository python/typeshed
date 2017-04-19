# Stubs for collections

# Based on http://docs.python.org/3.2/library/collections.html

# TODO more abstract base classes (interfaces in mypy)

# These are not exported.
import sys
import typing
from typing import (
    TypeVar, Generic, Dict, overload, List, Tuple,
    Callable, Any, Type, Optional, Union
)
# These are exported.
# TODO reexport more.
from typing import (
    Container as Container,
    Hashable as Hashable,
    Iterable as Iterable,
    Iterator as Iterator,
    Sized as Sized,
    Generator as Generator,
    ByteString as ByteString,
    Awaitable as Awaitable,
    Coroutine as Coroutine,
    AsyncIterable as AsyncIterable,
    AsyncIterator as AsyncIterator,
    Reversible as Reversible,
    Mapping as Mapping,
    MappingView as MappingView,
    ItemsView as ItemsView,
    KeysView as KeysView,
    ValuesView as ValuesView,
    MutableMapping as MutableMapping,
    Sequence as Sequence,
    MutableSequence as MutableSequence,
    MutableSet as MutableSet,
    AbstractSet as Set,
)
if sys.version_info >= (3, 6):
    from typing import (
        Collection as Collection,
        AsyncGenerator as AsyncGenerator,
    )

_T = TypeVar('_T')
_KT = TypeVar('_KT')
_VT = TypeVar('_VT')


# namedtuple is special-cased in the type checker; the initializer is ignored.
def namedtuple(typename: str, field_names: Union[str, Iterable[Any]], *,
               verbose: bool = ..., rename: bool = ..., module: str = None) -> Type[tuple]: ...

class UserDict(MutableMapping): ...
class UserList(MutableSequence): ...
class UserString(Sequence): ...
class MutableString(UserString, MutableSequence): ...

# Technically, deque only derives from MutableSequence in 3.5.
# But in practice it's not worth losing sleep over.
class deque(MutableSequence[_T], Generic[_T]):
    maxlen = ...  # type: Optional[int] # TODO readonly
    def __init__(self, iterable: Iterable[_T] = ...,
                 maxlen: int = ...) -> None: ...
    def append(self, x: _T) -> None: ...
    def appendleft(self, x: _T) -> None: ...
    def insert(self, i: int, x: _T) -> None: ...
    def clear(self) -> None: ...
    def count(self, x: _T) -> int: ...
    def extend(self, iterable: Iterable[_T]) -> None: ...
    def extendleft(self, iterable: Iterable[_T]) -> None: ...
    def pop(self, i: int = ...) -> _T: ...
    def popleft(self) -> _T: ...
    def remove(self, value: _T) -> None: ...
    def reverse(self) -> None: ...
    def rotate(self, n: int) -> None: ...

    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __str__(self) -> str: ...
    def __hash__(self) -> int: ...

    # These methods of deque don't really take slices, but we need to
    # define them as taking a slice to satisfy MutableSequence.
    @overload
    def __getitem__(self, index: int) -> _T: ...
    @overload
    def __getitem__(self, s: slice) -> Sequence[_T]: raise TypeError
    @overload
    def __setitem__(self, i: int, x: _T) -> None: ...
    @overload
    def __setitem__(self, s: slice, o: Iterable[_T]) -> None: raise TypeError
    @overload
    def __delitem__(self, i: int) -> None: ...
    @overload
    def __delitem__(self, s: slice) -> None: raise TypeError

    def __contains__(self, o: object) -> bool: ...

    # TODO __reversed__


class Counter(Dict[_T, int], Generic[_T]):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Mapping: Mapping[_T, int]) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[_T]) -> None: ...
    # TODO keyword arguments

    def elements(self) -> Iterator[_T]: ...

    @overload
    def most_common(self) -> List[_T]: ...
    @overload
    def most_common(self, n: int) -> List[_T]: ...

    @overload
    def subtract(self, Mapping: Mapping[_T, int]) -> None: ...
    @overload
    def subtract(self, iterable: Iterable[_T]) -> None: ...

    # The Iterable[Tuple[...]] argument type is not actually desirable
    # (the tuples will be added as keys, breaking type safety) but
    # it's included so that the signature is compatible with
    # Dict.update. Not sure if we should use '# type: ignore' instead
    # and omit the type from the union.
    @overload
    def update(self, m: Mapping[_T, int], **kwargs: int) -> None: ...
    @overload
    def update(self, m: Union[Iterable[_T], Iterable[Tuple[_T, int]]], **kwargs: int) -> None: ...

    def __add__(self, other: typing.Counter[_T]) -> typing.Counter[_T]: ...
    def __sub__(self, other: typing.Counter[_T]) -> typing.Counter[_T]: ...
    def __and__(self, other: typing.Counter[_T]) -> typing.Counter[_T]: ...
    def __or__(self, other: typing.Counter[_T]) -> typing.Counter[_T]: ...
    def __pos__(self) -> typing.Counter[_T]: ...
    def __neg__(self) -> typing.Counter[_T]: ...
    def __iadd__(self, other: typing.Counter[_T]) -> typing.Counter[_T]: ...
    def __isub__(self, other: typing.Counter[_T]) -> typing.Counter[_T]: ...
    def __iand__(self, other: typing.Counter[_T]) -> typing.Counter[_T]: ...
    def __ior__(self, other: typing.Counter[_T]) -> typing.Counter[_T]: ...

class OrderedDict(Dict[_KT, _VT], Reversible[_KT], Generic[_KT, _VT]):
    def popitem(self, last: bool = ...) -> Tuple[_KT, _VT]: ...
    def move_to_end(self, key: _KT, last: bool = ...) -> None: ...
    def __reversed__(self) -> Iterator[_KT]: ...

class defaultdict(Dict[_KT, _VT], Generic[_KT, _VT]):
    default_factory = ...  # type: Callable[[], _VT]

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, map: Mapping[_KT, _VT]) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[Tuple[_KT, _VT]]) -> None: ...
    @overload
    def __init__(self, default_factory: Callable[[], _VT]) -> None: ...
    @overload
    def __init__(self, default_factory: Callable[[], _VT],
                 map: Mapping[_KT, _VT]) -> None: ...
    @overload
    def __init__(self, default_factory: Callable[[], _VT],
                 iterable: Iterable[Tuple[_KT, _VT]]) -> None: ...
    # TODO __init__ keyword args

    def __missing__(self, key: _KT) -> _VT: ...
    # TODO __reversed__

if sys.version_info >= (3, 3):
    class ChainMap(MutableMapping[_KT, _VT], Generic[_KT, _VT]):
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, *maps: Mapping[_KT, _VT]) -> None: ...

        @property
        def maps(self) -> List[Mapping[_KT, _VT]]: ...

        def new_child(self, m: Mapping[_KT, _VT] = ...) -> typing.ChainMap[_KT, _VT]: ...

        @property
        def parents(self) -> typing.ChainMap[_KT, _VT]: ...

        def __setitem__(self, k: _KT, v: _VT) -> None: ...
        def __delitem__(self, v: _KT) -> None: ...
        def __getitem__(self, k: _KT) -> _VT: ...
        def __iter__(self) -> Iterator[_KT]: ...
        def __len__(self) -> int: ...
