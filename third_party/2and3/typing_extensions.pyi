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

# Return type that indicates a function does not return.
# This type is equivalent to the None type, but the no-op Union is necessary to
# distinguish the None type from the None value.
NoReturn = typing.Union[None]
