# Stubs for collections.abc (introduced from Python 3.3)
#
# https://docs.python.org/3.3/whatsnew/3.3.html#collections
import sys

from . import Callable as Callable
from . import Container as Container
from . import Hashable as Hashable
from . import ItemsView as ItemsView
from . import Iterable as Iterable
from . import Iterator as Iterator
from . import KeysView as KeysView
from . import Mapping as Mapping
from . import MappingView as MappingView
from . import MutableMapping as MutableMapping
from . import MutableSequence as MutableSequence
from . import MutableSet as MutableSet
from . import Sequence as Sequence
from . import Set as Set
from . import Sized as Sized
from . import ValuesView as ValuesView

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
    from . import (
        Collection as Collection,
        Reversible as Reversible,
        AsyncGenerator as AsyncGenerator,
    )
