import sys
import typing
from typing import (
    ClassVar, ContextManager, Counter, DefaultDict, Deque,
    NewType, overload, Text, TYPE_CHECKING,
)

if sys.version_info >= (3, 3):
    from typing import ChainMap

if sys.version_info >= (3, 5):
    from typing import (
        AsyncIterable, AsyncIterator, AsyncContextManager, Coroutine,
    )

if sys.version_info >= (3, 6):
    from typing import AsyncGenerator

if sys.version_info >= (3, 6):
    from typing import Collection
else:
    _T_co = typing.TypeVar('_T_co', covariant=True)
    class Collection(typing.Sized,
                     typing.Iterable[_T_co],
                     typing.Container[_T_co],
                     typing.Generic[_T_co]):
        ...

# Return type that indicates a function does not return.
# This type is equivalent to the None type, but the no-op Union is necessary to
# distinguish the None type from the None value.
NoReturn = typing.Union[None]
