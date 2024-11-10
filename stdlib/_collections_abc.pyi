import sys
from abc import abstractmethod
from builtins import dict_items as _dict_items, dict_keys as _dict_keys, dict_values as _dict_values
from typing import (  # noqa: Y022,Y038
    AbstractSet as Set,
    AsyncGenerator as AsyncGenerator,
    AsyncIterable as AsyncIterable,
    AsyncIterator as AsyncIterator,
    Awaitable as Awaitable,
    Callable as Callable,
    Collection as Collection,
    Container as Container,
    Coroutine as Coroutine,
    Generator as Generator,
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
    Protocol,
    Reversible as Reversible,
    Sequence as Sequence,
    Sized as Sized,
    ValuesView as ValuesView,
    runtime_checkable,
)

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
]
if sys.version_info < (3, 14):
    from typing import ByteString as ByteString  # noqa: Y057

    __all__ += ["ByteString"]

if sys.version_info >= (3, 12):
    __all__ += ["Buffer"]

if sys.version_info >= (3, 12):
    @runtime_checkable
    class Buffer(Protocol):
        @abstractmethod
        def __buffer__(self, flags: int, /) -> memoryview: ...

dict_keys = _dict_keys  # undocumented
dict_items = _dict_items  # undocumented
dict_values = _dict_values  # undocumented
