import sys
from types import FunctionType as FunctionType, MappingProxyType as mappingproxy  # undocumented
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
    ItemsView as ItemsView,
    Iterable as Iterable,
    Iterator as Iterator,
    KeysView as KeysView,
    Mapping as Mapping,
    MappingView as MappingView,
    MutableMapping as MutableMapping,
    MutableSequence as MutableSequence,
    MutableSet as MutableSet,
    Reversible as Reversible,
    Sequence as Sequence,
    Sized as Sized,
    TypeVar,
    ValuesView as ValuesView,
)
from typing_extensions import final

if sys.version_info >= (3, 9):
    from types import GenericAlias as GenericAlias  # undocumented

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
class dict_keys(KeysView[_KT_co], Generic[_KT_co, _VT_co]):  # undocumented
    if sys.version_info >= (3, 10):
        mapping: mappingproxy[_KT_co, _VT_co]

@final
class dict_values(ValuesView[_VT_co], Generic[_KT_co, _VT_co]):  # undocumented
    if sys.version_info >= (3, 10):
        mapping: mappingproxy[_KT_co, _VT_co]

@final
class dict_items(ItemsView[_KT_co, _VT_co], Generic[_KT_co, _VT_co]):  # undocumented
    if sys.version_info >= (3, 10):
        mapping: mappingproxy[_KT_co, _VT_co]

EllipsisType = ellipsis  # undocumented # noqa F811 from builtins
generator = Generator  # undocumented
coroutine = Coroutine  # undocumented
async_generator = AsyncGenerator  # undocumented
