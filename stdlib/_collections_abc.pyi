import sys
from types import MappingProxyType
from typing import (
    AbstractSet as Set,
    AsyncGenerator as AsyncGenerator,
    AsyncIterable as AsyncIterable,
    AsyncIterator as AsyncIterator,
    Awaitable as Awaitable,
    ByteString as ByteString,
    Callable as Callable,
    Collection as Collection,
    Container as Container,
    Coroutine as Coroutine,
    Generator as Generator,
    Generic,
    Hashable as Hashable,
    ItemsView as _ItemsView,
    Iterable as Iterable,
    Iterator as Iterator,
    KeysView as _KeysView,
    Mapping as Mapping,
    MappingView as _MappingView,
    MutableMapping as MutableMapping,
    MutableSequence as MutableSequence,
    MutableSet as MutableSet,
    Reversible as Reversible,
    Sequence as Sequence,
    Sized as Sized,
    TypeVar,
    ValuesView as _ValuesView,
    Any,
)
from typing_extensions import final

__all__ = [
    "Awaitable",
    "Coroutine",
    "AsyncIterable",
    "AsyncIterator",
    "AsyncGenerator",
    "Hashable",
    "Iterable",
    "Iterator",
    "Generator",
    "Reversible",
    "Sized",
    "Container",
    "Callable",
    "Collection",
    "Set",
    "MutableSet",
    "Mapping",
    "MutableMapping",
    "MappingView",
    "KeysView",
    "ItemsView",
    "ValuesView",
    "Sequence",
    "MutableSequence",
    "ByteString",
]

_KT_co = TypeVar("_KT_co", covariant=True)  # Key type covariant containers.
_VT_co = TypeVar("_VT_co", covariant=True)  # Value type covariant containers.

@final
class dict_keys(_KeysView[_KT_co], Generic[_KT_co, _VT_co]):  # undocumented
    if sys.version_info >= (3, 10):
        @property
        def mapping(self) -> MappingProxyType[_KT_co, _VT_co]: ...

@final
class dict_values(_ValuesView[_VT_co], Generic[_KT_co, _VT_co]):  # undocumented
    if sys.version_info >= (3, 10):
        @property
        def mapping(self) -> MappingProxyType[_KT_co, _VT_co]: ...

@final
class dict_items(_ItemsView[_KT_co, _VT_co], Generic[_KT_co, _VT_co]):  # undocumented
    if sys.version_info >= (3, 10):
        @property
        def mapping(self) -> MappingProxyType[_KT_co, _VT_co]: ...

class MappingView(_MappingView):
    _mapping: Mapping[Any, Any]  # undocumented

class KeysView(_KeysView[_KT_co], Generic[_KT_co]):
    _mapping: Mapping[_KT_co, Any]  # undocumented

class ValuesView(_ValuesView[_VT_co], Generic[_VT_co]):
    _mapping: Mapping[Any, _VT_co]  # undocumented

class ItemsView(_ItemsView[_KT_co, _VT_co], Generic[_KT_co, _VT_co]):
    _mapping: Mapping[_KT_co, _VT_co]  # undocumented
