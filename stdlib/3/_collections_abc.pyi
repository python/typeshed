
import sys

from typing import (
    AsyncIterable as AsyncIterable,
    AsyncIterator as AsyncIterator,
    Awaitable as Awaitable,
    ByteString as ByteString,
    Container as Container,
    Coroutine as Coroutine,
    Generator as Generator,
    Hashable as Hashable,
    Iterable as Iterable,
    Iterator as Iterator,
    Sized as Sized,
    Callable as Callable,
    Mapping as Mapping,
    MutableMapping as MutableMapping,
    Sequence as Sequence,
    MutableSequence as MutableSequence,
    AbstractSet as Set,
    MutableSet as MutableSet,
    MappingView as MappingView,
    ItemsView as ItemsView,
    KeysView as KeysView,
    ValuesView as ValuesView,
)

if sys.version_info >= (3, 6):
    from typing import (
        Collection as Collection,
        Reversible as Reversible,
        AsyncGenerator as AsyncGenerator,
    )

# Without the real definition, mypy and pytest both think that __all__ is empty, so re-exports nothing
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
