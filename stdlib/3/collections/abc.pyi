# Stubs for collections.abc (introduced from Python 3.3)
#
# https://docs.python.org/3.3/whatsnew/3.3.html#collections
import sys

from . import (
    Callable as Callable,
    Container as Container,
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
    Sequence as Sequence,
    Set as Set,
    Sized as Sized,
    ValuesView as ValuesView,
)

if sys.version_info >= (3, 5):
    from . import (
        Generator as Generator,
        ByteString as ByteString,
        Awaitable as Awaitable,
        Coroutine as Coroutine,
        AsyncIterable as AsyncIterable,
        AsyncIterator as AsyncIterator,
    )

if sys.version_info >= (3, 6):
    from . import Collection as Collection, Reversible as Reversible, AsyncGenerator as AsyncGenerator
